import argparse
from file.reading_and_writing import read_and_write_file

def main():
    parser = argparse.ArgumentParser(description='YAML Correction CLI Tool')
    parser.add_argument('filenames', nargs='*', help='Input YAML file name without extension (both ".yml" and ".yaml" extensions are supported)')
    args = parser.parse_args()

    if not args.filenames:
        print('Error: At least one YAML file should be provided.')
    else:
        for filename in args.filenames:
            read_and_write_file(filename)

if __name__ == '__main__':
    main()
