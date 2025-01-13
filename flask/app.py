from flask import Flask

# create an instance of the flask class
# which will be your WSGI application
app = Flask(__name__)

@app.route("/")
def welcome():
    return "Welcome to the flask course"

@app.route("/index")
def index():
    return "Welcome to the flask course index page"

if __name__=="__main__":
    app.run(debug=True)
