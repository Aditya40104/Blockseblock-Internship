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

    def mine_block(self, difficulty):
        print(f"⛏️ Mining block with difficulty: {difficulty}")
        start_time = time.time()
        target = '0' * difficulty

        while self.hash[:difficulty] != target:
            self.nonce += 1
            self.hash = self.calculate_hash()

        end_time = time.time()
        print(f"✅ Block mined: {self.hash}")
        print(f"🔢 Nonce: {self.nonce}, ⏱️ Time taken: {round(end_time - start_time, 4)}s")

# Example mining
block = Block(1, time.ctime(), "Some important data", "0000abc")
block.mine_block(difficulty=4)
