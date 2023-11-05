from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def helloWorld():
    return render_template('index.htm')

@app.route('/')
def predict():
    pass

if __name__ == '__main__':
    app.run(debug=True)