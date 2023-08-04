from PyPDF2 import PdfMerger

pdf = ["1.pdf", "2.pdf"]
merge = PdfMerger()

for newpdf in pdf:
    merge.append(newpdf)

merge.write("new.pdf")
merge.close()

