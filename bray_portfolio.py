from flask import Flask , redirect , url_for , render_template , request , session , flash

app = Flask(__name__)

@app.route('/home')
@app.route('/')
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)





