import os
from sendgrid import SendGridAPIClient
from sendgrid.helpers.mail import Mail

message = Mail(
    from_email='lidia.szewczyk@gmail.com',
    to_emails='lidia.szewczyk@gmail.com',
    subject='nowa wiadomość',
    html_content='<strong>napisz co chcesz</strong>'
)

sg = SendGridAPIClient('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')
response = sg.send(message)
print(response.status_code, response.body, response.headers)
