from utils import *

class Transaction:
    def __init__(self, frm, to, value, inputs):
        self.sender = frm
        self.receiver = to
        self.value = value
        self.inputs = inputs
        self.sequence = 0

    def calc_hash(self):
        return applySha256(
                str(self.sender) 
                + str(self.receiver)
                + str(value)
                + str(sequence))

    def generate_sig(self, private_key):
        data = str(self.sender.to_string()) + str(self.receiver.to_string()) + str(self.value)
        self.signature = apply_ecdsa_sig(private_key, data) 

    def verify_sig(self):
        data = str(self.sender.to_string()) + str(self.receiver.to_string()) + str(self.value)
        return verify_ecdsa_sig(self.sender, data, self.signature)
