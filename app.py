import datetime
from flask import Flask, render_template, request, redirect, url_for
from pymongo import MongoClient
#from flask.ext.mail import Mail, Message   

app = Flask(__name__)
client = MongoClient('localhost', 27017)

testdb = client['test-database']
testusers = testdb['test-users']

databases = ['notificationdb']#, scheduledb, timebudgetdb']

"""app.config.update(dict(
    DEBUG = True,
    MAIL_SERVER = 'smtp.gmail.com',
    MAIL_PORT = 587,
    MAIL_USE_TLS = True,
    MAIL_USE_SSL = False,
    MAIL_USERNAME = 'concentratedvictory@gmail.com',
    MAIL_PASSWORD = '',
))


mail = Mail(app)   
"""

"""
To make a user, you input your email. The email then gives you a key
that you input in the "new user" page (whose link is hidden and only
    accessible directly or 

"""


@app.route('/')
def login():
    return render_template("login.html")

@app.route('/home', methods=['POST','GET'])
def home():

    valid = False

    username = request.form['username']
    password = request.form['password']

    c = testusers.find({ "username": username, "password": password})

    user = next(c, None)
    if user:
        valid = True

    # woah, txt file database magic here

    dp = open("foo.txt", "r+")
    data = dp.read()
    exec data
    dp.close

    # such magic
    """
    notifications = []

    if valid:
        for dbname in databases:
            cursor = testdb[dbname].find()
            if dbname == "notificationdb":
                for notification in cursor:
                    notifications.append(notification)
            #elif dbname == "schedule":
            #    for scheduleevents in cursor:
            #        schedule.append(scheduleevents)
            #elif dbname == "time_budget":
            #    for timeevents in cursor:
            #        time_budget.append(time_budget)
            """

    if valid:
        print notifications
        return render_template("home.html",
            notifications = notifications)
    else:
        return redirect(url_for("login"))

@app.route('/closefriends', methods=['POST', 'GET'])
def closefriends():
	return render_template("closefriends.html")

@app.route('/timebudget', methods=['POST', 'GET'])
def timebudget():
    return render_template("timebudget.html")

@app.route('/yes', methods=['POST', 'GET'])
def yes():
    #if request.method=="GET":
        return render_template("yes.html")
"""    else:
        print request.form.keys()
        msg = Message('pico support', sender='concentratedvictory@gmail.com', recipients=[request.form['email']])
        msg.body = 'Thanks for signing up for pico! We are still under development, however; check back soon! -pico'
        msg.html = 'Thanks for signing up for pico! We are still under development, however; check back soon! <br/> -pico'
        with app.app_context():
            mail.send(msg)
        return render_template('yes.html', email=request.form['email'])
"""
 
if __name__=="__main__":
	app.debug=True
	app.run(host="0.0.0.0",port=5007)
