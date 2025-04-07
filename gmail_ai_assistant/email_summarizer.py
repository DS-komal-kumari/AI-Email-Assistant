from transformers import pipeline

# Use only PyTorch backend
summarizer = pipeline("summarization", model="google/flan-t5-base", framework="pt")

email = """
Hi Komal,

Just a reminder that our team meeting is scheduled for Friday at 2 PM. We’ll be discussing the Q2 goals and reviewing the project timelines. Please bring the updated task list and timelines with you.

Thanks,
Manager
"""

summary = summarizer(email, max_length=60, min_length=10, do_sample=False)
print("Summary:", summary[0]['summary_text'])


def summarize(text):
    # summarization logic
    return summary
