from datetime import datetime
from utils import applySha256

class Block:
    def __init__(self, data, previousHash):
        self.data = data
        self.previousHash = previousHash
        self.timeStamp = datetime.now()
        self.nonce = 0
        self.hash = self.calcHash()

    def calcHash(self):
        return applySha256(str(self.previousHash) 
                + str(self.timeStamp.timestamp()) 
                + str(self.data)
                + str(self.nonce))

    def mine(self, difficulty):
        target = "0"*difficulty
        # print(target)
        while not self.hash[:difficulty] == target:
            self.nonce += 1
            self.hash = self.calcHash()
            # print(self.hash[:difficulty])
        print("Block mined")


