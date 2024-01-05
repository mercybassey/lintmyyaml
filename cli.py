import argparse
from file.reading_and_writing import read_and_write_file

def main():
    parser = argparse.ArgumentParser(description='YAML Correction CLI Tool')
    parser.add_argument('filename', help='Input YAML file name without extension(both ."yml" and ".yaml" extensions are supported)')
    args = parser.parse_args()

    read_and_write_file(args.filename)

if __name__ == '__main__':
    main()
