import os
import yaml

from correction.clean_yaml import clean_yaml

def read_file(input_filename):
    valid_extensions = ['.yaml', '.yml']

    for ext in valid_extensions:
        x = f'{input_filename}{ext}'
        if os.path.exists(x):
            try:
                with open(x, 'r') as f:
                    data = yaml.safe_load(f)
                    return data
            except yaml.YAMLError:
                try:
                    with open(x, 'r') as f:
                        data = f.read()
                        corrected_yaml = yaml.safe_load(clean_yaml(data))
                        return corrected_yaml
                except FileNotFoundError:
                    continue
        else: print(f"File does not exist: {x}")
    print(f"Error: No valid YAML or YAML file found for '{input_filename}'.")
    return None
    