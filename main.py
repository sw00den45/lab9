#hi
def decode(encoded_password):
    decoded_password=""
    for character in encoded_password:
        if int(character)>=3:
            value_to_add=int(character)-3
            value_to_add=str(value_to_add)
            decoded_password+=value_to_add
        elif int(character)<3:
            changed_value=int(character)+10
            value_to_add=changed_value-3
            decoded_password+=str(value_to_add)
    return decoded_password
