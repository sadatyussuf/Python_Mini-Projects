import json
from json_to_csv.row_model import Row


def read_file(filename):
    rows = []

    with open(filename, 'r') as f:
        f = json.load(f)
        for item in f:
            row = Row(**item)
            rows.append(row)
    return rows
