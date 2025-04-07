# from gmail_reader import fetch_emails
# from summarizer import summarize_email

# emails = fetch_emails()
# for i, mail in enumerate(emails):
#     print(f"\n📩 Email #{i+1}")
#     summary = summarize_email(mail)
#     print("📝 Summary:", summary)

from gmail_reader import fetch_emails
from email_summarizer import summarize as summarize_email

def main():
    emails = fetch_emails()
    for email in emails:
        summary = summarize_email(email['body'])
        print("Subject:", email['subject'])
        print("Summary:", summary)

if __name__ == "__main__":
    main()

from gmail_reader import fetch_emails
from email_summarizer import summarize as summarize_email  # ← this line updated

emails = fetch_emails()
for i, mail in enumerate(emails):
    print(f"\n📩 Email #{i+1}")
    summary = summarize_email(mail)
    print("📝 Summary:", summary)


