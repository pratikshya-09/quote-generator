
import requests

def get_random_quote():
 response=requests.get("https://api.quotable.io/random")

 if response.status_code == 200:
    data = response.json()
    return data['content'], data['author']
 else:
    return "Failed to retrieve quote", "Unknown"
 

quote, author=get_random_quote()
print(f'"{quote}"-"{author}"')



