from xml.dom.minidom import Document
# import xml.dom.minidom

class XmlMaker:


    def __init__(self,txtpath,xmlpath):
        self.txtPath = txtpath
        self.xmlPath = xmlpath
        self.txtList = []


    def readtxt(self):
        txtfile = open(self.txtPath,"r",encoding='gbk',errors='ignore')
        self.txtList = txtfile.readlines()
        for i in self.txtList:
            oneline = i.strip().split(" ")
            if len(oneline) != 5:
                print("TxtError")

    def makexml(self):
        doc = Document()
        orderpack = doc.createElement("OrderPack")
        doc.appendChild(orderpack)
        objecname = "Order"
        for i in self.txtList:
            oneline = i.strip().split(" ")
            objectE = doc.createElement(objecname)
            objectE.setAttribute("number",oneline[0])

            objectcontent = doc.createElement("Content")
            objectcontenttext = doc.createTextNode(oneline[1])
            objectcontent.appendChild(objectcontenttext)
            objectE.appendChild(objectcontent)

            objectresult = doc.createElement("Result")
            objectresulttext = doc.createTextNode(oneline[2])
            objectresult.appendChild(objectresulttext)
            objectE.appendChild(objectresult)

            objectappname = doc.createElement("AppName")
            objectappnametext = doc.createTextNode(oneline[3])
            objectappname.appendChild(objectappnametext)
            objectE.appendChild(objectappname)

            objectdelay = doc.createElement("Delay")
            objectdelaytext = doc.createTextNode(oneline[4])
            objectdelay.appendChild(objectdelaytext)
            objectE.appendChild(objectdelay)

            orderpack.appendChild(objectE)

        f = open(self.xmlPath, 'w')
        doc.writexml(f, indent='\t', newl='\n', addindent='\t', encoding='gbk')
        f.close()



if __name__ == "__main__":
    read =XmlMaker("test.txt","test.xml")
    read.readtxt()
    read.makexml()
    print(read.txtPath)
    for i in read.txtList:
        print(i)