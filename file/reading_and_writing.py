from file.reading import read_file
from file.writing import write_file


def read_and_write_file(input_filename):
    data = read_file(input_filename)

    if data:
        write_file(input_filename, data)
        print(f'Done! Contents of {input_filename} corrected in place!')
    else:
        print(f'Error: No data to write for {input_filename}')