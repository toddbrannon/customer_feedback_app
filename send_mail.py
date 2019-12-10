import smtplib
from email.mime.text import MIMEText
# from send_mail import send_mail

def send_mail(customer, dealer, visit, rating, likelihood, comments):
    port = 2525
    smtp_server = 'smtp.mailtrap.io'
    login = 'd1b8f5f0bd58be'
    password = 'e70afe77d83026'
    message = f"<h3>New Feedback Submission</h3><ul><li>Customer: {customer}</li><li>Dealer: {dealer}</li><li>Nature of visit: {visit}</li><li>Likelihood to recommend: {likelihood}</li><li>Comments: {comments}</li></ul>"

    sender_email = 'email1@example.com'
    receiver_email = 'email2@example.com'
    msg = MIMEText(message, 'html')
    msg['Subject'] = 'Mercedes Benz Feedback'
    msg['From'] = sender_email
    msg['To'] = receiver_email

    # Send email
    with smtplib.SMTP(smtp_server, port) as server:
        server.login(login, password)
        server.sendmail(sender_email, receiver_email, msg.as_string())
