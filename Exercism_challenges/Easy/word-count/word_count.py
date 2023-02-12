import re
def count_words(sentence):
    # substitue any special characters in the sentence with whitespace
    words =re.sub("[!@#$%^&*(),.?\n\t:{}|<>_]"," ", sentence.lower())
    ch = ["' "," '","''"]
    for i in ch:
        words =words.replace(i,' ')
    # split the words based on the whitespace
    words = re.split(" ",words)
    dic = {}
    for i in words:
        # remove any trailing qoutation mark present in words
        if i.endswith("'"):
            i = i[:-1]
            words.append(i)
        # omit any whitespaces in our list of words
        if i != '':
            counter =words.count(i)
            # appending to the dictionary
            dic[i] = counter
    return dic