from flask import Flask,render_template,redirect,flash,session,url_for
app = Flask(__name__)
app.secret_key = "arvi"
@ app.route('/home')
def home():
    return render_template('home.html')
if __name__ == "__main__":
    app.run(debug=True)