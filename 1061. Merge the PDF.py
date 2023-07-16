from PyPDF2 import PdfWriter
import os

merger = PdfWriter() # Create a PdfWriter object
files = [file for file in os.listdir() if file.endswith(".pdf")] # Get a list of PDF files in the current directory

for pdf in files:
    merger.append(pdf) # Append each PDF file to the merger

merger.write("merged-pdf.pdf") # Write the merged PDF to a new file
merger.close()
