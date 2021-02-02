import requests
from bs4 import BeautifulSoup


def main(data, context):
    response = requests.get("https://github.com/users/NekoSarada1101/contributions")
    print(response)
    soup = BeautifulSoup(response.text, "html.parser")

    contributions = []  # type: list
    for tags in soup.find_all("rect"):
        contributions.append(tags.get('data-count'))

    today = contributions[len(contributions) - 1]  # type: str


if __name__ == "__main__":
    main("data", "context")
