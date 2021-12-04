from flask import Flask
from flask import render_template
from flask import jsonify
import scrap

app = Flask(__name__)


@app.route('/')
def index():
    return '<h1>Index Page!</h1>'


@app.route('/automobile.tn/<string:keywords>')
def automobile(keywords):
    k = ''.join(keywords)
    print(f'the keywords are: {k}')
    l = k.split('+')
    print(f'the keywords list is: {l}')

    # a default route response should be implemented for automobile.tn/
    # the scrap.automobile_search(l) should be async it takes too long
    # the fetching should be slower to allow images sources to load and get fetched
    # scrap should be a class

    return jsonify(scrap.automobile_search(l))


@app.route('/affare.tn/<string:keywords>')
def affare(keywords):
    return f'affare.tn {keywords}'


@app.route('/baniola.tn/<string:keywords>')
def baniola(keywords):
    return f'baniola.tn {keywords}'


@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)


if __name__ == "__main__":
    app.run()