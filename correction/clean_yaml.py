import yaml
from correction.clean_string import clean_string
from correction.convert_tabs_to_spaces import convert_tabs_to_spaces
from correction.remove_special_characters import remove_special_characters


def clean_yaml(yaml_content):
    cleaned_yaml_content = remove_special_characters(yaml_content)
    parsed_yaml = yaml.safe_load(cleaned_yaml_content)
    cleaned_yaml_content = convert_tabs_to_spaces(cleaned_yaml_content)


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