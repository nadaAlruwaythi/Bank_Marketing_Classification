from flask import Flask, render_template, request, jsonify
from pycaret.classification import *
import pandas as pd
import numpy as np
import csv
import webbrowser

app = Flask(__name__)

model = load_model('the_model1')


cols = ['age', 'job', 'marital', 'education', 'default', 'housing', 'loan', 'contact', 'poutcome']

@app.route("/")
def home():
    return render_template("homepage.html")

@app.route("/calculate")
def cal():
    return render_template("calculate.html") 

@app.route("/contactus")
def contant():
    return render_template("contactus.html")

@app.route("/result", methods=["POST", "GET"])
def result():

    int_feautres = [x for x in request.form.values()]
    final = [np.array(int_feautres)]
    predictio = model.predict(final)
    catg = ["Yes", "NO"]
    output = catg[int(predictio[0])]
    with open('GFG.csv', 'a', newline='') as f: 
        wr = csv.writer(f)
        if f.tell() == 0:
            wr.writerow(cols)
        wr.writerows(final) 
    st = " "
    if output == "Yes":
        st =  "The client subscribed to a term deposit"
    elif output == "NO":
        st = "The client has not subscribed to a term deposit"
   

    return render_template("finalresult.html", pred='  {}'.format(output), content=st)


@app.route("/aboutweb")
def about():
    return render_template("aboutweb.html")

@app.route("/userinformation")
def prediction():
    return render_template("userinformation.html")

if __name__ == "__main__":
    app.run(debug=True)