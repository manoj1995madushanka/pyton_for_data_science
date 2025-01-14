from flask import Flask, render_template, request, redirect, url_for

# create an instance of the flask class
# which will be your WSGI application
app = Flask(__name__)


@app.route("/")
def welcome():
    return "<html><H1>Welcome to the flask course</H1></html>"


@app.route("/indexold")
def indexOld():
    return render_template('index.html')


@app.route("/index", methods=['GET'])
def index():
    return render_template('index.html')


@app.route("/form", methods=['GET', 'POST'])
def form():
    if request.method == 'POST':
        name = request.form['name']
        return f'Hello {name}'
    return render_template('form.html')


# Variable rule example
@app.route("/success/<int:score>")
def success(score):
    res = ""
    if score > 50:
        res = "PASS"
    else:
        res = "FAIL"
    return render_template('result.html', results=res)
    # return "The marks you got is " + str(score)


@app.route("/successres/<int:score>")
def successres(score):
    res = ""
    if score > 50:
        res = "PASS"
    else:
        res = "FAIL"
    exp = {'score': score, "res": res}
    return render_template('resultres.html', results=exp)


@app.route("/submitmarks", methods=['GET', 'POST'])
def submitmarks():
    total_score = 0
    if request.method == 'POST':
        science = float(request.form['science'])
        maths = float(request.form['maths'])
        c = float(request.form['c'])
        datascience = float(request.form['datascience'])

        total_score = (science + maths + c + datascience) / 4
    return redirect(url_for('success', score=total_score))


if __name__ == "__main__":
    app.run(debug=True)
