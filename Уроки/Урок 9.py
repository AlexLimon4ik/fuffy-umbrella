# import urllib.request

# opener = urllib.request.build_opener()
# responde = opener.open("https://images.app.goo.gl/5FcenYmhv4JKmip17")
# print(responde.read())

# import requests

# responde = requests.get('https://httpbin.org/post')
# print(responde.content)
# print(f"Datatype - {type(responde.content)}")

# responde = requests.post('https://httpbin.org/post', data="Test data")
# headers = {"h1": "Test title"}
# print(responde.content)
# print(f"Datatype - {type(responde.content)}")

# res_parse_list = []
# responde = requests.get("https://coinmarketcap.com/")
# responde_text = responde.text
# responde_parse = responde_text.split("<span>")
# for pars_elem_1 in responde_parse:
#     if pars_elem_1.startswith("$"):
#         for pars_elem_2 in pars_elem_1.split("</span"):
#             if pars_elem_2.startswith("$") and pars_elem_2[1].isdigit():
#                 res_parse_list.append(pars_elem_2)

# bitcoin = res_parse_list[0]
# print(bitcoin)

from bs4 import BeautifulSoup
import requests
response = requests.get("https://coinmarketcap.com/")
if response.status_code == 200:
    soup = BeautifulSoup(response.text, features="html.parser")
    soup_list = soup.find_all("a", {"href": "/currencies/bitcoin/#markets"})
    res = soup_list[0].find("span")
    print(res.text)     