from output import write_to_xlsx
from intro_func import (
    get_pdf_files,
    extract_data_file,
)


def main():
    pdf_files = get_pdf_files()
    rows = []  # List that will contain the data of all rows (list of lists)
    for file in pdf_files:
        months = extract_data_file(file)
        for month in months:
            rows.append(month)
    write_to_xlsx(rows)


if __name__ == "__main__":
    main()
