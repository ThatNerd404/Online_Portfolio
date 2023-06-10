from flask import Flask , redirect , url_for , render_template , request , session , flash

app = Flask(__name__)

@app.route('/home')
@app.route('/')
def home():
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

#TODO: improve website by:
#TODO: turning single picture into a slide show
#TODO: Improve aestheics 
#TODO: Make the link redirect to my projects
#TODO: Improve link to search github for projects and grab the readme text and use that to describe each thing I make automatically 





