import re
def is_isogram(string):
    # removing all non alphanumeric characters
    rm_sp =re.split('[^a-zA-Z0-9]', string)
    # converting the resulting list back to a string
    cv_str = ''.join(rm_sp)
    # convert all characters to lowercase
    cv_str = cv_str.lower()
    # getting a list of all the individaul characters
    c_list = [i for i in cv_str]
    # getting a set of unique characters
    s_list = set(c_list)
    # check if the lenght of the two lists are equal
    if len(c_list) != len(s_list):
        return False
    else:
        return True
