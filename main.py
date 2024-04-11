#Shane Wooden

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

def encode(password):
    new_password = ''
    for number in password:
        if number == '9':
            new_password += '2'
        if number == '8':
            new_password += '1'
        if number == '7':
            new_password += '0'
        else:
            new_password += str(int(number)+3)
    return new_password

if __name__ == '__main__':
    while True:
        print('Menu\n-------------\n1. Encode\n2. Decode\n3. Quit\n')
        option = int(input('Please enter an option: '))
        if option == 3:
            break
        if option == 1:
            password = str(input('Please enter your password to encode: '))
            encoded_password = encode(password)
            print('Your password has been encoded and stored!')
        if option == 2:
            decoded_password = decode(encoded_password)
            print(f'The encoded password is {encoded_password}, and the original password is {decoded_password}.')