'''
more information : https://developers.google.com/gmail/api/reference/rest
and : https://developers.google.com/gmail/api/quickstart/python
'''
from __future__ import print_function
import os.path
import base64
from googleapiclient.discovery import build
from google_auth_oauthlib.flow import InstalledAppFlow
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials

# If modifying these scopes, delete the file token.json.  
SCOPES = 'https://mail.google.com/'

def getCredentials():
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
    return creds

def payload2fields(txt):
    """
    Transform request GMail API to ready-to-use for todoapp.
    """

    mimeType = txt['payload'].get('mimeType')
    data =''

    #MIME errors management
    if mimeType == "text/plain":
        try:
            data = txt['payload'].get('body')['data']
        except KeyError:
            print("Error in txt['payload'].get('body')['data']")
            exit()
    elif mimeType == "multipart/alternative":
        try:
            data = txt['payload'].get('parts')[0]['body']['data']
        except IndexError:
            print("Error, list index out of range in get('parts')")
            exit()
    else:
        print("bad mimeType, need text/plain or multipart/alternative")
        exit()

    #email subject searching
    for n in range(len(txt['payload'].get('headers'))):
        if txt['payload'].get('headers')[n]['name'] == 'Subject':
            subject = txt['payload'].get('headers')[n]['value']

    #message cleaning and decoding
    task = subject[7:].strip()
    decode = str(base64.urlsafe_b64decode(data))
    cleaned_decode = decode.strip("b'").split("\\r\\n")
    
    #unpack fields
    list = []
    for item in cleaned_decode:
        list += item.split(' : ')

    priority = ""
    label = ""
    desc = ""

    for n in range(len(list)):
        if list[n]=='Priority':
            priority = list[n+1]
        if list[n]=='Label':
            label = list[n+1]
        if list[n]=='Note':
            desc = list[n+1]

    return task, priority, label, desc

def getMail():
    """
    Shows basic usage of the Gmail API. Ready2Use from google. see link at the top
    """
    creds = getCredentials()
    service = build('gmail', 'v1', credentials=creds)

    # catch email from Gmail, with maxResults parameter and , q = 'todo' filter
    result = service.users().messages().list(maxResults=100, userId='me', q='subject:todo').execute()
    messages = result.get('messages')

    #todo : gérer les messages vides
    for msg in messages:
            txt = service.users().messages().get(userId='me', id=msg['id']).execute()
            task,priority,label,desc = payload2fields(txt)

    return task, priority,label, desc

def deleteMail():
    '''
    allows you to delete the added messages to the app in your email box
    '''
    creds = getCredentials()
    service = build('gmail', 'v1', credentials=creds)

    # catch email from Gmail, with maxResults parameter and , q = 'todo' filter
    result = service.users().messages().list(maxResults=100, userId='me', q='subject:todo').execute()
    messages = result.get('messages')

    for msg in messages:
        service.users().messages().delete(userId='me',id=msg['id']).execute()

if __name__ == '__main__':
    getMail()