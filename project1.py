from PyPDF2 import PdfMerger

ALL = ["1.pdf", "2.pdf"]
Pdf_merge = PdfMerger()

for newpdf in Pdf_merge:
    merge.append(newpdf)

merge.write("allnew.pdf")
merge.close()

