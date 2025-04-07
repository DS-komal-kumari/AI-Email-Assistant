import pyodbc
import json
import time

# Dummy email fetcher — replace with real Gmail API logic
def get_emails():
    return [
        {
            "message_id": "abc123",
            "thread_id": "thread_001",
            "in_reply_to": None,
            "sender": "example@gmail.com",
            "recipient": "you@gmail.com",
            "subject": "Test Email",
            "timestamp": int(time.time()),
            "body": "Hello from your assistant!",
            "attachments": []
        }
    ]

# Step 1: Connect to SQL Server
conn = pyodbc.connect(
    r'DRIVER={ODBC Driver 17 for SQL Server};'
    r'SERVER=KOMAL\MSSQL;'  # Your server name
    r'DATABASE=master;'     # Change to your DB name if different
    r'Trusted_Connection=yes;'
)
print("✅ Connected to SQL Server")

# Step 2: Create cursor
cur = conn.cursor()

# Step 3: Create table if not exists
cur.execute("""
IF NOT EXISTS (
    SELECT * FROM sysobjects WHERE name='emails' AND xtype='U'
)
CREATE TABLE emails (
    message_id NVARCHAR(255) PRIMARY KEY,
    thread_id NVARCHAR(255),
    in_reply_to NVARCHAR(255),
    sender NVARCHAR(MAX),
    recipient NVARCHAR(MAX),
    subject NVARCHAR(MAX),
    timestamp BIGINT,
    body NVARCHAR(MAX),
    attachments NVARCHAR(MAX)
)
""")
conn.commit()
print("📩 Table created or already exists.")


# Step 4: Fetch and store emails
def fetch_and_store_emails():
    emails = get_emails()
    for email_data in emails:
        try:
            cur.execute("""
                IF NOT EXISTS (SELECT 1 FROM emails WHERE message_id = ?)
                INSERT INTO emails (message_id, in_reply_to, thread_id, sender, recipient, subject, timestamp, body, attachments)
                VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?)
            """, (
                email_data["message_id"],
                email_data["message_id"],
                email_data["in_reply_to"],
                email_data["thread_id"],
                email_data["sender"],
                email_data["recipient"],
                email_data["subject"],
                email_data["timestamp"],
                email_data["body"],
                json.dumps(email_data["attachments"])
            ))
            print(f"📥 Email saved: {email_data['subject']}")
        except Exception as e:
            print(f"⚠️ Error saving email {email_data['message_id']}: {e}")

    conn.commit()
    print("✅ All emails processed and stored.")


# Run the pipeline
fetch_and_store_emails()

# Step 5: Close connection
conn.close()
