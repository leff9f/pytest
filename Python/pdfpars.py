import slate3k
import openpyxl

# open pdf file with prop: read boolean
with open('1312_03_13.pdf', 'rb') as f:
    doc = slate3k.PDF(f)
print(doc)

# open txt file for writing and write text from pdf
with open('1312.txt', 'w', encoding='utf-8') as fg:
    fg.write(str(doc))

# open txt file for reading and read text to txt0
with open('1312.txt', 'r', encoding='utf-8', errors='ignore') as file:
    txt = file.readline()

# text clearing
txt_pr = str(txt).split('\\n')
txt_cleared = []
for a in txt_pr:
    if a != '':
        txt_cleared.append(a)

#допилить загрузку в эксель
#print(txt_cleared.count('[\'Труба' or '\\\\x0c\', \'Труба'))




#ind = txt3.index('Труба')
#txt2 = txt3[ind+2]
print(len(txt_pr))
print(txt_cleared)

#b = text1.split('\n')
#print(tt)


#import PyPDF2

#pl = open('1313.pdf', 'rb')
#pl_read = PyPDF2.PdfFileReader(pl)
#num_p = pl_read.numPages
#get_page = pl_read.getPage(2)
#text1 = get_page.extractText()

#with open('1312.txt', 'w', encoding='utf-8') as fg:
#    fg.write(text1)