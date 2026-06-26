import os
import subprocess
import time
import socket
import re
from playwright.sync_api import sync_playwright

def is_server_running(host, port):
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as sock:
        return sock.connect_ex((host, port)) == 0

def run_scenario(page, host, port, origin_uuid, mode, target_type=None, target_name=None):
    print(f"--- Running scenario: Origin={origin_uuid}, Mode={mode}, TargetType={target_type} ---")
    
    # Navigate
    page.goto(f"http://{host}:{port}/api/gui/relationship/add/?client_uuid={origin_uuid}")
    
    # Wait for selection
    page.wait_for_selector("#relationship-selector", state="visible")
    page.wait_for_timeout(1000)
    
    # Select mode
    if mode == 'create':
        page.click("text=Create New")
        page.wait_for_selector("#generic-crud-form:not(.d-none)", state="visible")
        page.fill("input[name='new_client_name']", target_name)
        page.select_option("select[name='new_client_type']", target_type)
    elif mode == 'existing':
        page.click("text=Search Existing")
        page.wait_for_selector("#generic-crud-form:not(.d-none)", state="visible")
        
        # Interact with Select2 dropdown
        page.click(".select2-dropdown")
        page.wait_for_selector(".select2-results__option", state="visible")
        # Click the first available option (excluding the placeholder)
        page.click(".select2-results__option:not(.select2-results__option--disabled)")
    
    page.wait_for_timeout(1000)
    # Submit
    page.click("button[type='submit']")
    
    # Assert
    # We allow navigation to both client and le lists depending on the section
    page.wait_for_url(re.compile(r'/(clients|le)/.*'), timeout=15000)
    print("Scenario successful!")

def run_relationship_test():
    # Start Server
    server_process = subprocess.Popen(["python", "start_app.py", "--port", "8003"])
    
    # Wait for server
    host, port = "127.0.0.1", 8003
    timeout = 30 # seconds
    start_time = time.time()
    while not is_server_running(host, port) and (time.time() - start_time) < timeout:
        time.sleep(1)
    
    if not is_server_running(host, port):
        server_process.terminate()
        raise Exception("Server failed to start")

    # UUIDs from DB
    np_uuid = "d7de102d-2f45-4159-bfbc-8141799da499"
    le_uuid = "1ce00e65-b42d-4123-ac2a-a7c678def0aa"

    # Define scenarios - expanded for comprehensiveness
    scenarios = [
        # Create modes
        {"origin_uuid": np_uuid, "mode": "create", "target_type": "np", "target_name": "Test NP to NP"},
        {"origin_uuid": np_uuid, "mode": "create", "target_type": "le", "target_name": "Test NP to LE"},
        {"origin_uuid": le_uuid, "mode": "create", "target_type": "np", "target_name": "Test LE to NP"},
        {"origin_uuid": le_uuid, "mode": "create", "target_type": "le", "target_name": "Test LE to LE"},
        
        # Existing modes
        {"origin_uuid": np_uuid, "mode": "existing"},
        {"origin_uuid": le_uuid, "mode": "existing"},
    ]

    try:
        # Run Test
        with sync_playwright() as p:
            browser = p.webkit.launch(headless=False)
            page = browser.new_page()
            
            for s in scenarios:
                run_scenario(page, host, port, **s)
            
            browser.close()
            print("All scenarios completed successfully!")
    except Exception as e:
        print(f"Test failed: {e}")
        raise
    finally:
        # Cleanup
        server_process.terminate()
        server_process.wait()

if __name__ == "__main__":
    run_relationship_test()
