from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def main():
    return render_template('main.html')


app.run(port=8080, host='127.0.0.1')
