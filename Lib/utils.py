def text2dic(file_path, separator, dic={}):
    """
    convert line by line the content of the text file into a dictionnary,
    every line of the file readed correspond to a key and a value,
    the key equal to the part before the separator given in parameter and
    its value correspond to the part after the separator
    """
    try:
        with open(file_path, 'r') as file:
            for line in file :
                if separator in line:
                    key = line[:line.find(separator)]
                    value = line[line.find(separator)+1:].rstrip('\n')
                    dic[key] = value
    except:
        print("txt2dico as meet a problem verify if your path is correct")
    return dic


def getLastestLines(file_path, number_of_lines=1):
    """
    return the x lastest line in the file given
    if the given file contain less lines than x lines
    the the whole file content is return without errors
    """
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()
            lignes_wanted = ''
            if (len(lines) > number_of_lines) or (len(lines) == number_of_lines):
                lignes_wanted = lignes_wanted.join(lines[-number_of_lines:])
            if len(lines) < number_of_lines:
                if len(lines) != 0:
                    lignes_wanted = lignes_wanted.join(lines)
    except:
        print("getLastestLines as meet a problem verify if your path is correct")
    return lignes_wanted
