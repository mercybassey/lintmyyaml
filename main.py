import yaml

def read_file(input_filename):
    with open(f'{input_filename}.yaml', 'r') as f:
        data = yaml.safe_load(f)
        return data
    
def write_file(output_filename, data):
    with open(f'{output_filename}.yaml', 'w') as file:
        yaml.dump(data, file, sort_keys=False)

def read_and_write_file(input_filename, output_filename):
    data = read_file(input_filename)

    if data:
        write_file(output_filename, data)
        print(f'Done! Contents of {input_filename} written to {output_filename}')

read_and_write_file('example', 'output')