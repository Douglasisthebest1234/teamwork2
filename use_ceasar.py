from caesar_cipher import encrypt, decrypt
from sha256 import sha_256


message = "Hello, World!"
shift = 3

secret = encrypt(message, shift)
print("Original: ", message)
print("Encrypted:", secret)
print("Decrypted:", decrypt(secret, shift))
print("SHA256:   ", sha_256(message))
