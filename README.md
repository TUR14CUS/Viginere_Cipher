# Vigenere Cipher Implementation

## Overview
This Python project provides a robust implementation of the Vigenere cipher, a classical encryption technique that enhances the security of messages by using a polyalphabetic substitution method. The project consists of a `VigenereCipher` class, offering a user-friendly interface for encrypting and decrypting messages, as well as an alternative approach utilizing separate functions.

## VigenereCipher Class

### Initialization
To create an instance of the VigenereCipher class, initialize it with a key of your choice.

```python
# Create an instance of VigenereCipher with the key "Penguin"
vig_cipher = "Penguin"
cipher = VigenereCipher(vig_cipher)
```

### Encryption and Decryption
The VigenereCipher class provides methods for encrypting and decrypting messages.

```python
# Get the plaintext from user input
plaintext = input("Enter the plaintext: ")

# Encrypt the plaintext
ciphertext = cipher.encrypt(plaintext)

# Decrypt the ciphertext
decrypted_plaintext = cipher.decrypt(ciphertext)
```

### Example Output
```plaintext
Plaintext: HelloWorld
Ciphertext: RmgyyVvnos
Decrypted plaintext: Helloworld
```

## Alternative Approach

An alternative approach is presented using separate functions for encryption and decryption, allowing for a more modular and customizable implementation.

### Usage Example
```python
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
```
