from json_to_csv import read_file
from json_to_csv.convert_json import write_to_csv


def main(filename):
    data = read_file(filename)
    write_to_csv(data)


if __name__ == '__main__':
    main('data.json')
    # data = read_file('data.json')
    # write_to_csv(data)

    # print(data)
