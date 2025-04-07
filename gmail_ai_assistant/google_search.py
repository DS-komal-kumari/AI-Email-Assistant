import requests

API_KEY = "AIzaSyBLb4-Dqhm2mwt0bMm6mnp2OCoRGreUcUA"
CSE_ID = "234b0f9342f724c6a"

def google_search(query, num_results=3):
    """Perform a Google Custom Search and return top results."""
    url = "https://www.googleapis.com/customsearch/v1"
    params = {
        "key": API_KEY,
        "cx":  CSE_ID,
        "q":   query,
        "num": num_results
    }
    response = requests.get(url, params=params)
    response.raise_for_status()
    data = response.json()

    results = []
    for item in data.get("items", [])[:num_results]:
        results.append({
            "title":   item["title"],
            "snippet": item["snippet"],
            "link":    item["link"]
        })
    return results