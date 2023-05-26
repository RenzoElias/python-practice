import jwt
import os
import pytz
import uuid
from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter
from datetime import datetime
from num2words import num2words
from datetime import date


def remove_pdf(pdf_list):
    for pdf in pdf_list:
        if os.path.isfile(pdf):
            os.remove(pdf)


def unir_pdf(pdf_unir, name='file'):
    fusionador = PdfFileMerger()
    nombre_archivo_salida = f'{name}.pdf'

    # print('Unir PDFs')
    # for pdf in pdf_unir:
    #     fusionador.append(PdfFileReader(open(pdf,'rb')),import_bookmarks=False)
    
    print('Unir PDFs')
    for pdf in pdf_unir:
        with open(pdf,'rb') as pdfAux:
            fusionador.append(PdfFileReader(pdfAux),import_bookmarks=False)
        # os.remove(pdf)
    # with open(nombre_archivo_salida, 'wb') as salida:
    #     fusionador.write(salida)
    
    print('Write Unificado PDFs', pdf_unir, fusionador)
    fusionador.write(nombre_archivo_salida)
    fusionador.close()

    remove_pdf(pdf_unir)

    # for pdf in pdf_unir:
    #     if os.path.isfile(pdf):
    #         os.remove(pdf)

    # print('Limpiar PDFs temporales', pdf_unir) # se usara el metodo externo

    # try:
    #     for pdf in pdf_unir:
    #         if os.path.isfile(pdf):
    #             os.remove(pdf)
    # except:
    #     print("Error in")

    return nombre_archivo_salida


def count_pages_pdf(name):
    if name:
        pdf_name = f'{name}.pdf'
        pdf_existente = PdfFileReader(open(pdf_name, "rb"))
        numero_de_paginas = pdf_existente.getNumPages()

        return numero_de_paginas
    else:
        return 0


def format_value(value: str, style: str = ""):
    if not value:
        return ""

    value = value.strip()
    if style == "upper":
        return value.upper()
    if style == "title":
        return value.title()
    if style == "capitalize":
        return value.capitalize()
    if style == "lower":
        return value.lower()
    else:
        return value


def generate_token():
    token = uuid.uuid4()
    return str(token)


def remove_duplicates(elements):
    """
    * Elimina los elementos duplicados de una lista
    * @param elements es de tipo list
    * Retorna una nueva lista de elementos únicos
    """
    res_list = []
    for index in range(len(elements)):
        if elements[index] not in elements[(index + 1) :]:
            res_list.append(elements[index])
    return res_list


def concatenate_list(values, style=""):
    """
    * Concatena un conjunto de strings de una lista en un string
    * @param values es una lista de strings
    * @param style puede tomar los valores de lower, upper o title
    * Retorna un string concatenado de los elementos del parámetro values
    """
    concatenate = ""
    for value in values:
        if value:
            concatenate += f"{value.strip()} "
    result = concatenate.strip()

    if style == "lower":
        return result.lower()
    elif style == "upper":
        return result.upper()
    elif style == "title":
        return result.title()
    else:
        return result


def separate_names(names):
    name_list = names.split(" ")
    first_name = name_list[0]
    middle_name = " ".join(name_list[1:])
    return {
        "first_name": first_name,
        "middle_name": middle_name,
    }


def calculate_age(born_date):
    today = date.today()
    one_or_zero = (today.month, today.day) < (born_date.month, born_date.day)
    year_difference = today.year - born_date.year
    age = year_difference - one_or_zero
    return age


def encode_payload(payload, key="secret", algorithm="HS256"):
    encoded_jwt = jwt.encode(payload, key, algorithm=algorithm)
    return encoded_jwt


def get_local_time(utc_time, timezone="America/Lima"):
    local_timezone = pytz.timezone(timezone)
    current_time = utc_time.replace(tzinfo=pytz.utc)
    return current_time.astimezone(tz=local_timezone)


def convert_datetime_to_str(current_datetime, format_datetime="%Y-%m-%d %H:%M:%S"):
    if not current_datetime:
        return ""
    return current_datetime.strftime(format_datetime)


def convert_str_to_datetime(str_date, format_date='%d/%m/%Y'):
    return datetime.strptime(str_date, format_date)


def convert_float_to_str(number):
    return "%.2f" % float(number)


def get_tax_amounts(amount: float, is_str=False):
    total_amount = amount or 0
    taxable_amount = total_amount / 1.18 or 0
    tax_amount = (total_amount - taxable_amount) or 0

    if is_str:
        return {
            "total_amount": convert_float_to_str(total_amount),
            "taxable_amount": convert_float_to_str(taxable_amount),
            "tax_amount": convert_float_to_str(tax_amount),
        }

    return {
        "tax_amount": round(tax_amount, 2),
        "taxable_amount": round(taxable_amount, 2),
        "total_amount": round(total_amount, 2),
    }


def transform_amount_to_word(amount: str):
    [int_value, decimal_value] = amount.split(".")
    amount_word = num2words(int_value, lang="es")
    decimal_value = decimal_value.zfill(2)
    amount_word = f"{amount_word} CON {decimal_value}/100".upper()
    return amount_word


def delete_files(file_list):
    for item in file_list:
        if os.path.isfile(item):
            os.remove(item)


def remove_files(files, parent_dir=""):
    for removed_file in files:
        file_deleted = f"{parent_dir}/{removed_file}" if parent_dir else removed_file
        if os.path.isfile(file_deleted):
            os.remove(file_deleted)


def tipo_documento (s):
    if s == 1:
        return 'DNI'
    else:
        return 'OTROS'



