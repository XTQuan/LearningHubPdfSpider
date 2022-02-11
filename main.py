from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
import requests
import os
import PyPDF2

headers = {
  'Cookie': 'AKAMAI_AUTH_COOKIE=~expires=1619334394~access=/icontent_e/CUSTOM_eu/sap/lhcust/Steeb/*!/icontent_e/CUSTOM/sap/*!/icontent_e/CUSTOM_eu/sap/lhcust/Hitachi/*!/icontent_e/CUSTOM_eu/sap/lhcust/1335114/*!/icontent_e/CUSTOM_eu/sap/lhcust/16223/*!/icontent_e/CUSTOM_eu/sap/lhcust/SASHAKTA/*!/icontent_e/CUSTOM_eu/sap/lhcust/PGK/*!/icontent_e/CUSTOM_eu/sap/lhcust/IBM/*!/icontent_e/CUSTOM_eu/sap/lhcust/electromech/*!/icontent_e/CUSTOM_eu/sap/lhcust/MUR/*!/icontent_e/CUSTOM_eu/sap/lhcust/MB/*!/icontent_e/CUSTOM_eu/sap/*!/icontent_e/CUSTOM_eu/sap/lhcust/2017939/*!/icontent_e/CUSTOM/platlap/*!/icontent_e/CUSTOM_eu/sap/lhcust/941031/*!/icontent_e/CUSTOM_eu/sap/lhcust/CSC/*!/icontent_e/CUSTOM_eu/sap/lhcust/1400618/*!/icontent/public/*!/icontent_e/public/*~md5=7bbcb5c5c4eb5e936d17cd0d8efd173b; BIGipServerP_ORIGIN-EU-ICONTENT.PLATEAU.COM-80=!Fh9Ui1aeqZGWnPJLEOpnqJbIIHncHA/gz5/N4yHQTKzhqExPkPSYg686qyqUlBnsGfuI+QBQeXA0Aw==; SKIP_LMS_MAINT_NOTIFY=Y; TENANT_AUTH_COOKIE=saplearnhub; route=032b090601adaf5c1ce98da7f649827e3fdc8795'
}

bookName = 'AC233_EN_Col16_v1' # 175
curPage = 1
allPage = 175

# url = "https://saplearninghub.plateau.com/icontent_e/CUSTOM_eu/sap/self-managed/ebook/SAPX01_EN_Col17_v2/xml/topic1.svg"
urlTopic = "https://saplearninghub.plateau.com/icontent_e/CUSTOM_eu/sap/self-managed/ebook/" + bookName + "/xml/topic"

rootDir = os.path.dirname(os.path.abspath("__file__"))
rootDir = rootDir + '\\result\\' + bookName
# print(rootDir)
payload={}

def mergePDF():
    pdfFM = PyPDF2.PdfFileMerger()
    page = 1
    while page <= allPage:
        file = open(rootDir + '\\pdf\\' +str(page) + ".pdf", 'rb')
        pdfFM.append(file)
        page += 1

    # output the file.
    with open(rootDir + "\\" + bookName + ".pdf", 'wb') as write_out_file:
        pdfFM.write(write_out_file)

    while page <= allPage:
        file.close()

if __name__ == '__main__':
    # Bookdir
    dir = rootDir
    if not os.path.exists(dir):
        os.makedirs(dir)
    dir = rootDir + '\\pdf\\'
    if not os.path.exists(dir):
        os.makedirs(dir)
    dir = rootDir + '\\svg\\'
    if not os.path.exists(dir):
        os.makedirs(dir)

    while curPage <= allPage:
        print('正在下载第' + str(curPage) + '/' + str(allPage) + '页......' )
        url = urlTopic  + str(curPage) + ".svg"
        response = requests.request("GET", url, headers=headers, data=payload, verify=False)
        # print(response.text)
        fileName = rootDir + '\\svg\\' + str(curPage) + '.svg'
        with open(fileName, 'w', encoding='utf-8') as f:
            f.write(response.text)
        drawing = svg2rlg(fileName)
        renderPDF.drawToFile(drawing, rootDir + '\\pdf\\' +str(curPage) + ".pdf")
        curPage += 1
    mergePDF()
