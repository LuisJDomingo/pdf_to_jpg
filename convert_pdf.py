import fitz
from PIL import Image

def pdf_to_jpf(pdf_path, output_folder):
    pdf_document = fitz.open(pdf_path)
    for page in range(len(pdf_document)):
        page = pdf_document[page]
        pix = page.get_pixmap(dpi=300)
        image_path = f"{output_folder}/page_{page_num+1}.jpg"
        img
