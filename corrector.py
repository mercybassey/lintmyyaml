import re
import yaml

def clean_string(input_string):
    if isinstance(input_string, str):
        return re.sub(r'^[^A-Za-z0-9]*', "", input_string)
    else:
        return input_string

def remove_special_characters(yaml_str):
    if isinstance(yaml_str, str):
        yaml_str = re.sub(r'[^A-Za-z0-9\s:\n-]', '', yaml_str)
        return yaml_str
    else:
        return yaml_str

def clean_yaml(yaml_content):
    cleaned_yaml_content = remove_special_characters(yaml_content)
    parsed_yaml = yaml.safe_load(cleaned_yaml_content)

    def clean_dict(input_dict):
        cleaned_dict = {}
        for key, value in input_dict.items():
            clean_key = clean_string(key)
            if isinstance(value, dict):
                cleaned_dict[clean_key] = clean_dict(value)
            else:
                cleaned_dict[clean_key] = clean_string(value)
        return cleaned_dict

    cleaned_parsed_yaml = clean_dict(parsed_yaml)

    return yaml.dump(cleaned_parsed_yaml, default_flow_style=False, sort_keys=False) 



