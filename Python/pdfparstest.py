import PyPDF2

pl = open('13122.pdf', 'rb')
pl_read = PyPDF2.PdfFileReader(pl)
num_p = pl_read.numPages
get_page = pl_read.getPage(2)
text1 = get_page.extractText()
print(text1)

with open('1312.txt', 'w', encoding='utf-8', errors='ignore') as fg:
    fg.write(text1)
