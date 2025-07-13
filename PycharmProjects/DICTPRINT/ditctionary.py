from flask import Flask ,request,jsonify
import mysql.connector



#for SQL connection
db = mysql.connector.connect(host='localhost',
                             user='root',
                             password='vidya143',
                             database='cardata',
                            )
app=Flask(__name__)

@app.route('/SQL_DATA_to_Postman',methods=['GET'])
def GetDataUsingSql():
    result=''
    with db.cursor() as cursor:
        sql="SELECT * FROM car limit 5"
        cursor.execute(sql)
        result=cursor.fetchall()
        result=str(result)
    return result

if __name__ == '__main__':
    app.run()