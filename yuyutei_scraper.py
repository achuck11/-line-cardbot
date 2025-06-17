
import requests
from bs4 import BeautifulSoup

def search_by_id_or_name(keyword):
    search_url = f"https://yuyu-tei.jp/sell/sell_price.php?name={keyword}"
    headers = {"User-Agent": "Mozilla/5.0"}
    res = requests.get(search_url, headers=headers)
    soup = BeautifulSoup(res.text, "html.parser")

    items = soup.select(".item_box")
    if not items:
        return "找不到相關卡片。"

    result = []
    for item in items[:5]:
        name = item.select_one(".item_name").text.strip()
        price = item.select_one(".sell_price").text.strip()
        result.append(f"{name}: {price}")

    return "\n".join(result)
