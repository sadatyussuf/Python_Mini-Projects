import pathlib

BASEDIR = pathlib.Path(__file__).parent

txt_file = list(BASEDIR.glob("*.txt"))[0]

# print(txt_file)
with open(txt_file, "r") as f:
    readf = f.read()
    readf = readf.split("\n")
    res = []
    count = 0
    for num in readf:
        if num == "":
            res.append(count)
            count = 0
        else:
            count += int(num)

    print(max(res))
    # print(readf)
