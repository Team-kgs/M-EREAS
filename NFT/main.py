from blockchain import blockchain

Kcoin = blockchain()
print(Kcoin.chain)

transaaction1 ={
    'Sender': 'Kimkkochu',
    'Receiver': 'admin',
    'Amount': 1000,
}

Kcoin.add_block(transaaction1)
print(Kcoin.chain)
print(Kcoin.verify_blockchain())
print(Kcoin.chain[0].hash)

'''
Kcoin.chain[0].transactions = {
    'Sender': 'fuck',
    'Receiver': 'aa',
    'Amount': 1211,
}
print(Kcoin.verify_blockchain())
'''