from PyPDF2 import PdfWriter
import os

# if not os.path.exists("Pdfs"):
#     os.mkdir("Pdfs")

merger = PdfWriter()
files = [file for file in os.listdir("Pdfs") if file.endswith(".pdf")]

for pdf in files:
    merger.append(f"Pdfs/{pdf}")

merger.write("Pdfs/merger-pdf.pdf")
merger.close()

print("Pdf merged successfully")
