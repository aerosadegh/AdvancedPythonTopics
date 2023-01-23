x = 0


def read_csv(filename, delimiter=",", encoding=None):
    # stuff read_csv
    with open(filename, "r", encoding=encoding) as f:
        content = [[item for item in row.split(delimiter)] for row in f.readlines()]
    return content
