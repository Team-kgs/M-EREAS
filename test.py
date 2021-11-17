# import requests
# import json
# 
# URL = 'http://127.0.0.1:5000/'
# '''res = requests.get(URL, params={'token': '4e7cc2fe113f061f7f2c8f2a65890669b3a4c53975064216fcfb8c0cf5a4dfa6'})
# print(res.json())
# '''
# requests.post(URL+'chain/add_block', data=json.dumps({
#                             'Sender': 'USER',
#                             'Receiver': 'ChainSERVER',
#                             'Map Position': {},
#                         }))
from ursina import *
app = Ursina()

text = Text(text='gooadfasdfasfasdfasafasdfasafsdfa', parent = camera.ui,text_colors=color.azure)

app.run()