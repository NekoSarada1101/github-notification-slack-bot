import json
import requests
from bs4 import BeautifulSoup
from settings import *


def main(data, context):
    response = requests.get("https://github.com/users/NekoSarada1101/contributions")
    print(response)
    print(response.text)
    soup = BeautifulSoup(response.text, "html.parser")

    contributions = []  # type: list
    for tags in soup.find_all("rect"):
        contributions.append(tags.get('data-count'))
    print(contributions)

    today = contributions[len(contributions) - 1]  # type: str
    print("today=" + today)

    if today == "0":
        text = "<@" + SLACK_USER_ID + "> まだGitHubの芝が生えてません！"  # type: str
        data = {"text": text}  # type: dict
        print("data=" + str(data))
        payload = json.dumps(data).encode("utf-8")
        response = requests.post(SLACK_WEBHOOK_URL, payload)
        print(response)


if __name__ == "__main__":
    main("data", "context")
