import requests
from bs4 import BeautifulSoup
import csv
import json
import re

URL = "https://ich.unesco.org/en/state/armenia-AM"
BASE = "https://ich.unesco.org"


def scrape_unesco():

    response = requests.get(URL)
    soup = BeautifulSoup(response.text, "html.parser")

    data = []

    for link in soup.find_all("a", href=True):

        href = link["href"]

        if "/en/RL/" in href or "/en/USL/" in href:

            text = link.parent.get_text(strip=True)

            title = link.text.strip()

            full_url = BASE + href

            year_match = re.search(r"(\d{4})", text)
            year = year_match.group(1) if year_match else ""

            list_match = re.search(r"\((.*?)\)", text)
            list_type = list_match.group(1) if list_match else ""

            id_match = re.search(r"(\d{5})$", href)
            element_id = id_match.group(1) if id_match else ""

            data.append({
                "element_id": element_id,
                "title": title,
                "year": year,
                "list_type": list_type,
                "url": full_url,
                "source_page": URL
            })

    return data


def save_csv(data):

    with open("armenia_unesco.csv", "w", newline="", encoding="utf-8") as f:

        writer = csv.DictWriter(
            f,
            fieldnames=[
                "element_id",
                "title",
                "year",
                "list_type",
                "url",
                "source_page"
            ]
        )

        writer.writeheader()
        writer.writerows(data)


def save_json(data):

    with open("armenia_unesco.json", "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4, ensure_ascii=False)


def main():

    data = scrape_unesco()

    save_csv(data)
    save_json(data)

    print("Elements collected:", len(data))
    print("Files created:")
    print(" - armenia_unesco.csv")
    print(" - armenia_unesco.json")


if __name__ == "__main__":
    main()
