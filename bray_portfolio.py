from flask import Flask , redirect , url_for , render_template , request , session , flash

app = Flask(__name__)
def home():
    return "Hello! this is the test page <h1>HELLO<h1>"

if __name__ == "__main__":
    app.run(host='0.0.0.0')





