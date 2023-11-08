 
from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///architecture.db'
db = SQLAlchemy(app)

class Architecture(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(80), unique=True, nullable=False)
    description = db.Column(db.Text, nullable=True)

    def __repr__(self):
        return '<Architecture %r>' % self.name

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/types')
def types():
    architectures = Architecture.query.all()
    return render_template('types.html', architectures=architectures)

@app.route('/history')
def history():
    return render_template('history.html')

@app.route('/materials')
def materials():
    return render_template('materials.html')

@app.route('/tools')
def tools():
    return render_template('tools.html')

@app.route('/careers')
def careers():
    return render_template('careers.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # send the email
        return render_template('contact.html', message='Your message has been sent.')
    else:
        return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
