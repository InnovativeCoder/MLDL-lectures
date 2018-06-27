from flask import Flask, jsonify, request
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
    request_data = request.get_json() #this will allow us to get the json data
    new_store = {
        'name' : request_data['name'],
        'items' : []
    }
    stores.append(new_store)
    return jsonify(new_store)

#GET /store/<string:name>
@app.route('/store/<string:name>') # http://127.0.0.1:5000/store/some name
def get_store(name):
    #iterate over stores, if matches return that one, else return error
    for store in stores:
        if store['name'] == name:
            return jsonify(store)
    return jsonify({'message':'store not found'})

#GET /store
@app.route('/store')
def get_stores():
    return jsonify({'stores': stores}) #json takes a string of dictionaries

#POST /store/<string:name>/item {name:, price:}
@app.route('/store/<string:name>/item', methods =['POST'])
def create_items_in_store (name):
    for store in stores:
        if store['name'] == name:
            new_item = {
                'name' : request_data['name'],
                'price' : request_data['price']
            }
            store['items'].append(new_item)
            return jsonify(new_item)
    return jsonify({'message':'store not found'})


#GET /store/<string:name>
@app.route('/store/<string:name>/item')
def get_items_in_store(name):
    for store in stores:
        if store['name'] == name:
            return jsonify({'items': store['items']})
    return jsonify({'message':'item not found'})

if __name__ == '__main__':
   app.run()
