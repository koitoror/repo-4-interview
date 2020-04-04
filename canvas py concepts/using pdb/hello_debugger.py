import json
import pdb

def path_to_dict(path):
    """Open file at provided path and return as dictionary."""
    with open(path) as json_file:
        json_dict = json.load(json_file)
    return json_dict

def print_values(input_dict):
    """Loop through dictionary and print values."""
    pdb.set_trace()
    for k, v in input_dict.items():
        print('{0}: {1}'.format(k, v))


def main():
    """Entrypoint to application."""
    pdb.set_trace()
    sample_dict = path_to_dict('sample.json') # path not absolute and zworks if python file run from this directory
    print_values(sample_dict)


if __name__ == '__main__':
    main()