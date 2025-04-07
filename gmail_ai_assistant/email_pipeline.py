import pyodbc

# Connect to SQL Server
conn = pyodbc.connect(
    r'DRIVER={ODBC Driver 17 for SQL Server};'
    r'SERVER=KOMAL\MSSQL;'
    r'DATABASE=master;'
    r'Trusted_Connection=yes;'
)
cur = conn.cursor()

# Sample email list (replace this with real Gmail API data)
emails = [
    {
        "message_id": "123",
        "thread_id": "abc",
        "in_reply_to": None,
        "sender": "komal@example.com",
        "recipient": "you@example.com",
        "subject": "Test Email",
        "timestamp": 1710000000,
        "body": "This is a test email body for checking summarization and storing in database. It's quite long...",
        "attachments": None
    }
]

# Helper function to truncate/summarize
def summarize_email_body(body, max_length=300):
    if len(body) > max_length:
        return body[:max_length] + "..."
    return body

# Save to DB
for email in emails:
    summary = summarize_email_body(email['body'])

    cur.execute("""
        IF NOT EXISTS (SELECT 1 FROM emails WHERE message_id = ?)
        INSERT INTO emails (message_id, thread_id, in_reply_to, sender, recipient, subject, timestamp, body, attachments)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
    """, (
        email['message_id'],
        email['message_id'],
        email['thread_id'],
        email['in_reply_to'],
        email['sender'],
        email['recipient'],
        email['subject'],
        email['timestamp'],
        summary,  # summarized body
        email['attachments']
    ))
    print(f"✅ Saved: {email['subject']}")

conn.commit()
conn.close()
print("🎉 All emails processed and saved.")
from google_search import google_search

email_body = "What is the capital of Italy?"

if "capital" in email_body.lower():
    results = google_search(email_body)
    for res in results:
        print(f"🔍 {res['title']} - {res['link']}")
        print(f"📄 {res['snippet']}")
from google_search import google_search

def process_email(email):
    query = email.get("body", "")
    if "capital" in query.lower() or "who is" in query.lower():
        results = google_search(query)
        reply = "\n".join([f"{r['title']}\n{r['snippet']}\n{r['link']}" for r in results])
        return reply
    return "No search needed."
dummy_email = {"body": "What is the capital of Italy?"}
print(process_email(dummy_email))
try:
    results = google_search(query)
except Exception as e:
    results = [{"title": "Search failed", "snippet": str(e), "link": ""}]
