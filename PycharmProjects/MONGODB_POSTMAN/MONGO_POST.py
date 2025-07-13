from flask import Flask, request, jsonify

import pymongo

client = pymongo.MongoClient(
    "mongodb+srv://amargajula:amargajula@cluster0.ec3uf.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
db = client.Super_DB_1

app=Flask(__name__)

@app.route('/pqr', methods=['GET'])
def fetch_mongo():
    col = db["super_DB_collection_1"]
    #data={"result":str(list(Colle_ction.find().limit(100)))}
    data ={"result":str(list(col.find()))}
    return jsonify(data)


if __name__ == '__main__':
    app.run()