from flask import Flask,request,jsonify
import mysql.connector as conn
import pymongo


app=Flask(__name__)

@app.route('/sql_app',methods=['POST','GET'])

def sql_db_read():
    if (request.method)=='POST':

        data_req = request.json
        mydb=conn.connect(host=str(data_req["host"]),user=str(data_req["user"]),passwd=str(data_req["passwd"]),database=str(data_req["database"]) )
        cursor=mydb.cursor()
        querry = "select * from stdnt"
        cursor.execute(querry)
        #mydb.commit()
        result = str(cursor.fetchall())

        return {"result" : result }

@app.route('/mongo_app',methods=['POST','GET'])

def mongo_db_read():
    if (request.method)=='POST':

        data_req = request.json

        client = pymongo.MongoClient( data_req["conn_str"])
        db = client[data_req["database"]] #super_DB_1
        col = db[data_req["col"]] #super_DB_collection_1
        result = str(list(col.find()))
        return {"result" : result }

if __name__ =="__main__":
    app.run(host="localhost",port=9000)

