#Use this function to encode your message, use what ever offset you'd like. Don't tell.
import string

alphabet_list = [letter for letter in string.ascii_lowercase]

def caesarEncoder(message, offset):
    encoded_message = ""
    for char in message:
        char = char.lower()
        if char in alphabet_list:
            index = alphabet_list.index(char)
            new_index = (index-offset+26)%26
            encoded_message += alphabet_list[new_index]
        else:
            encoded_message += char
    return print(encoded_message)

