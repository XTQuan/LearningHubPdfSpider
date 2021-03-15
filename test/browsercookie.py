import requests
import browsercookie
import http.client

cj = browsercookie.load()

conn = http.client.HTTPSConnection("saplearninghub.plateau.com")

headers = {
    'cache-control': "no-cache",
    'postman-token': "83313036-c3d2-90ae-5bc5-3319cea9943e"
    }

conn.request("GET", "/icontent_e/CUSTOM_eu/sap/self-managed/ebook/EWM100_EN_Col18_v1/xml/topic15.svg", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))


url = 'https://saplearninghub.plateau.com/icontent_e/CUSTOM_eu/sap/self-managed/ebook/EWM100_EN_Col18_v1/xml/topic15.svg'
r = requests.get(url, cookies=cj)
print(r.content)
