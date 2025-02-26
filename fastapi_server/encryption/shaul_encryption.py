from .encryption_interface import IEncryptor


class ShaulEncryption(IEncryptor):
    def encrypt(self, data: str):
        return self.encryption(data)

    def decrypt(self, data: str):
        return self.decryption(data)

    def encryption(self, data):
        counter = 0
        array_encryption = ""
        for word in data:
            counter += 1
            nem = ord(word)
            if not counter % 10:
                array_encryption += chr(((counter * 2) ** 2) - counter)
            if nem < 100:
                nem -= 7
            if counter % 3 or not counter % 4:
                nem += 41
            if nem < 200:
                nem = ((nem + 2) ** 2)
            else:
                nem += 2
                nem += counter ** 2

            array_encryption += (chr(nem))
        return array_encryption

    def decryption(self, data):
        counter = 0
        true = True
        array_encryption = ""
        for word in data:
            counter += 1
            nem = ord(word)
            experience = (nem ** 0.5) - 2
            if not experience % 1:
                nem = experience
            else:
                nem -= counter ** 2
                nem -= 2
            if counter % 3 or not counter % 4:
                nem -= 41

            if nem + 7 < 100:
                nem += 7

            if counter % 10 or not true:
                array_encryption += (chr(int(nem)))
                true = True
            else:
                counter -= 1
                true = False
        return array_encryption
    