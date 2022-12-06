import hashlib
import time

class Block:
    def __init__(self, data, previous_hash):
        self.data = data
        self.timestamp = time.time()
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        # Calculate the hash of the block using the data, timestamp, and previous hash
        block_data = (str(self.data) + str(self.timestamp) + str(self.previous_hash)).encode()
        return hashlib.sha256(block_data).hexdigest()

class Blockchain:
    def __init__(self):
        self.blocks = []

    def add_block(self, data):
        # Add a new block to the chain
        if len(self.blocks) == 0:
            previous_hash = None
        else:
            previous_hash = self.blocks[-1].hash

        new_block = Block(data, previous_hash)
        self.blocks.append(new_block)

    def verify_chain(self):
        # Verify the integrity of the chain by checking the hashes of the blocks
        for i in range(1, len(self.blocks)):
            previous_block = self.blocks[i-1]
            current_block
