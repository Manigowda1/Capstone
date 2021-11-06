import requests
from bs4 import BeautifulSoup

Products_to_track = [
    {
        "prod_URL": "https://www.amazon.in/OnePlus-Nord-Blue-128GB-Storage/dp/B097RD2JX8/ref=sr_1_1?dchild=1&pf_rd_i=1389401031&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_p=006764d9-6108-4b9a-b176-91bab4120f70&pf_rd_r=Y8988MGSV6C0YM02N8WP&pf_rd_s=merchandised-search-3&qid=1630825546&refinements=p_89%3AOnePlus&rnid=3837712031&s=electronics&sr=1-1",
        "name": "Nord 2",
        "target_price": 29000
    },
    {
        "prod_URL": "https://www.amazon.in/Redmi-9A-2GB-32GB-Storage/dp/B08696XB4B/ref=sr_1_2?dchild=1&pf_rd_i=1389401031&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_p=006764d9-6108-4b9a-b176-91bab4120f70&pf_rd_r=Y8988MGSV6C0YM02N8WP&pf_rd_s=merchandised-search-3&qid=1630828917&refinements=p_89%3AOnePlus%7CRedmi&rnid=3837712031&s=electronics&sr=1-2",
        "name": "Redmi9A",
        "target_price": 7000
    },
    {
        "prod_URL": "https://www.amazon.in/NOKIA-105-2019-Dual-Black/dp/B07WXW8V4X/ref=sr_1_1?dchild=1&pf_rd_i=1389401031&pf_rd_m=A1VBAL9TL5WCBF&pf_rd_p=006764d9-6108-4b9a-b176-91bab4120f70&pf_rd_r=Y8988MGSV6C0YM02N8WP&pf_rd_s=merchandised-search-3&qid=1630829267&refinements=p_89%3ANokia&rnid=3837712031&s=electronics&sr=1-1",
        "name": "Nokia",
        "target_price": 1500

    },
    {
        "prod_URL":"https://www.amazon.in/Vivo-Y20G-Storage-Additional-Exchange/dp/B08LRD6YM1/ref=sr_1_1?dchild=1&qid=1630995778&refinements=p_89%3AVivo&rnid=3837712031&s=electronics&sr=1-1",
        "name":"Vivo Y20G",
        "target_price": 16000
    }

]


def give_me_price(URL):
    headers = {
        "user-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4577.63 Safari/537.36"

    }
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    price = soup.find(id="priceblock_ourprice")
    if (price == None):
        price = soup.find(id="priceblock_dealprice")

    return price.getText()


Result = open('file.text', 'w')

try:
    for every_prod in Products_to_track:
        Indprice = give_me_price(every_prod.get("prod_URL"))
        print(f"Mobile {every_prod.get('name')} has a price of {Indprice}")

        my_indprice = Indprice[1:-3]
        my_indprice = my_indprice.replace(',', '')
        my_indprice = int(float(my_indprice))

        if my_indprice < every_prod.get("target_price"):
            print("You can buy!")
            Result.write(f"\nMobile {every_prod.get('name')} has a price of {my_indprice},under target price!!")
        else:
            print("Price has not changed")
finally:
    Result.close()
