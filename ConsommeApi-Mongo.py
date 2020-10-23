from flask import Flask
from flask import jsonify
from flask import request
from flask_pymongo import PyMongo 
from bson.json_util import dumps
from bson.objectid import ObjectId
from flask import jsonify, request
from flask import Flask, render_template, redirect, url_for, request
app=Flask(__name__)
app.config['MONGO_URI'] = 'mongodb://localhost:27017/DigiPages-stat'

mongo=PyMongo(app)

@app.route('/products')
#show all the products 
def products():
    products = mongo.db.categorynavigations.find({'product'})
    resp = dumps(products)
    return resp

@app.route('/products/<id>')
#show with a specific id 
def prodI(id):
    prod = mongo.db.categorynavigations.find_one({'_id':ObjectId(id)})
    resp = dumps(prod)
    return resp 

@app.route('/delete/<id>',methods=['DELETE'])
##delete 
def delete_user(id):
    mongo.db.categorynavigations.delete_one({'id':ObjectId(id)})
    resp = jsonify("User deleted successfully ")
    resp.status_code = 200
    return resp

@app.route('/prodname')
def test():
    products = mongo.db.dataSet.find()
    resp = dumps(products)
    return resp




if __name__ == '__main__':
    app.run(debug=True)
