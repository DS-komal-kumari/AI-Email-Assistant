# AI Personal Email Assistant 🤖📧

This is a prototype for an AI-powered email assistant developed as part of the internship task at **Wasserstoff**. The assistant reads emails, understands their intent, and generates polite professional replies using a transformer-based language model.

## ✨ Features

- Reads emails from a list (mock inbox)
- Uses HuggingFace's `google/flan-t5-base` to understand and respond to email queries
- Automatically drafts professional replies
- (Optional) Saves all replies into a CSV file for review

## 🔧 Tech Stack

- Python
- HuggingFace Transformers (`flan-t5-base`)
- Jupyter Notebook / Python Script
- Pandas (for saving replies to CSV)

## 🔍 How It Works

1. A list of emails is provided as input.
2. Each email is passed to the language model using a prompt.
3. The model generates a professional reply.
4. The email and its reply are saved to `email_replies.csv`.

## 🚀 Getting Started

### 1. Install dependencies

```bash
pip install transformers pandas
