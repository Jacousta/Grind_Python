import requests
from bs4 import BeautifulSoup
import lxml
import smtplib

head = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7)"
                  " AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36",
    "Accept-Language": "en-GB,en-US;q=0.9,en;q=0.8"

}
response = requests. \
    get(
    url="https://www.amazon.com/Total-Wireless-Apple-iPhone-Generation/dp/B09VY71F9M/?_encoding=UTF8&pd_rd_w=sUX60&c"
        "ontent-id=amzn1.sym.7f957896-9457-4ac3-8c2b-58f2b6be2857&pf_rd_p=7f957896-9457-4ac3-8c2b-58f2b6be2857&pf_"
        "rd_r=T0K2PNXNVPVMTVK45H25&pd_rd_wg=eRkMU&pd_rd_r=f9d1a7e6"
        "-ea8e-4cfa-9ffe-c7135d26ea47&ref_=pd_gw_exports_top_sellers_unrec",headers=head)

soup = BeautifulSoup(response.text,parser=lxml,features="lxml")
price = soup.find_all("span",class_="a-offscreen")
actual_price = (float(price[0].text.split("$")[1]))
target_price = 350
if actual_price <= target_price:
    print("Paste code to send mail USELESS")
    pass

