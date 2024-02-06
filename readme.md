# Project Title: Spanish Tax Information Extractor (Mod 111)

This project is designed to extract specific information about a tax in Spain, specifically Mod 111. It reads PDF files, extracts the necessary data, and writes the output to an Excel file.

## Project Structure

The project consists of several Python files:

- `definitive.py`: This is the main entry point of the application. It uses functions from `intro_func.py` to extract data from PDF files and then writes the extracted data to an Excel file using a function from `output.py`.

- `intro_func.py`: This file contains functions for reading PDF files and extracting data from them. The `extract_data_file` function is used to extract data from a single file, and the `extract_data_page` function is used to extract data from a single page of a PDF file.

- `output.py`: This file contains functions for writing data to an Excel file. The `write_to_xlsx` function is used to write the extracted data to an Excel file.

- `support_regex.py`: This file contains the `extract_perceptor_importe_retencion` function, which uses regular expressions to extract specific pieces of data from the text of a PDF file.

## How to Run

To run the project, execute the `definitive.py` script. This will read all PDF files in the current directory, extract the necessary data, and write the output to an Excel file named "Modelo 111.xlsx".

```sh
python definitive.py
```
## Dependencies

This project depends on the following Python libraries:

- `pdfplumber` for reading PDF files
- `openpyxl` for writing to Excel files
- `csv` for reading CSV files

Make sure to install these dependencies before running the project:

```sh
pip install pdfplumber openpyxl csv
```