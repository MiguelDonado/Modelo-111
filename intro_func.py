import os
import pdfplumber
from support_regex import fecha, año, periodo, extract_perceptor_importe_retencion


def get_pdf_files():
    pdf_files = [f for f in os.listdir(".") if f.endswith(".pdf")]
    return pdf_files


def read_pdf(file):
    # It'll return the text from the PDF file as one string
    with pdfplumber.open(file) as pdf:
        text_file = [page.extract_text() for page in pdf.pages]
    return text_file


def extract_data_page(page):
    if "realizada" in page:
        fecha_field = fecha.search(page).group(1)
        return [fecha_field]
    elif "Forma de" in page:
        año_field = [año.search(page).group(1)]
        periodo_field = [periodo.search(page).group(1)]
        amounts = extract_perceptor_importe_retencion(page)
        final = [año_field, periodo_field, amounts]
        flattened = [item for sublist in final for item in sublist]
        return flattened

    else:
        return None


def extract_data_file(file):
    text_file = read_pdf(file)
    row = []
    rows = []
    for page in text_file:
        if provisional_row := extract_data_page(page):
            row.extend(provisional_row)
        else:
            row.append("ERROR")
        if row == ["ERROR"] * 2:
            row = ["ERROR"] * 22
            rows.append(row)
            row = []
        if len(row) > 10:
            rows.append(row)
            row = []
    return rows
