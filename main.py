import os
import yaml

def read_file(input_filename):
    valid_extensions = ['.yaml', '.yml']

    for ext in valid_extensions:
        x = f'{input_filename}{ext}'
        if os.path.exists(x):
            try:
                with open(x, 'r') as f:
                    data = yaml.safe_load(f)
                    return data
            except FileNotFoundError:
                continue
        else: print(f"File does not exist: {x}")
    print(f"Error: No valid YAML or YAML file found for '{input_filename}'.")
    return None
    
def write_file(output_filename, data):
    with open(f'{output_filename}.yaml', 'w') as file:
        yaml.dump(data, file, sort_keys=False)

def read_and_write_file(input_filename, output_filename):
    data = read_file(input_filename)

    if data:
        write_file(output_filename, data)
        print(f'Done! Contents of {input_filename} written to {output_filename}')

read_and_write_file('example', 'output')