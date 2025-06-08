import hashlib
import time

class Block:
    def __init__(self, index, timestamp, data, previous_hash=''):
        self.index = index
        self.timestamp = timestamp
        self.data = data
        self.previous_hash = previous_hash
        self.nonce = 0
        self.hash = self.calculate_hash()

    def calculate_hash(self):
        to_hash = str(self.index) + self.timestamp + str(self.data) + self.previous_hash + str(self.nonce)
        return hashlib.sha256(to_hash.encode()).hexdigest()

    def __str__(self):
        return f"Block {self.index}:\nData: {self.data}\nHash: {self.hash}\nPrevious Hash: {self.previous_hash}\n"

# Create blockchain
blockchain = []

# Genesis block
genesis_block = Block(0, time.ctime(), "Genesis Block", "0")
blockchain.append(genesis_block)

# Add two more blocks
for i in range(1, 3):
    prev_block = blockchain[-1]
    new_block = Block(i, time.ctime(), f"Block {i} data", prev_block.hash)
    blockchain.append(new_block)

# Display blocks
for block in blockchain:
    print(block)

# Tampering test
print("🔧 Tampering Block 1...")
blockchain[1].data = "Hacked Data"
blockchain[1].hash = blockchain[1].calculate_hash()

print("🔍 Checking blockchain validity:")
for block in blockchain:
    print(block)
