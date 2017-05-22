from flask import Flask, render_template
app = Flask(__name__)


@app.route('/')
def home():
    return render_template('index.html')


@app.route('/search')
def render():
    return render_template('search_en.html')


if __name__ == '__main__':
    app.run(debug=True)
