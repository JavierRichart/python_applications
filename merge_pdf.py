from PyPDF4 import PdfFileMerger
import os

merger = PdfFileMerger()
for items in os.listdir(''):
    if items.endswith('.pdf'):
        merger.append(items)
    merger.write("final_pdf.pdf")
    merger.close()

for items in os.listdir():
    if items != 'final_pdf.pdf' and items.endswith('.pdf'):
        os.remove(items)
