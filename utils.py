import hashlib

def applySha256(input):
    return hashlib.sha256(bytes(input, 'utf-8')).hexdigest()

def apply_ecdsa_sig(private_key, inpt):
    return private_key.sign(bytes(inpt, 'utf-8'))

def verify_ecdsa_sig(public_key, data, signature):
    return public_key.verify(signature, bytes(data, 'utf-8'))
