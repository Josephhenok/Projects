"""
This function encrypts a list using a key in list form from another file
The list has its values swapped with the position of that value from the key
The new swapped list is put into a cipher_text which is returned
"""
def encrypt(plain_text, key):
    cipher_text = []
    for i in range(len(plain_text)):
        cipher_text.append(key[plain_text[i]])
    return cipher_text
"""
This function decrypts a list using a key in list form from another file
The list has its values swapped with the value of the position from the key 
The new swapped list is put into a plain_text which is returned
"""
def decrypt(cipher_text, key):
    plain_text = []
    for i in range(len(cipher_text)):
        plain_text.append(key.index(cipher_text[i]))
    return plain_text
"""
This function reads a file as a list in binary
The list is then put into a variable (number), and returned
"""
def read_file(file_name):
    file = open(file_name,"rb")
    number = list(file.read())
    file.close()
    return (number)
"""
This function writes content given to a file
The function takes in content and the file they want it written to
The content is then written to the new file with nothing returned
"""
def write_file(file_name, content):
    file = open(file_name, "wb")
    file.write(bytes(content))
    file.close()
"""
This functions tests to see if all the functions above work
"""
def test_encryption():
    read_file("key")
    cipher_text = encrypt(read_file("plain_text"), read_file("key"))
    write_file("cipher_text", cipher_text)
    plain_text = decrypt(read_file("cipher_text"),read_file("key"))
    write_file("plain_text1", plain_text)

if __name__ == '__main__':
    test_encryption()


