import os

def environment_name(request):
    """
    Context processor to provide the environment name based on EUD_CONFIG_FILE.
    """
    config_file = os.environ.get("EUD_CONFIG_FILE", "")
    if not config_file:
        return {'env_name': 'Local', 'env_country': None}
    
    filename = os.path.basename(config_file).lower()
    env_country = None
    
    # Check for Germany
    if "germany" in filename or "ger" in filename:
        env_country = "GER"
        if "te" in filename or "te2" in filename:
            return {'env_name': 'TE2-GER', 'env_country': env_country}
        if "prod" in filename:
            return {'env_name': 'PROD-GER', 'env_country': env_country}
    
    # Check for Italy
    if "italy" in filename or "ita" in filename:
        env_country = "ITA"
        if "te" in filename or "te2" in filename:
            return {'env_name': 'TE2-ITA', 'env_country': env_country}
        if "prod" in filename:
            return {'env_name': 'PROD-ITA', 'env_country': env_country}
            
    # Check for Dev
    if "dev" in filename:
        return {'env_name': 'DEV', 'env_country': None}
        
    # Default to filename if no keyword matches
    return {'env_name': os.path.basename(config_file), 'env_country': env_country}
