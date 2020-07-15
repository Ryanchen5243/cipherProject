def caesar_cipher(text):
    encode = ""
    for char in text:
        if ((ord(char) < 97 or ord(char) > 122) and (ord(char) < 65 or ord(char) > 90)):
            encode += char
        elif (char == "X"):
            encode += "A"
        elif (char == "Y"):
            encode += "B"
        elif (char == "Z"):
            encode += "C"
        elif (char == "x"):
            encode += "a"
        elif (char == "y"):
            encode += "b"
        elif (char == "z"):
            encode += "c"
        else:
            encode += chr(ord(char) + 3)
    return encode
#print(caesar_cipher("Hi, what are you doing?"))

def decode_caesar_cipher(text):
    decode = ""
    for char in text:
        if ((ord(char) < 97 or ord(char) > 122) and (ord(char) < 65 or ord(char) > 90)):
            decode += char
        elif (char == "A"):
            decode += "X"
        elif (char == "B"):
            decode += "Y"
        elif (char == "C"):
            decode += "Z"
        elif (char == "a"):
            decode += "x"
        elif (char == "b"):
            decode += "y"
        elif (char == "c"):
            decode += "z"
        else:
            decode += chr(ord(char) -3)
    return decode
#print(decode_caesar_cipher("Kl, zkdw duh brx grlqj?"))