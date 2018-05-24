from flask import Flask, render_template, request
from webbrowser import open_new_tab
from modules.read_csv import find_best, create_template
app = Flask(__name__)
ind = 0


@app.route("/", methods = ['GET','POST'])
def start():
    return render_template('greet.html')

@app.route("/result", methods = ['GET','POST'])
def take_data():
    global ind
    ind += 1
    town = request.form['town']
    country = request.form['country']
    radius = request.form['radius']
    if not radius.strip():
        radius = 0
    else:
        radius = float(radius)
    address = "{0}, {1}".format(town, country)
    result = create_template(find_best(address, radius), ind)
    return render_template('map{}.html'.format(ind), result=result)


if __name__ == "__main__":
    open_new_tab('http://localhost:5000')
    app.run(port=5000)

