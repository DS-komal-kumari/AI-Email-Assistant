import os.path
import base64
import re
from google.auth.transport.requests import Request
from google.oauth2.credentials import Credentials
from google_auth_oauthlib.flow import InstalledAppFlow
from googleapiclient.discovery import build

# SCOPES - Read-only access to Gmail
SCOPES = ['https://www.googleapis.com/auth/gmail.readonly']

def get_gmail_service():
    creds = None
    if os.path.exists('token.json'):
        creds = Credentials.from_authorized_user_file('token.json', SCOPES)

    if not creds or not creds.valid:
        if creds and creds.expired and creds.refresh_token:
            creds.refresh(Request())
        else:
            flow = InstalledAppFlow.from_client_secrets_file(
                'credentials.json', SCOPES)
            creds = flow.run_local_server(port=0)

        with open('token.json', 'w') as token:
            token.write(creds.to_json())

    return build('gmail', 'v1', credentials=creds)

def fetch_emails():
    service = get_gmail_service()
    results = service.users().messages().list(userId='me', maxResults=5).execute()
    messages = results.get('messages', [])

    emails = []  # 🟢 List to collect email info

    for msg in messages:
        txt = service.users().messages().get(userId='me', id=msg['id']).execute()
        payload = txt['payload']
        headers = payload['headers']

        subject = next((h['value'] for h in headers if h['name'] == 'Subject'), "No Subject")
        sender = next((h['value'] for h in headers if h['name'] == 'From'), "Unknown Sender")

        # Decode email body (if available)
        parts = payload.get('parts', [])
        body = ""
        for part in parts:
            if part['mimeType'] == 'text/plain':
                data = part['body'].get('data')
                if data:
                    body = base64.urlsafe_b64decode(data).decode("utf-8")
                    break

        emails.append({
            'from': sender,
            'subject': subject,
            'body': body
        })

    return emails  # 🟢 Now it returns the list

if __name__ == '__main__':
    # fetched = fetch_emails()
    # for email in fetched:
    #     print("\n📩 Email")
    #     print("From:", email['from'])
    #     print("Subject:", email['subject'])
    #     print("Body:", email['body'][:200])  # Print first 200 chars only
    #     print("-" * 50)
    emails = fetch_emails()
for i, mail in enumerate(emails):
    print(f"\n📩 Email #{i+1}")
    summary = summarize_email(mail)
    summary_text = summary[0]['summary_text'] if summary else "No summary available."
    print("📝 Summary:", summary_text)
