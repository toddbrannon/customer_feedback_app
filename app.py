from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from send_mail import send_mail

app = Flask(__name__)

ENV = 'prod'

if ENV == 'prod':
    app.debug = True
    app.config['SQLALCHEMY_DATABASE_URI'] = ''
else:
    app.debug = False
    app.config['SQLALCHEMY_DATABASE_URI'] = ''

app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)

class Feedback(db.Model):
    __tablename__ = 'feedback'
    id = db.Column(db.Integer, primary_key=True)
    customer = db.Column(db.String(200))
    dealer = db.Column(db.String(200))
    visit = db.Column(db.String(200))
    rating = db.Column(db.Integer)
    likelihood = db.Column(db.Integer)
    comments = db.Column(db.Text())

    def __init__(self, customer, dealer, visit, rating, likelihood, comments):
        self.customer = customer
        self.dealer = dealer
        self.visit = visit
        self.rating = rating
        self.likelihood = likelihood
        self.comments = comments

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/submit', methods=['POST'])
def submit():
    if request.method == 'POST':
        customer = request.form['customer']
        dealer = request.form['dealer']
        visit =  request.form['visit']
        rating = request.form['rating']
        likelihood = request.form['likelihood']
        comments = request.form['comments']
        # print(customer, dealer, rating, comments)
        if customer == '' or dealer == '':
            return render_template('index.html', message='Please complete all fields')
        if db.session.query(Feedback).filter(Feedback.customer == customer).count() == 0:
            data = Feedback(customer, dealer, visit, rating, likelihood, comments)
            db.session.add(data)
            db.session.commit()
            send_mail(customer, dealer, visit, rating, likelihood, comments)
            return render_template('success.html')
        return render_template('index.html', message='You have already submitted feedback')

if __name__ == '__main__':
    app.run()   

