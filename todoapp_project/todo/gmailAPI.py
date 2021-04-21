from __future__ import print_function
import os.path
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
import pickle
import os.path
import base64
import email
from bs4 import BeautifulSoup
from googleapiclient.http import MediaInMemoryUpload

# If modifying these scopes, delete the file token.json.
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def payload2fields(txt):
    """Transform request GMail API to ready-to-use for todoapp.
    """
    mimeType = txt['payload'].get('mimeType')
    data =''

    if mimeType == "text/plain":
        try:
            data = txt['payload'].get('body')['data']
        except KeyError:
            print("Error in txt['payload'].get('body')['data'] line 23")
            exit()

    elif mimeType == "multipart/alternative":
        try:
            data = txt['payload'].get('parts')[0]['body']['dataa']
        except IndexError:
            print("Error, list index out of range in get('parts')")
            exit()

    else:
        print("bad mimeType, need text/plain or multipart/alternative")
        exit()

    try: 
        subject = txt['payload'].get('headers')[6]['value']
    except IndexError:
            print("Error, list index out of range in get('headers')")
            exit()

    task = subject[7:].strip()
    decode = str(base64.urlsafe_b64decode(data))
    cleaned_decode = decode.strip("b'").split("\\r\\n")
    
    list = []
    for item in cleaned_decode:
        list += item.split(' : ')

    try:
        priority = list[1]
        label = list[3]
        desc = list[5]
        #effacer email

        return task, priority, label, desc
    except IndexError:
        print("Error, list index out of range in priority, label, or desc")

def main():
    """Shows basic usage of the Gmail API.
    Lists the user's Gmail labels.
    """
    creds = None
    # The file token.json stores the user's access and refresh tokens, and is
    # created automatically when the authorization flow completes for the first
    # time.
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)
    # If there are no (valid) credentials available, let the user log in.
    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)
        # Save the credentials for the next run
        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    service = build('gmail', 'v1', credentials=creds)

    # Call the Gmail API
    results = service.users().labels().list(userId='me').execute()
    labels = results.get('labels', [])

    if not labels:
        print('No labels found.')
    else:
        print('Labels:')
        for label in labels:
            print(label['name'])
    

    # catch email from Gmail, with maxResults parameter and , q = 'to do' filter
    result = service.users().messages().list(maxResults=100, userId='me', q='subject:todo').execute()
    messages = result.get('messages')

    for msg in messages:

            txt = service.users().messages().get(userId='me', id=msg['id']).execute()
            task,priority,label,desc = payload2fields(txt)
            print(f'tache : {task}, prio : {priority},label : {label}, note: {desc}')


if __name__ == '__main__':
    main()