from svglib.svglib import svg2rlg
from reportlab.graphics import renderPDF
import requests
import os
import PyPDF2

headers = {
  'Cookie': 'AKAMAI_AUTH_COOKIE=~expires=1616640967~access=/icontent_e/CUSTOM_eu/sap/lhcust/Steeb/*!/icontent_e/CUSTOM/sap/*!/icontent_e/CUSTOM_eu/sap/lhcust/Hitachi/*!/icontent_e/CUSTOM_eu/sap/lhcust/1335114/*!/icontent_e/CUSTOM_eu/sap/lhcust/16223/*!/icontent_e/CUSTOM_eu/sap/lhcust/SASHAKTA/*!/icontent_e/CUSTOM_eu/sap/lhcust/PGK/*!/icontent_e/CUSTOM_eu/sap/lhcust/IBM/*!/icontent_e/CUSTOM_eu/sap/lhcust/electromech/*!/icontent_e/CUSTOM_eu/sap/lhcust/MUR/*!/icontent_e/CUSTOM_eu/sap/lhcust/MB/*!/icontent_e/CUSTOM_eu/sap/*!/icontent_e/CUSTOM_eu/sap/lhcust/2017939/*!/icontent_e/CUSTOM/platlap/*!/icontent_e/CUSTOM_eu/sap/lhcust/941031/*!/icontent_e/CUSTOM_eu/sap/lhcust/CSC/*!/icontent_e/CUSTOM_eu/sap/lhcust/1400618/*!/icontent/public/*!/icontent_e/public/*~md5=380e3bfcff5903642f2965ffe75ba73a; BIGipServerP_ORIGIN-EU-ICONTENT.PLATEAU.COM-80=!Fh9Ui1aeqZGWnPJLEOpnqJbIIHncHA/gz5/N4yHQTKzhqExPkPSYg686qyqUlBnsGfuI+QBQeXA0Aw==; PSA_CPNT_ID=EWM100%5fEN%5fCol18; PSA_CPNT_REV_DATE=01%2f12%2f2013%2012%3a00%3a00%20Greenwich%20Mean%20Time; PSA_CPNT_REV_NUMBER=1; PSA_CPNT_TYPE_ID=e%2dbook; PSA_STUD_CPNT_ID=12803416; PSA_STUD_CPNT_MOD_ID=207699; PSA_STUD_CPNT_MOD_NAME=Processes%2520in%2520SAP%2520Extended%2520Warehouse%2520Management; SKIP_LMS_MAINT_NOTIFY=Y; TENANT_AUTH_COOKIE=saplearnhub; route=032b090601adaf5c1ce98da7f649827e3fdc8795'
}
bookName = 'EWM100'
allPage = 214
curPage = 1

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
    with open(rootDir + "\\Merged.pdf", 'wb') as write_out_file:
        pdfFM.write(write_out_file)

    while page <= allPage:
        file.close()

# url = "https://saplearninghub.plateau.com/icontent_e/CUSTOM_eu/sap/self-managed/ebook/EWM100_EN_Col18_v1/xml/topic14.svg"
if __name__ == '__main__':
    # while curPage <= allPage:
    #     url = "https://saplearninghub.plateau.com/icontent_e/CUSTOM_eu/sap/self-managed/ebook/EWM100_EN_Col18_v1/xml/topic" + str(curPage) + ".svg"
    #     response = requests.request("GET", url, headers=headers, data=payload)
    #     # print(response.text)
    #     fileName = rootDir + '\\svg\\' + str(curPage) + '.svg'
    #     with open(fileName, 'w', encoding='utf-8') as f:
    #         f.write(response.text)
    #     drawing = svg2rlg(fileName)
    #     renderPDF.drawToFile(drawing, rootDir + '\\pdf\\' +str(curPage) + ".pdf")
    #     print('正在下载第' + str(curPage) + '/' + str(allPage) + '页......' )
    #     curPage += 1
    mergePDF()
