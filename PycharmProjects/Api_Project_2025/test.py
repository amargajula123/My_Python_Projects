from flask import Flask,request,jsonify

app = Flask(__name__) # __name__ means all the named functions its going to import
# app is object of the "Flask" so that i can use fuctions of flask

@app.route('/reach',methods=['POST','GET'])  # This defines the endpoint /reach.
def test():
    if (request.method == 'POST'):
        a = request.json['num1'] # requesting data as json format you can send a data in
        b = request.json['num2'] # any format in "text" format or "string" or "numeric" format any format you want you can send
        result = a + b
        return jsonify(result)

@app.route('/reach_1',methods=['POST','GET'])
def test1():
    if (request.method == 'POST'):
        a = request.json['num1'] # requesting data as json format you can send a data in
        b = request.json['num2'] # any format in "text" format or "string" or "numeric" format any format you want you can send
        result = a - b
        return jsonify(result)

@app.route('/reach_2',methods=['POST','GET']) # This defines the endpoint /reach_2.
def test2():
    if (request.method == 'POST'):
        a = request.json['num1'] # requesting data as json format you can send a data in
        b = request.json['num2'] # any format in "text" format or "string" or "numeric" format any format you want you can send
        result = a * b                                                       # if a * b = 2*2 = 4
        return jsonify(str(result)) # the out will be prited as string format like =  "4" -> like string prints



# now i have execute the app that i have created so that i have to do bellow
if __name__ == '__main__':
    app.run(port=9000)  # so over all this will keep my server up and running when i execute,

    """
    TASK:-
    write a fuction to fetch a data from sql via API(postman)
    write a fuction to ferch a data from mongoDb via API(postman).
    """

    # this 2 lines is the constractor call of a python main function we are trying to do
    # we are saying that try to call a main method of a python class with name and
    # execute app what ever flask app that i created, with which we have binded functions of it,
    # and its keep on running,

    # URL(Uniform Resource Locator) = The complete web address where the API is hosted
    # example : http://127.0.0.1:9000/reach
    # Endpoint = The specific path inside the API "that provides a certain functionality"
    # Example: /reach in http://127.0.0.1:9000/reach
    # from above in this endpoint(api defines an endpoint) /reach

    # ✅ An API is a system that allows communication between applications.
    # ✅ It defines multiple endpoints, each endpoints serving a different function.
    # ✅ We can add as many endpoints as we want, depending on the application's needs.


