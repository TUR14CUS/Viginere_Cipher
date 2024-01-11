class VigenereCipher:
    def __init__(self, key):
        self.key = key.lower()

    def encrypt(self, plaintext):
        ciphertext = ""
        key_index = 0

        for char in plaintext:
            char = char.lower()

            if char.isalpha():
                vig_key = self.key[key_index]
                vig_key_value = ord(vig_key) - ord("a")
                vig_char = chr(((ord(char) - ord("a") + vig_key_value) % 26) + ord("a"))
                key_index = (key_index + 1) % len(self.key)
            else:
                vig_char = char

            ciphertext += vig_char

        return ciphertext

    def decrypt(self, ciphertext):
        decrypted_plaintext = ""
        key_index = 0

        for char in ciphertext:
            char = char.lower()

            if char.isalpha():
                vig_key = self.key[key_index]
                vig_key_value = ord(vig_key) - ord("a")
                plain_char = chr(((ord(char) - vig_key_value - ord("a")) % 26) + ord("a"))
                key_index = (key_index + 1) % len(self.key)
            else:
                plain_char = char

            decrypted_plaintext += plain_char

        return decrypted_plaintext

# Create an instance of VigenereCipher with the key "Penguin"
vig_cipher = "Penguin"

# Get the plaintext from user input
plaintext = input("Enter the plaintext: ")

# Encrypt the plaintext using the VigenereCipher instance
cipher = VigenereCipher(vig_cipher)
ciphertext = cipher.encrypt(plaintext)

# Decrypt the ciphertext using the VigenereCipher instance
decrypted_plaintext = cipher.decrypt(ciphertext)

# Print the original plaintext, ciphertext, and decrypted plaintext
print("Plaintext: " + plaintext)
print("Ciphertext: " + ciphertext)
print("Decrypted plaintext: " + decrypted_plaintext)


# Alternative approach using separate functions for encryption and decryption

# Define a function to encrypt the plaintext using the Vigenere cipher
def vig_encrypt(plaintext, key, key_index):
    ciphertext = ""
    for char in plaintext:
        char = char.lower()

        if char.isalpha():
            vig_key = key[key_index]
            vig_key_value = ord(vig_key) - ord("a")
            vig_char = chr(((ord(char) - ord("a") + vig_key_value) % 26) + ord("a"))
            key_index = (key_index + 1) % len(key)
        else:
            vig_char = char

        ciphertext += vig_char

    return ciphertext

# Define a function to decrypt the ciphertext using the Vigenere cipher
def vig_decrypt(ciphertext, key, key_index):
    decrypted_plaintext = ""
    for char in ciphertext:
        char = char.lower()

        if char.isalpha():
            vig_key = key[key_index]
            vig_key_value = ord(vig_key) - ord("a")
            plain_char = chr(((ord(char) - vig_key_value - ord("a")) % 26) + ord("a"))
            key_index = (key_index + 1) % len(key)
        else:
            plain_char = char

        decrypted_plaintext += plain_char

    return decrypted_plaintext

# Get the plaintext from user input
plaintext = input("Enter the plaintext: ")

# Encrypt the plaintext using the vig_encrypt function
key_index = 0
ciphertext = vig_encrypt(plaintext, vig_cipher, key_index)

# Decrypt the ciphertext using the vig_decrypt function
decrypted_plaintext = vig_decrypt(ciphertext, vig_cipher, key_index)

# Print the original plaintext, ciphertext, and decrypted plaintext
print("Plaintext: " + plaintext)
print("Ciphertext: " + ciphertext)
print("Decrypted plaintext: " + decrypted_plaintext)