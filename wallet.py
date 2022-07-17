from ecdsa import SigningKey

class Wallet:
    def __init__(self):
        self.private_key, self.public_key = self.generate_keypair()

    def generate_keypair(self):
        sk = SigningKey.generate()
        vk = sk.verifying_key
        return (sk, vk)
    
