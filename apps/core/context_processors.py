import os

def environment_name(request):
    """
    Context processor to provide the environment name based on EUD_CONFIG_FILE.
    """
    config_file = os.environ.get("EUD_CONFIG_FILE", "")
    if not config_file:
        return {'env_name': 'Local'}
    
    filename = os.path.basename(config_file).lower()
    
    # Check for Germany
    if "germany" in filename or "ger" in filename:
        if "te" in filename or "te2" in filename:
            return {'env_name': 'TE2-GER'}
        if "prod" in filename:
            return {'env_name': 'PROD-GER'}
    
    # Check for Italy
    if "italy" in filename or "ita" in filename:
        if "te" in filename or "te2" in filename:
            return {'env_name': 'TE2-ITA'}
        if "prod" in filename:
            return {'env_name': 'PROD-ITA'}
            
    # Check for Dev
    if "dev" in filename:
        return {'env_name': 'DEV'}
        
    # Default to filename if no keyword matches
    return {'env_name': os.path.basename(config_file)}
