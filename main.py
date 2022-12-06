class Block:
    def __init__(self, data, previous_hash):
        self.data = data
        self.timestamp = time.time()
        self.previous_hash = previous_hash
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        # Calculate the hash of the block using the data, timestamp, and previous hash
        ...

class Blockchain:
    def __init__(self):
        self.blocks = []

    def add_block(self, data):
        # Add a new block to the chain
        ...

    def verify_chain(self):
        # Verify the integrity of the chain by checking the hashes of the blocks
        ...

blockchain = Blockchain()
blockchain.add_block("This is the first block in the chain")
blockchain.add_block("This is the second block in the chain")
blockchain.add_block("This is the third block in the chain")
