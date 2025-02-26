from abc import ABC ,abstractmethod
class IEncryptor(ABC):
    @staticmethod
    def encrypt(self,logger):
        pass

    @staticmethod
    def decrypt(self,logger):
        pass
