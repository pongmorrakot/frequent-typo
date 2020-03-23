print("typo check")

charlist = ["1","!","2","@","3","#","4","$","5","%","6","^","7","&","8","*","9","(","0",")","-","_","=","+","q","Q","w","W","e","E","r","R","t","T","y","Y","u","U","i","I","o","O","p","P","[","{","]","}","a","A","s","S","d","D","f","F","g","G","h","H","j","J","k","K","l","L",";",":","z","Z","x","X","c","C","v","V","b","B","n","N","m","M",",","<",".",">","/","?","`","~"]

def compare(str1, str2):
    # compare the correct and typo strings
    # locate the index where it's different
    return str1 == str2

def insert(str1, index, char):
    # modify the string by insertion
    return str1[:index] + char + str1[index:]

def delete(str1, index ):
    # modify a string by deletion
    return str1[:index] + str1[index+1:]

def transpose(str1, index1, index2):
    # modify the string by switching two characters
    return str1[:index1] + str1[index2] + str1[index1+1:index2] + str1[index1] + str1[index2+1:]

def substitute(str1, index, char):
    # modify the string by substitute a char
    return str1[:index] + char + str1[index+1:]

def main(orig, typo, maxEdit):
    return correct(orig, typo)

def correct(orig, typo):
    if compare(orig, typo):
        return "0"
    for t in range(len(typo)):
        if compare(orig, delete(typo,t)):
            return "d"
        for u in range(len(typo)):
            if compare(orig, transpose(typo, t, u)):
                return "t"
        for c in charlist:
            if compare(orig, insert(typo, t, c)):
                return "i"
            elif compare(orig, substitute(typo, t, c)):
                return "s"
    return "x"

