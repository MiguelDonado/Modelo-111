from openpyxl import Workbook
import csv


def write_to_xlsx(meses):
    # The argument is a list with 12 tuples. Each tuples contains the desired data for each month.
    # It creates a xlsx with the desired format.

    fieldnames = get_cabeceras()

    wb = Workbook()
    ws = wb.active
    ws.append(fieldnames)

    for mes in meses:
        ws.append(mes)

    wb.save("Modelo 111.xlsx")


def get_cabeceras():
    # This function returns the cabeceras that are used in Dossier Anual HH-2
    with open("cabeceras.csv", "r") as file:
        reader = csv.reader(file)
        cabeceras = [row[0] for row in reader]  # Get the first column from each row
        return cabeceras
