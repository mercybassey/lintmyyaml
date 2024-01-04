import re

def remove_special_characters(yaml_str):
    if isinstance(yaml_str, str):
        yaml_str = re.sub(r'[^A-Za-z0-9\s:\n-]', '', yaml_str)
        return yaml_str
    else:
        return yaml_str