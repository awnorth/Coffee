# Use this function to decode, may have to alter it if offset not given.

import string

alphabet_list = [letter for letter in string.ascii_lowercase]
secret = "Hqk, itmf fuyq pa kag imzf fa xqmhq?"
def caesarDecoder(message, offset):
    decoded_message =""
    for char in message:
        if char in alphabet_list:
            char = char.lower()
            index = alphabet_list.index(char)
            new_index = (index+offset)%26
            decoded_message += (alphabet_list[new_index])
        else:
            decoded_message += char
    return decoded_message


message = "insert message here"

print(caesarDecoder(message, 12))   
