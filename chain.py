from block import Block

DIFFICULTY = 4

blockchain = []

genesis_block = Block('hi I am the first block', "0")
print("Hash for block 0:", genesis_block.hash)
genesis_block.mine(DIFFICULTY)

block_1 = Block("I am the second block", genesis_block.hash)
print("Hash for block 1:", block_1.hash)
block_1.mine(DIFFICULTY)

block_2 = Block("I am the third block", block_1.hash)
print("Hash for block 2:", block_2.hash)
block_2.mine(DIFFICULTY)

blockchain += [genesis_block, block_1, block_2]

def is_chain_valid(blockchain):
    for i in range(1, len(blockchain)):
        cur = blockchain[i]
        prev = blockchain[i-1]
        
        if not cur.hash == cur.calcHash():
            return False
        
        if not cur.previousHash == prev.hash:
            return False

        if not cur.hash[:DIFFICULTY] == "0"*DIFFICULTY:
            return False

    return True

print("blockchain valid: ", is_chain_valid(blockchain))
        
