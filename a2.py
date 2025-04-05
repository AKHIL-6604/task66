import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# Use your Gmail address and the App Password (generated from Google account settings)
from_id = 'chintudaida5@gmail.com'        # Replace with your Gmail address
pwd = 'your_app_password'               # Replace with your generated app password

def mailstu(li, msg):
    try:
        # Set up the SMTP server and login
        s = smtplib.SMTP('smtp.gmail.com', 587, timeout=120)
        s.starttls()  # Secure the connection using TLS
        s.login(from_id, pwd)  # Login with your email and app password
        
        # Sending the email to each student in the list
        for to_id in li:
            message = MIMEMultipart()
            message['Subject'] = 'Attendance report'
            message.attach(MIMEText(msg, 'plain'))  # Email body content
            content = message.as_string()
            s.sendmail(from_id, to_id, content)  # Send the email
        
        print("Mail sent to students")
        s.quit()  # Close the connection after sending the emails
    except Exception as e:
        print(f"Error sending email: {e}")

# Sample usage
students_emails = ['student1@example.com', 'student2@example.com']  # List of student emails
message = "You have an attendance warning!"  # Example message
mailstu(students_emails, message)
