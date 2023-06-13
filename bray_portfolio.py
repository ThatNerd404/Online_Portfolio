from flask import Flask , redirect , url_for , render_template , request , session , flash

app = Flask(__name__)

@app.route('/home')
@app.route('/')
def home():
    return render_template("Home.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)

#TODO: improve website by:
#* TODO: turning single picture into a slide show
#TODO: Improve aestheics (change border colors to the same yellow and add some more stuff to make the home page have more going for it)
#TODO: Make the link redirect to my projects
#TODO: Improve link to search github for projects and grab the readme text and use that to describe each thing I make automatically 
#TODO: Possibly add more pages and a way to go between pages




