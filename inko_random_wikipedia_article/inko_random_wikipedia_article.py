# import json
# import textwrap
# import urllib.request

# API_URL = "https://en.wikipedia.org/api/rest_v1/page/random/summary"

# def main():
#     """
#     Fetches a random Wikipedia article summary and prints it in a readable format.

#     This function makes an HTTP GET request to the specified API URL, which returns
#     a JSON response containing a random Wikipedia article's title and extract. It then
#     extracts these values from the JSON response and prints them in a nicely formatted
#     way using the `textwrap` module.
#     """
#     with urllib.request.urlopen(API_URL) as response:
#         data = json.load(response)

#     print(data["title"], end="\n\n")
#     print(textwrap.fill(data["extract"]))

# # def main():
# #     raise Exception("Boom!")

# if __name__ == "__main__":
#     main()

import httpx
from rich.console import Console
from importlib.metadata import metadata

API_URL = "https://en.wikipedia.org/api/rest_v1/page/random/summary"
USER_AGENT = "{Name}/{Version} (Contact: {Author-email})"

def build_user_agent():
    fields = metadata("inko-random-wikipedia-article")
    return USER_AGENT.format_map(fields)

def main():
    headers = {"User-Agent": USER_AGENT}

    with httpx.Client(headers=headers) as client:
        response = client.get(API_URL, follow_redirects=True)
        response.raise_for_status()
        data = response.json()

    console = Console(width=72, highlight=False)
    console.print(data["title"], style="bold", end="\n\n")
    console.print(data["extract"])