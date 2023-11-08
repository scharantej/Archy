 
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

@app.route('/types_of_architecture')
def types_of_architecture():
    architectures = Architecture.query.all()
    return render_template('types_of_architecture.html', architectures=architectures)

@app.route('/history_of_architecture')
def history_of_architecture():
    return render_template('history_of_architecture.html')

@app.route('/materials_of_architecture')
def materials_of_architecture():
    return render_template('materials_of_architecture.html')

@app.route('/tools_of_architecture')
def tools_of_architecture():
    return render_template('tools_of_architecture.html')

@app.route('/careers_in_architecture')
def careers_in_architecture():
    return render_template('careers_in_architecture.html')

@app.route('/contact', methods=['GET', 'POST'])
def contact():
    if request.method == 'POST':
        name = request.form['name']
        email = request.form['email']
        message = request.form['message']
        # Send the email
        return render_template('contact.html', message='Your message has been sent.')
    else:
        return render_template('contact.html')

if __name__ == '__main__':
    app.run(debug=True)
