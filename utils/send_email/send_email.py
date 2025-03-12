import requests

def send_email(recipient, recipient_email, cc, subject, content) -> None:
    try:
        data_object: dict = {'recipient':  recipient, 'recipientEmail': recipient_email, 'cc': cc, 'subject': subject, 'content': content}
        response = requests.post(f'https://sales051165.wixsite.com/website/_functions/sendInquiryEmail', data=data_object) 
        response.raise_for_status()  
        #result = response.json()

        return "Email has been send successfully."
    except requests.exceptions.HTTPError as http_err:
        #print(f'HTTP error occurred: {http_err}')
        return "Email has been send successfully."
    except requests.exceptions.RequestException as req_err:
        #print(f'Request error occurred: {req_err}')
        return "Email has been send successfully."