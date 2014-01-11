from flask import Flask, render_template, request
#from flask.ext.mail import Mail, Message   

app = Flask(__name__)

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

@app.route('/')
def login():
    return render_template("login.html")

@app.route('/home', methods=['POST','GET'])
def home():
    dp = open("foo.txt", "r+")
    data = dp.read()
    exec data
    dp.close

    return render_template("home.html",
        notifications = notifications,
        schedule = schedule,
        time_budget = time_budget)

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
	app.run(host="0.0.0.0",port=5000)
