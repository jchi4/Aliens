from flask import Flask, render_template, request, redirect, flash
from flask_mysqldb import MySQL
from scripts.scraper import getReddit
import yaml

app = Flask(__name__)

# Configure db
db = yaml.safe_load(open("db.yaml"))
app.config['MYSQL_HOST'] = db['mysql_host']
app.config['MYSQL_USER'] = db['mysql_user']
app.config['MYSQL_PASSWORD'] = db['mysql_password']
app.config['MYSQL_DB'] = db['mysql_db']

# app.config['MYSQL_HOST'] = 'aws-lab.cu3ottuyfwbk.us-east-1.rds.amazonaws.com'
# app.config['MYSQL_USER'] = 'admin'
# app.config['MYSQL_PASSWORD'] = '29!nt$XELNE1'
# app.config['MYSQL_DB'] = 'flaskapp'

mysql = MySQL(app)

@app.route('/')
def index():
        # data = getReddit() #getting back the pandas dataframe of json data
        # if data != None:
        #     return render_template('index.html', data=data)
        # else:
        #     return render_template("error.html")

        data = getReddit() #getting back the pandas dataframe of json data
        return render_template('index.html', data=data)
        # if request.method == 'POST':
        #     # Fetch form data
        #     userDetails = request.form
        #     if userDetails['name'] != '' and userDetails['email'] != '': #if both fields are not empty
        #         name = userDetails['name']
        #         email = userDetails['email']
        #         cur = mysql.connection.cursor()
        #         cur.execute("INSERT INTO users(name, email) VALUES(%s, %s)",(name, email))
        #         mysql.connection.commit()
        #         cur.close()
        #         return "<p>Success</p>"
        # return render_template('index.html')

@app.route('/newsletter', methods=['GET', 'POST'])
def newsletter():
        if request.method == 'POST':
            # Fetch form data
            userDetails = request.form
            if userDetails['name'] != '' and userDetails['email'] != '': #if both fields are not empty
                name = userDetails['name']
                email = userDetails['email']
                cur = mysql.connection.cursor()
                cur.execute("INSERT INTO users(name, email) VALUES(%s, %s)",(name, email))
                mysql.connection.commit()
                cur.close()
                # flash("You have signed up for the newsletter! Thank you!")
                return redirect(request.url)

        return render_template('newsletter.html')

if __name__ == "__main__":
        app.run()