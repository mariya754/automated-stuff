import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.image import MIMEImage
import os
from secret import email_mpi as my_email, email_mpi_p as app_specific_password, email_rec as receiver



# SMTP Server and port no for GMAIL.com
gmail_server = "smtp.gmail.com"
gmail_port = 587

try:
    # Starting connection
    my_server = smtplib.SMTP(gmail_server, gmail_port)
    my_server.ehlo()
    my_server.starttls()

    # Debug: Print email and masked password
    print(f"Email: {my_email}")
    print(f"Password: {'*' * len(app_specific_password)}")

    # Login with your email and app-specific password
    my_server.login(my_email, app_specific_password)
    print("Login successful")


    # Create the email
    body="hopefully that works\n"
    msg = MIMEMultipart()
    msg['From'] = my_email
    msg['To'] = receiver
    msg['Subject'] = "test"

    # define your location
    grade_card_path = '/Users/masha/Desktop/python/chlen.jpeg'
    # Read the image from location
    grade_card_img = open(grade_card_path, 'rb').read()


    msg.attach(MIMEText(body, 'plain'))
    msg.attach(MIMEImage(grade_card_img, name=os.path.basename(grade_card_path)))

    # Send the email
    my_server.send_message(msg)
    print("Email sent successfully")

except Exception as e:
    print(f"An error occurred: {e}")

finally:
    # Close the server connection
    my_server.quit()
