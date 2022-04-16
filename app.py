import pymongo
from flask import Flask, render_template,request
from flask_cors import CORS,cross_origin

app = Flask(__name__)

@app.route('/', methods = ["POST","GET"])
@cross_origin()
def homePage():
    return render_template("index.html")

@app.route('/ineuron-courses', methods = ["POST","GET"])
@cross_origin()
def ineuron_db():
    if request.method == "POST":
        try:
            CLIENT_URL = "mongodb+srv://shivansh:t2092081@shivansh-db2.kktnl.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
            client = pymongo.MongoClient(CLIENT_URL)
            db = client.test
            db = client["Scrapper"]
            Collection = db["iNeuron_Course"]
            ineuron_data  = []
            for i in Collection.find():
                ineuron_data.append(i)
            return render_template('results.html', ineuron_data=ineuron_data[0:(len(ineuron_data))])
        except:
            return "Problem occured in fetching data....Please Retry"

@app.route('/ineuron-courses-filter', methods = ["POST","GET"])
@cross_origin()
def ineuron_db2():
    if request.method == "POST":
        try:
            if request.form['filter'] != "":
                filter = str(request.form['filter'])

            CLIENT_URL = "mongodb+srv://shivansh:t2092081@shivansh-db2.kktnl.mongodb.net/myFirstDatabase?retryWrites=true&w=majority"
            client = pymongo.MongoClient(CLIENT_URL)
            db = client.test
            db = client["Scrapper"]
            Collection = db["iNeuron_Course"]
            ineuron_data  = []
            try:
                for i in Collection.find({"Title" : filter}):
                    ineuron_data.append(i)
            except:
                return "Course does not exist....Please check your course name"
            return render_template('results.html', ineuron_data = ineuron_data[0:(len(ineuron_data))])
        except:
            return "Problem occured in fetching data....Please Retry"

if __name__=="__main__":
    app.run(host="localhost",port = 8001)