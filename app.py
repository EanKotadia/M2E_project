from flask import Flask, render_template;
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/logs')
def logs():
    return render_template('logs.html')

@app.route('/about')
def about():
    return render_template('about.html')

# Run the Flask app
if __name__ == '__main__':
    app.run(debug=True)