import os

import wtforms
from flask import Flask, url_for, render_template, request, redirect
from flask_mail import Mail, Message
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, IntegerField, EmailField, TextAreaField
from wtforms.validators import DataRequired
import psycopg2
from data.image_data import photos

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = os.environ.get("DATABASE_URL1", "sqlite:///data/rsvps.db")
app.config['MAIL_SERVER'] = 'smtp.gmail.com'
app.config['MAIL_PORT'] = 465
app.config['MAIL_USERNAME'] = os.environ.get("EMAIL")
app.config['MAIL_PASSWORD'] = os.environ.get("PASSWORD")
app.config['MAIL_USE_TLS'] = False
app.config['MAIL_USE_SSL'] = True
app.secret_key = "os.environ.get('SECRET_KEY')"
db = SQLAlchemy(app)
pictures = photos


class RSVP(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    num_guests = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f"{self.name}"


class RSVPForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()], render_kw={"placeholder": "NAME"})
    num_guests = IntegerField('num_of_guests', validators=[DataRequired()],
                              render_kw={"placeholder": "NUMBER OF GUESTS"})


class ContactForm(FlaskForm):
    name = StringField('name', validators=[DataRequired()], render_kw={"placeholder": "NAME"})
    email = EmailField('email', validators=[DataRequired()], render_kw={"placeholder": "Email"})
    message = TextAreaField('message', validators=[DataRequired()], render_kw={"placeholder": "Enter Message"})


db.create_all()
guests = db.session.query(RSVP).all()


@app.route("/", methods=["GET", "POST"])
def index():
    return render_template('index.html')


@app.route("/add", methods=["GET", "POST"])
def add():
    global guests
    if request.method == "POST":
        new_rsvp = RSVP(
            name=request.form["name"],
            num_guests=request.form["num_guests"]
        )
        try:
            db.session.add(new_rsvp)
            db.session.commit()
            guests = db.session.query(RSVP).all()
        except:
            pass
        print(guests)
        return redirect(url_for('rsvp'))

    return render_template('rsvp.html', rsvps=guests)


@app.route("/send", methods=["GET", "POST"])
def send():
    if request.method == "POST":
        mail = Mail(app)
        msg = Message("Message From Wedding Site", sender=f"Wedding Site: {request.form['name']} "
                      , recipients=["dmobley0608@gmail.com"])
        msg.body = f'Email: {request.form["email"]}\n\n{request.form["message"]}'
        mail.send(msg)
        return redirect('contact')
    return render_template('index.html')


@app.route("/photos")
def photos():
    return render_template(f'photos.html', images=pictures)


@app.route("/contact")
def contact():
    form = ContactForm()
    if form.validate_on_submit():
        return redirect('index')
    return render_template('contact.html', form=form)


@app.route("/rsvp")
def rsvp():
    global guests
    guests = db.session.query(RSVP).all()
    form = RSVPForm()
    if form.validate_on_submit():
        return redirect(url_for('rsvp'))
    return render_template('rsvp.html', rsvps=guests, form=form)


if __name__ == "__main__":
    app.run(debug=True)
