import re

fecha = re.compile(r"(\d\d-\d\d-\d\d\d\d)\s")
año = re.compile(r"\.\s(\d{4})\s", flags=re.MULTILINE)
periodo = re.compile(r"Per.odo.*?(\d\w)\nN.mero\s", flags=re.MULTILINE)

# --------------------------------------------------------------------------------
casilla_01 = re.compile(r"^Rendimientos.*?\s01(.*)\s02", flags=re.MULTILINE)
casilla_02 = re.compile(r"^Rendimientos.*?\s02(.*)\s03", flags=re.MULTILINE)
casilla_03 = re.compile(r"^Rendimientos.*?\s03(.*)", flags=re.MULTILINE)
# --------------------------------------------------------------------------------
casilla_04 = re.compile(r"^Rendimientos.*?\s04(.*)\s05", flags=re.MULTILINE)
casilla_05 = re.compile(r"^Rendimientos.*?\s05(.*)\s06", flags=re.MULTILINE)
casilla_06 = re.compile(r"^Rendimientos.*?\s06(.*)", flags=re.MULTILINE)
# --------------------------------------------------------------------------------
casilla_07 = re.compile(r"^Rendimientos.*?\s07(.*)\s08", flags=re.MULTILINE)
casilla_08 = re.compile(r"^Rendimientos.*?\s08(.*)\s09", flags=re.MULTILINE)
casilla_09 = re.compile(r"^Rendimientos.*?\s09(.*)", flags=re.MULTILINE)
# --------------------------------------------------------------------------------
casilla_10 = re.compile(r"^Rendimientos.*?\s10(.*)\s11", flags=re.MULTILINE)
casilla_11 = re.compile(r"^Rendimientos.*?\s11(.*)\s12", flags=re.MULTILINE)
casilla_12 = re.compile(r"^Rendimientos.*?\s12(.*)", flags=re.MULTILINE)
# --------------------------------------------------------------------------------
casilla_13 = re.compile(r"^Premios.*?\s13(.*)\s14", flags=re.MULTILINE)
casilla_14 = re.compile(r"^Premios.*?\s14(.*)\s15", flags=re.MULTILINE)
casilla_15 = re.compile(r"^Premios.*?\s15(.*)", flags=re.MULTILINE)
# --------------------------------------------------------------------------------
casilla_16 = re.compile(r"^Premios.*?\s16(.*)\s16", flags=re.MULTILINE)
casilla_17 = re.compile(r"^Premios.*?\s17(.*)\s17", flags=re.MULTILINE)
casilla_18 = re.compile(r"^Premios.*?\s18(.*)", flags=re.MULTILINE)
# --------------------------------------------------------------------------------
casilla_19 = re.compile(r"^Percepciones.*?\s19(.*)\s20", flags=re.MULTILINE)
casilla_20 = re.compile(r"^Percepciones.*?\s20(.*)\s21", flags=re.MULTILINE)
casilla_21 = re.compile(r"^Percepciones.*?\s21(.*)", flags=re.MULTILINE)
# --------------------------------------------------------------------------------
casilla_22 = re.compile(r"^Percepciones.*?\s22(.*)\s23", flags=re.MULTILINE)
casilla_23 = re.compile(r"^Percepciones.*?\s23(.*)\s24", flags=re.MULTILINE)
casilla_24 = re.compile(r"^Percepciones.*?\s24(.*)", flags=re.MULTILINE)
# --------------------------------------------------------------------------------
casilla_25 = re.compile(r"^Contraprestaciones.*?\s25(.*)\s26", flags=re.MULTILINE)
casilla_26 = re.compile(r"^Contraprestaciones.*?\s26(.*)\s27", flags=re.MULTILINE)
casilla_27 = re.compile(r"^Contraprestaciones.*?\s27(.*)", flags=re.MULTILINE)
# --------------------------------------------------------------------------------
casilla_30 = re.compile(r"^Resultado.*?\s30(.*)", flags=re.MULTILINE)


def to_number(number):
    return float(number.replace(".", "").replace(",", "."))


def check_match(input, string):
    try:
        result = input.search(string).group(1)
        if result:
            return to_number(result)
        else:
            return 0.00
    except AttributeError:
        return 0.00


def extract_perceptor_importe_retencion(s):
    casillas = [
        casilla_01,
        casilla_02,
        casilla_03,
        casilla_04,
        casilla_05,
        casilla_06,
        casilla_07,
        casilla_08,
        casilla_09,
        casilla_10,
        casilla_11,
        casilla_12,
        casilla_13,
        casilla_14,
        casilla_15,
        casilla_16,
        casilla_17,
        casilla_18,
        casilla_19,
        casilla_20,
        casilla_21,
        casilla_22,
        casilla_23,
        casilla_24,
        casilla_25,
        casilla_26,
        casilla_27,
        casilla_30,
    ]
    lst = [check_match(casilla, s) for casilla in casillas]
    mylist = (
        lst[0:12]
        + [lst[12] + lst[18] + lst[24]]
        + [lst[15] + lst[21]]
        + [lst[14] + lst[20] + lst[26]]
        + [lst[16] + lst[22]]
        + [lst[14] + lst[20] + lst[26]]
        + [lst[17] + lst[23]]
        + [lst[27]]
    )
    return mylist
