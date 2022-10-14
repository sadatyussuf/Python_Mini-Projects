import csv
from dataclasses import asdict


def write_to_csv(rows):
    rows_dict = asdict(rows[0])
    fieldnames = list(rows_dict.keys())

    with open('results.csv', 'w') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for row in rows:
            row = asdict(row)
            writer.writerow(row)

    print(fieldnames)
