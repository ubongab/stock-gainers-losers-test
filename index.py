from flask import Flask, jsonify, render_template
from downloader import Downloader

app = Flask(__name__)

dw = Downloader()


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/api/gainers/<int:count>')
def gainers(count):
    return jsonify({'datetime': dw.date_time, 'results':dw.gainers[:count]})#" <h2> Gainers </h2>"

@app.route('/api/losers/<int:count>')
def losers(count):
    return jsonify({'datetime':dw.date_time,'results':dw.losers[:count]})#" <h2> Losers </h2>"



if __name__ == '__main__':
    app.debug = True
    app.run()