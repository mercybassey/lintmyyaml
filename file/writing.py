import yaml


def write_file(output_filename, data):
    with open(f'{output_filename}.yaml', 'w') as file:
        yaml.dump(data, file, sort_keys=False)
