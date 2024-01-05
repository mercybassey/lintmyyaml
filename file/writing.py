import os
import yaml

def write_file(input_filename, data):
    valid_extensions = ['.yaml', '.yml']
    for ext in valid_extensions:
        current_file = f'{input_filename}{ext}'
        if os.path.exists(current_file):
            with open(current_file, 'w') as file:
                yaml.dump(data, file, sort_keys=False)
            print(f'Done! Contents of {current_file} corrected in place!')
            return

    print(f"Error: No valid YAML or YAML file found for '{input_filename}'.")
