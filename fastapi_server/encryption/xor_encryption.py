from .encryption_interface import IEncryptor

class XOrEncryption(IEncryptor):
    def encrypt(self, data: str):
        key = "interpreter"
        return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(data))


    def decrypt(self, data: str):
        key = "interpreter"
        return ''.join(chr(ord(c) ^ ord(key[i % len(key)])) for i, c in enumerate(data))
