import re


def clean_string(input_string):
    if isinstance(input_string, str):
        return re.sub(r'^[^A-Za-z0-9]*', "", input_string)
    else:
        return input_string