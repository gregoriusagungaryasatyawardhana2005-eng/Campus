import random
import string

chars = " " + string.punctuation + string.digits + string.ascii_letters
chars = list(chars)
key = chars.copy()

random.shuffle(key)

print(f"chars: {chars}")
print(f"key: {key}")

plaint_text = input("Message to encrypt: ")
cipher_text = " "

for letter in plaint_text:
    index = chars.index(letter)
    cipher_text += key[index]

print(f"original message {plaint_text}")
print(f"ciphered message {cipher_text}")

Enable_Decrypt = input("y/n")
if Enable_Decrypt == "y":
    input_decrypt = input("Message to decrypt")
    decrypt_text = " "
    for letter in input_decrypt:
        index = key.index(letter)
        decrypt_text += chars[index]
print(f"Decrypted text {decrypt_text}")