from transformers import pipeline

summarizer = pipeline("summarization", model="t5-small", tokenizer="t5-small")

def summarize_email(content):
    return summarizer("summarize: " + content, max_length=100, min_length=20, do_sample=False)[0]['summary_text']
