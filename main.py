import hashlib 
import datetime as date

class Block:
    def __init__(self, index, timestamp, data, previous_hash):
        self.index = index
        self.timestamp  = timestamp
        self.data = data
        self.previous_hash = previous_hash

        self.hash = self.hash_block()

    def hash_block(self):
        sha = hashlib.sha256()
        sha.update(str(self.index).encode() + 
                   str(self.timestamp).encode() + 
                   str(self.data).encode() + 
                   str(self.previous_hash).encode())
        
        return sha.hexdigest()
    
def create_genesis_block():
    return Block(0, date.datetime.now(), "Genesis Block", "0")


def next_block(last_block):
    index = last_block.index + 1
    timestamp = date.datetime.now()
    data = "Hey I'm block " + str(index)
    this_hash = last_block.hash
    
    return Block(index, timestamp, data, this_hash)


blockchain = [create_genesis_block()]
previous_block = blockchain[0]


for i in range(0, 20):
    block_to_add = next_block(previous_block)
    blockchain.append(block_to_add)
    previous_block = block_to_add

    print(f"Block [{block_to_add.index}] has been added to the blockchain!")
    print(f"Hash {block_to_add.hash}\n")