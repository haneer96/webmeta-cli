import requests
from bs4 import BeautifulSoup
import sys


url = input("Enter URL: ")


if not url.startswith("http"):
    print("⚠️ URL missing http/https, please prepend it")
    sys.exit(1)

try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()
except requests.exceptions.RequestException as e:
    print(f"❌ Failed to fetch URL: {e}")
    sys.exit(1)


soup = BeautifulSoup(response.text, "html.parser")


title = soup.title.string.strip() if soup.title and soup.title.string else "No title"


description_tag = soup.find("meta", {"name": "description"})
description = description_tag["content"].strip() if description_tag and "content" in description_tag.attrs else "No description"


print("=== Webmeta Result ===")
print(f"Title      : {title}")
print(f"Description: {description}")
print("======================")
