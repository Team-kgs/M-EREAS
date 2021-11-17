from blockchain import blockchain
from flask import Flask, request, jsonify
import json

Map_NFT = blockchain()

app = Flask(__name__)

app.config['JSONIFY_PRETTYPRINT_REGULAR'] = True

@app.route('/')
def hello():
    return "<h2>NTF SERVER: INDEX_PAGE</h2>"

@app.route('/chain/informations', methods=['GET'])
def chain_info():
    NTF_Token = request.args.get('token')
    block = Map_NFT.chain
    for i in block:
        if i.hash == NTF_Token:
            response = {
                'NTF_token': i.hash,
                'transactions': i.transactions,
                'timestamp': i.timestamp
            }
            return jsonify(response), 200
    return "False Token"

@app.route('/chain/add_block', methods=['POST'])
def add_block_in_chain():
    params = json.loads(request.get_data(), encoding='utf-8')
    return Map_NFT.add_block(params).hash

app.run()