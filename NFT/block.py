from datetime import datetime
from hashlib import sha256

# timestamp: 만들어진 시간
# hash: 현재 해시값
# prev hash: 이전 해시값
# nonce: 논스값(int)
# transaction: 데이터 트랙젠션

class block:
    def __init__(self, transactions, prev_hash, nonce=0):
        self.timestamp = datetime.now()
        self.transactions = transactions
        self.prev_hash = prev_hash
        self.nonce = nonce
        self.hash = self.generate_hash()

    def generate_hash(self):
        block_contents = str(self.timestamp) + str(self.transactions) + str(self.prev_hash) + str(self.nonce)
        block_hash = sha256(block_contents.encode())
        return block_hash.hexdigest()

    def print_block(self):
        print("timestamp:", self.timestamp)
        print("transactions:", self.transactions)
        print("current hash:", self.generate_hash())