from block import block

class blockchain:
    def __init__(self):
        self.chain = [] # save all block
        self.all_transactions = [] # save data chain & transactions
        self.genesis_block()

    def genesis_block(self):
        transactions = {}
        Block = block(transactions, 0)
        self.chain.append(Block)
        return self.chain

    def add_block(self, transactions):
        prev_block_hash = self.chain[-1].hash
        new_block = block(transactions, prev_block_hash)
        self.chain.append(new_block)
        return new_block
    
    def verify_blockchain(self):
        for i in range(1, len(self.chain)):
            current = self.chain[i]
            prev = self.chain[i-1]
            if current.hash != current.generate_hash():
                print("[!] 블록의 현재 해시가 블록의 생성된 해시와 같지 않습니다.")
                return False
            if prev.hash != prev.generate_hash():
                print("[!] 이전 블록의 해시는 현재 블록에 저장된 이전 해시 값과 일치하지 않습니다.")
                return False
            if current.prev_hash != prev.hash:
                return False
        return True