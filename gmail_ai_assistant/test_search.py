from google_search import google_search

if __name__ == '__main__':
    for r in google_search("What is the capital of Italy?"):
        print(r["title"], "\n", r["snippet"], "\n", r["link"], "\n")
