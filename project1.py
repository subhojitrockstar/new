from PyPDF2 import PdfMerger

ALL = ["1.pdf", "2.pdf"]
Pdf_merge = PdfMerger()

for newpdf in Pdf_merge:
    Pdf_merge.append(newpdf)

Pdf_merge.write("allnew.pdf")
Pdf_merge.close()

