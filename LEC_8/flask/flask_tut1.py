from flask import Flask, jsonify
app = Flask(__name__)

stores = [ #contains list of dictionaries
    {
        'name' : 'My wonderful Store',
        'items' : [
                {
                'name': 'My Item',
                'price' : 200.00
                }
        ]
    }
]

#POST - used to recieve data
#GET - used to send data back

#Code flow

#POST /store data:{name:}
@app.route('/store', methods =['POST'])
def create_store ():
    pass

#GET /store/<string:name>
@app.route('/store/<string:name>') # http://127.0.0.1:5000/store/some name
def get_store(name):
    pass

#GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores}) #json takes a string of dictionaries

#POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods =['POST'])
def create_items_in_store (name):
    pass


#GET /store/<string:name>
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    pass

if __name__ == '__main__':
   app.run()
