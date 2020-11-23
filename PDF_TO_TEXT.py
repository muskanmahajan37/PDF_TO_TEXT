import PyPDF2


pdfFileObject = open(r"<pdf_path>", 'rb')

pdfReader = PyPDF2.PdfFileReader(pdfFileObject)

print(" No. Of Pages :", pdfReader.numPages)

pageObject = pdfReader.getPage(0)
print(pageObject.extractText())

pdfFileObject.close()