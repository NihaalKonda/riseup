from flask import Flask, render_template, redirect, url_for, request
import pymongo
from flask_pymongo import PyMongo
from database import Database
app = Flask(__name__, static_url_path='')
name_key = {}
@app.before_first_request
def initialize_database():
    Database.initialize()
@app.route('/', methods=["GET", "POST"])
def home():
    documents = Database.show_docs()
    return render_template("base.html", documents=documents)
'''@app.route('/signup', methods=["GET", "POST"])
def signup_func():
    doc={
        'name':request.form.get("name_signup"),
        'email':request.form.get("email_signup"),
        'password':request.form.get("password_signup"),
        'keywords':(request.form.get("keyword_signup")).replace(" ", "").split(",")
    }
    Database.insert_record(doc)
    return redirect(url_for("home"))'''
@app.route('/signup', methods=["GET", "POST"])
def signup_func():
    #keyword_final = request.form.get("keyword_signup")
    #print(keyword_final)
    doc={
        'name':request.form.get("name_signup"),
        'email':request.form.get("email_signup"),
        'password':request.form.get("password_signup"),
        'keywords':request.form.get("keyword_signup")
    }
    #name_key[request.form.get("name_signup")] = keyword_final.replace(" ", "").split(",")
    name_key[request.form.get("name_signup")] = request.form.get("keyword_signup")
    Database.insert_record(doc)
    return render_template("base.html", namekeydict = name_key)
@app.route('/navbar', methods=["GET", "POST"])
def business_nav():
    keyword_search = request.form.get("business_search")
    business_list = []
    matches = []
    final_keys = list(name_key.keys())
    final_values = list(name_key.values())
    for index, item in enumerate(final_values):
        item_check = list(item.split("-"))
        if keyword_search in item_check:
            matches.append(final_keys[index])
    return render_template("base.html", business_results=matches, namekeydict = name_key)

@app.route('/payforward', methods=["GET", "POST"])
def payforward():
    keyword_search = request.form.get("company_name")
    final_keys = list(name_key.keys())
    donations = []
    for name in final_keys:
        if keyword_search in name:
            donations.append(name)
    return render_template("base.html", donations = donations)

#############################

'''for i in final_values:
        print(type(i))
        print(i)
        business_list = list(Database.DB.users.find({keyword_search: {'$in': i}}))'''
'''app = Flask(__name__, template_folder='templates')
app.config["MONGO_URI"] = "mongodb://localhost:27017/project-db"
mongo=PyMongo(app)

@app.route('/', methods=["GET", "POST"])
def home():
    if request.method=="GET":
        docs = mongo.db.Documents.find()
        return render_template("base.html", render_docs=docs)
    elif request.method=="POST":
        document = {}
        for item in request.form:
            document[item] = request.form[item]
        mongo.db.Documents.insert_one(document)
        return redirect('/')'''

if __name__=='__main__':
    app.run(debug=True)
