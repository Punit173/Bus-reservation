from flask import  Flask , render_template , request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Integer, String
from sqlalchemy.orm import Mapped, mapped_column
from sqlalchemy.orm import DeclarativeBase
from datetime import datetime
from flask_mail import Mail
import smtplib

app = Flask(__name__,template_folder='image')
app.config["SQLALCHEMY_DATABASE_URI"] = 'mysql://root:@localhost/bus reservation'

class Base(DeclarativeBase):
  pass
db = SQLAlchemy(model_class=Base)
db.init_app(app)


class Contacts(db.Model):
    sno: Mapped[int] = mapped_column(Integer, primary_key=True)
    name: Mapped[str] = mapped_column(String,  nullable=False)
    email: Mapped[str] = mapped_column(String,  nullable=False)
    phone: Mapped[int] = mapped_column(Integer,  nullable=False)
    msg: Mapped[str] = mapped_column(String,  nullable=False)
    date: Mapped[str] = mapped_column(String, nullable=True)

class Tickets(db.Model):
    sno: Mapped[int] = mapped_column(Integer, primary_key=True)
    aadhaar: Mapped[str] = mapped_column(String,  nullable=False)
    Name: Mapped[str] = mapped_column(String,  nullable=False)
    Contact_no: Mapped[str] = mapped_column(String,  nullable=False)
    Board_place: Mapped[str] = mapped_column(String,  nullable=False)
    Destination: Mapped[str] = mapped_column(String,  nullable=False)
    Date: Mapped[str] = mapped_column(String, nullable=True)

class Payment(db.Model):
    card_no: Mapped[int] = mapped_column(Integer, primary_key=True)
    exp: Mapped[str] = mapped_column(String,  nullable=False)
    cvv: Mapped[str] = mapped_column(String,  nullable=False)
    name: Mapped[str] = mapped_column(String,  nullable=False)
    date: Mapped[str] = mapped_column(String, nullable=True)


@app.route("/")
def hello():
    return render_template("15-10-2023.htm")

@app.route("/tickets", methods = ['GET','POST'])
def tickets():
    if(request.method=='POST'):
        aadh=request.form.get('tel')
        Name=request.form.get('passenger_name')
        cont=request.form.get('telephone')
        board=request.form.get('board_place')
        dest=request.form.get('Your_destination')
        entry = Tickets(aadhaar=aadh,Name=Name,Contact_no=cont,Board_place=board,Destination=dest,Date=datetime.now())
        db.session.add(entry)
        db.session.commit()



        message1=f"""Subject: Booking Confirmation and Payment Details - EFare Bus Booking

                    Dear {Name},

                    Thank you for choosing EFare Bus Booking for your upcoming journey from {board} to {dest}. We are delighted to confirm your ticket reservation, and we appreciate the opportunity to serve you.

                    Booking Details:
                    - Departure City: {board}
                    - Destination City: {dest}
                    - Bus Service: Multani Sona / TN 09 CVXY 1425

                    Passenger Details:
                    - Passenger Name: {Name}
                    - Email Address: {cont}

                    Payment Details:
                    We would like to inform you that the payment for your ticket has been successfully processed. Below are the payment details:

                    - Transaction ID: TTCNI022000800594
                    - Payment Amount: Rs 1569
                    - Payment Method: Card

                    Please keep this email for your records, as it serves as confirmation of your booking and payment. In case you have any questions or concerns regarding your reservation, feel free to contact our customer support team at [Customer Support Email/Phone Number].

                    We wish you a pleasant and comfortable journey with EFare Bus Booking. Thank you for trusting us with your travel needs.

                    Safe travels!

                    Best regards,

                    Customer Service Team
                    EFare Bus Booking
                    projectbusportal@gmail.com"""

        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login("punitking748@gmail.com","rhyp gkgc azro ewlj")
        server.sendmail("punitking748@gmail.com", cont, message1)


    return render_template("30-10-2023.htm")

@app.route("/payment", methods = ['GET','POST'])
def payment():
    if(request.method=='POST'):
        card_no=request.form.get('cardNumber')
        exp=request.form.get('expiryDate')
        cvv=request.form.get('cvv')
        name=request.form.get('cardHolder')
        entry = Payment(card_no=card_no,exp=exp,cvv=cvv,name=name,date=datetime.now())
        db.session.add(entry)
        db.session.commit()

    return render_template("payment.htm")

@app.route("/payment_success")
def payment_success():
    return render_template("payment_success.htm")

@app.route("/contact", methods = ['GET','POST'])
def Contact():
    if(request.method=='POST'):
        name=request.form.get('name')
        email=request.form.get('email')
        phone=request.form.get('phone')
        msg=request.form.get('msg')

        entry = Contacts(name=name,email=email,phone=phone,msg=msg,date=datetime.now())
        db.session.add(entry)
        db.session.commit()
        message=f""" 
                Subject: Your Recent Bus Booking Inquiry

                Dear {name},

                I hope this email finds you well. My name is Punit, and I am reaching out to you in response to your recent inquiry on our bus booking website. We appreciate your interest in our services and are delighted to assist you with your travel plans.

                We understand that planning a journey can be a meticulous task, and we are here to make the process as smooth as possible for you. To better assist you, could you please provide us with some additional details regarding your travel requirements? This information will help us tailor our services to meet your specific needs:

                1. Travel Date and Time: When are you planning to embark on your journey, and at what time?
                2. Departure and Arrival Locations: Which cities or towns do you plan to travel from and to?
                3. Preferred Amenities: Are there any specific amenities or features you are looking for in a bus service?
                4. Budget Constraints: Do you have any budget constraints or preferences for the type of bus service you are interested in?

                Once we have these details, we can present you with the best available options that align with your preferences. Our goal is to ensure that you have a comfortable and enjoyable travel experience.

                Feel free to reply to this email with the required information, or if you prefer, you can contact our customer support team at 97564-55141 for immediate assistance. We are committed to providing you with top-notch service and making your journey a memorable one.

                Thank you for choosing EFare Bus Booking for your travel needs. We look forward to serving you and making your upcoming journey a pleasant and stress-free experience.

                Safe travels!

                Best regards,

                Punit
                EFare Bus Booking 
                projectbusportal@gmail.com
                """
        server = smtplib.SMTP("smtp.gmail.com",587)
        server.starttls()
        server.login("punitking748@gmail.com","rhyp gkgc azro ewlj")
        server.sendmail("punitking748@gmail.com",email,message)
        
    return render_template("21-10-2023.htm")

@app.route("/about")
def about():
    return render_template("29-10-2023.htm")

app.run(debug=True)