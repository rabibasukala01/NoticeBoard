# logic and implementation to convert each pdf pages to png images

import fitz
import requests
test_url = "https://www.khec.edu.np/uploads/notice/Notice_20230131_1675154003_01.pdf"

response = requests.get(test_url)

# Open the PDF from the URL as a binary stream
with open('notice.pdf', "wb") as f:
    f.write(response.content)

# Open the PDF file
pdf_doc = fitz.open("notice.pdf")
print(len(pdf_doc))

# loop through pages
for x in range(len(pdf_doc)):
    # taking each page and saving as png
    page = pdf_doc[x]

    pix = page.get_pixmap()
    # print(pix)
    pix.save(f"pdfimages{x}.png")
