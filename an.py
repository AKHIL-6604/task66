import pandas as pd
import smtplib
from email.mime.text import MIMEText
from email.mime.multipart import MIMEMultipart'
def read_excel(file_path):
    df = pd.read_excel(file_path)
    return df

# Count the number of absences per student in a specific subject
def count_absences(df, subject, limit=3):
    subject_df = df[df['Subject'] == subject]  # Filter data for the subject
    absent_students = subject_df[subject_df['Attendance'] == 'Absent']  # Filter absences
    return absent_students

# Send email to a student
def send_email_to_student(student_email, absences_count, subject, total_classes, smtp_server, smtp_port, sender_email, sender_password):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = student_email
        msg['Subject'] = f"Attendance Alert: {subject}"

        body = f"Dear Student,\n\nYou have missed {absences_count} out of {total_classes} classes for the subject: {subject}. Please be aware that you are reaching your absence limit.\n\nBest regards,\nYour School."
        msg.attach(MIMEText(body, 'plain'))

        # Set up SMTP server and send email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            text = msg.as_string()
            server.sendmail(sender_email, student_email, text)
            print(f"Email sent to {student_email}")
    except Exception as e:
        print(f"Error sending email to {student_email}: {e}")

# Send email to staff
def send_email_to_staff(staff_email, student_name, student_email, absences_count, subject, smtp_server, smtp_port, sender_email, sender_password):
    try:
        msg = MIMEMultipart()
        msg['From'] = sender_email
        msg['To'] = staff_email
        msg['Subject'] = f"Attendance Alert for {student_name}"

        body = f"Dear Staff,\n\nThe student {student_name} ({student_email}) has reached {absences_count} absences in the subject: {subject}. Please take the necessary actions.\n\nBest regards,\nAttendance System"
        msg.attach(MIMEText(body, 'plain'))

        # Set up SMTP server and send email
        with smtplib.SMTP(smtp_server, smtp_port) as server:
            server.starttls()
            server.login(sender_email, sender_password)
            text = msg.as_string()
            server.sendmail(sender_email, staff_email, text)
            print(f"Email sent to {staff_email}")
    except Exception as e:
        print(f"Error sending email to staff: {e}")

# Main function to process data
def main(file_path, subject, limit=3, smtp_server="smtp.gmail.com", smtp_port=587, sender_email="your_email@gmail.com", sender_password="your_password"):
    df = read_excel(file_path)

    # Get total classes from the subject data
    total_classes = df[df['Subject'] == subject].shape[0]  # Number of rows for the subject

    # Get the list of students with absences in the subject
    absent_students = count_absences(df, subject, limit)

    # Notify students and staff
    for index, row in absent_students.iterrows():
        student_email = row['Email']
        student_name = row['Student Name']
        absences_count = row['Attendance'].count('Absent')

        # Notify student if they reach the limit
        if absences_count >= limit:
            send_email_to_student(student_email, absences_count, subject, total_classes, smtp_server, smtp_port, sender_email, sender_password)

            # Notify staff if a student reaches the limit
            staff_email = "staff_email@example.com"  # Replace with actual staff email
            send_email_to_staff(staff_email, student_name, student_email, absences_count, subject, smtp_server, smtp_port, sender_email, sender_password)

# Example usage
if __name__ == "__main__":
    file_path = "ak.xlsx"  # Excel file containing attendance data
    subject = "java"  # The subject to check absences for
    main(file_path, subject)
