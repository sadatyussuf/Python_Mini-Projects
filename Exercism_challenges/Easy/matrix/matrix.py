class Matrix:
    def __init__(self, matrix_string):
        self.matrix_string = matrix_string

    def row(self, index):
        string = self.matrix_string
        split_string = string.split('\n')
        split_list =split_string[index-1].split()
        int_list = list(map(int,split_list))
        return int_list

    def column(self, index):
        array = []
        string = self.matrix_string
        split_string = string.split('\n')
        test_list = [i.split() for i in split_string]
        for item in test_list:
            array.append(int(item[index-1]))
        return array
