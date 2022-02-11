from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
import requests
import os
import PyPDF2

headers = {
  'Cookie': ''
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
