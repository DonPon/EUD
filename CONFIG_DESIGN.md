# Architectural Design: Environment-Agnostic Bot Configuration

## 1. Overview
This design outlines a pattern for building portable, environment-agnostic Python automation bots. It enables a single executable (`.exe`) to be deployed across multiple environments (e.g., DE-TE2, DE-PROD, IT-TE2, IT-PROD, DEV) without recompilation. Configuration is externalized via YAML files, and environment selection is handled via command-line arguments or an interactive fallback.

## 2. Architectural Components

### 2.1. Entry Point: `main.py`
The primary orchestration script for the bot.
*   **Responsibility**: 
    1.  Parse command-line arguments using `argparse`.
    2.  Expect a `--config-file` argument (the full system path to the target YAML).
    3.  If the argument is missing, invoke the interactive environment selection prompt via `europe_domestic_utils`.
    4.  Pass the resolved configuration path to the configuration manager (`config.py`).

### 2.2. Configuration Interface: `config.py`
The internal bridge module that abstracts configuration access.
*   **Responsibility**:
    1.  Receive the validated configuration file path from `main.py`.
    2.  Utilize `europe_domestic_utils` to load and parse the YAML.
    3.  Provide a clean, read-only interface (e.g., a dictionary or configuration object) for the bot’s business logic to access settings.
    4.  Implement caching of the loaded configuration object to optimize performance by avoiding repeated disk I/O.

### 2.3. Utility Submodule: `europe_domestic_utils` (Black Box)
The utility library handling infrastructure-related tasks.
*   **Responsibility**: 
    1.  Provide the `get_config_path()` function, which triggers a Tkinter dialog for user-selection of a config file if no CLI path is provided.
    2.  Provide a robust `load_validated_yaml(path)` function that reads, parses, and validates the schema of the YAML configuration.

## 3. Deployment Strategy (ADT)
The system is designed for deployment via the "ADT" tool, facilitating easy environment switching without altering the binary.

*   **Automated Usage (e.g., Scheduled Tasks)**: 
    `bot.exe --config-file "C:\Path\To\Configs\DE_PROD.yaml"`
*   **Manual Usage (Interactive)**: 
    `bot.exe` (User selects the appropriate config file via a triggered Tkinter window).

## 4. Contract Definition
To ensure the bot remains decoupled from `europe_domestic_utils`, the following contract must be maintained:

| Function | Signature | Expected Behavior |
| :--- | :--- | :--- |
| `get_config_path()` | `() -> str` | If no path is provided, launches Tkinter and returns user-selected path. |
| `load_validated_yaml(path)` | `(str) -> dict` | Reads YAML, validates schema, returns dict. |

## 5. Summary of Design Principles
1.  **Immutability**: The executable remains unchanged across environments.
2.  **Externalization**: Environment-specific settings are confined to standalone YAML files.
3.  **Flexibility**: CLI-first approach for automated pipelines, interactive-fallback for manual operation.
4.  **Separation of Concerns**: The bot logic is isolated from configuration loading and utility logic.
