# import os
import pdfkit
from flask import render_template
from urllib.request import urlopen
from app.config import  STATIC_FILES_URL
from app.plataforma.utils import sendCorreo as send_methods
# test
from PyPDF2 import PdfFileMerger, PdfFileReader, PdfFileWriter

# =================================================================
def create_pdf_list_test(pdf_data):
    pdf_list = []
    if pdf_data:
        # condition_name = f"{pdf_data.get('nameTestPdf')}"
        condition_name = "test"
        condition_pdf = create_pdf(condition_name, 'test_pdf_dev.html', pdf_data)
        pdf_list.append(condition_pdf)

    return pdf_list


def send_documents_test(contractor, affiliates, pdf_list):
    contractor_nameDoctor = "contractor_nameDoctor"
    contractor_namePaciente = "contractor_namePaciente"
    # print("Correo a enviar", contractor.get('email', ''))
    contractor_email = 'renzoeliasdelacalle@gmail.com'
    # contractor_email = "renzoeliasdelacalle@gmail.com"
    email_subject = 'TEST ENVIO PDF'

    # affiliate_list = []
    # for affiliate in affiliates:
    #     affiliate_list.append({
    #         'names': affiliate.get('affiliate').get_names(),
    #         'last_names': affiliate.get('affiliate').get_last_names(),
    #     })

    data = {
        "contractor_name":"Maykol",
        "affiliates":[
            {
                "document_id":"42127533",
                "names":"Maykol Cristiam",
                "last_names":"Linares Monteza"
            },
            {
                "document_id":"32945234",
                "names":"Victoria Ruby",
                "last_names":"Celis Salinas"
            }
        ],
        "affiliate_cert":[
            {
                "certificate_id":"000300000086"
            },
            {
                "certificate_id":"000300000086"
            },
        ]
    }

    email_body = render_template('test_correo_dev.html', data=data)
    send_methods.sendCorreoAdjunto(
        email_body,
        email_subject,
        contractor_email,
        pdf_list
    )
# =================================================================


def create_pdf_list(pdf_data):
    pdf_list = []
    if pdf_data:
        # 2. PDF DEL CONDICIONADO PARTICULAR
        # condition_data = {
        #     'contractor': {
        #         'name': "contractor"
        #     },
        #     'plan_name': "plan_name",
        # }
        # condition_data['affiliates'] = [affiliate_data]
        # condition_name = f'{number_certificate}-condicionado-particular'
        # condition_pdf = create_pdf(condition_name, 'generar-orden-pdf.html', condition_data)
        
        name_file = f"{pdf_data.get('idsiniestro')}"
        # pdf_lab = create_pdf(name_file+'-lab', 'pdf-orden-lab.html', pdf_data)
        
        print("pdf_data - ", pdf_data)
        # pdf_lab = create_pdf_register(name_file+'-lab', 'pdf-orden-lab.html', pdf_data)
        pdf_lab = create_pdf_register(name_file, 'pdf-orden-atencion.html', pdf_data)
        
        # pdf_list.extend([pdf_lab, pdf_img, pdf_receta])
        pdf_list.append(pdf_lab)
        # pdf_list.append(condition_pdf)

    return pdf_list

def create_pdf(name, template_name, data):
    pdf_name = f'{name}.pdf'
    pdf_body = render_template(template_name, data=data)

    options = {
        'page-size': 'A4',
        'margin-top': '0.5in',
        'margin-right': '0.5in',
        'margin-bottom': '0.5in',
        'margin-left': '0.5in',
        'encoding': 'UTF-8',
    }

    pdfkit.from_string(pdf_body, pdf_name, options)
    if 'qr_code_path' in data:
        qr_path = data.get('qr_code_path').split('/')
        return [pdf_name, qr_path[len(qr_path)-1]]
    else:
        return pdf_name
    
def create_pdf_register(name, template_name, data):
    pdf_name = f'{name}.pdf'
    pdf_body = render_template(template_name, data=data)
    
    ruta_footer = './app/plataforma/templates/00-footer.html'
    ruta_header = './app/plataforma/templates/00-header.html'
    
    options = {
        'page-size': 'A4',
        'margin-top': '0.5in',
        'margin-right': '0.5in',
        'margin-bottom': '0.5in',
        'margin-left': '0.5in',
        'encoding': 'UTF-8',
        'header-spacing': -13,
        'header-html': ruta_header,
        # 'footer-spacing': -2,
        # 'footer-spacing': -10,
        'footer-spacing': -14,
        'footer-html': ruta_footer,
    }

    pdfkit.from_string(pdf_body, pdf_name, options)
    if 'qr_code_path' in data:
        qr_path = data.get('qr_code_path').split('/')
        return [pdf_name, qr_path[len(qr_path)-1]]
    else:
        return pdf_name

def create_pdf_test_global(name, template_name, data, count=0, code_iafa=""):
    count_pdf = f'{count}'

    pdf_name = f'{name}.pdf'
    pdf_body = render_template(template_name, data=data)

    # code_susalud=''
    # breakpoint()
    # code_susalud = ''
    code_susalud = 'Código de registro Susalud: ' + str(code_iafa) if code_iafa != '' and code_iafa else ' '
    ruta_footer = './app/plataforma/templates/00-footer.html'
    ruta_header = './app/plataforma/templates/00-header.html'

    # print("code_iafa", code_iafa)
    print("code_susalud", code_susalud)

    options = {
        'page-size': 'A4',
        'margin-top': '0.5in',
        'margin-right': '0.5in',
        'margin-bottom': '0.5in',
        'margin-left': '0.5in',
        'encoding': 'UTF-8',
        'header-spacing': -13,
        'header-html': ruta_header,
        # 'footer-spacing': -2,
        # 'footer-spacing': -10,
        'footer-spacing': -14,
        'footer-html': ruta_footer,
        'page-offset': count_pdf,
        'replace': [('code', code_susalud)],
    }

    pdfkit.from_string(pdf_body, pdf_name, options)
    if 'qr_code_path' in data:
        qr_path = data.get('qr_code_path').split('/')
        return [pdf_name, qr_path[len(qr_path)-1]]
    else:
        return pdf_name

def create_pdf_test(name, template_name, data, count=0):
    pdf_name = f'{name}.pdf'
    count_pdf = f'{count}'
    pdf_body = render_template(template_name, data=data)

    ruta_footer = './app/plataforma/templates/00-footer.html'
    code_susalud = ''

    if len(data) > 1:
        code_susalud = ''
    elif len(data) == 1 :
        if data[0]['plan_id'] == 3:
            code_susalud = 'Código de registro Susalud: 20031-0008'
        elif data[0]['plan_id'] == 4:
            code_susalud = 'Código de registro Susalud: 20031-0007'
        elif data[0]['plan_id'] == 5:
            code_susalud = 'Código de registro Susalud: 20031-0006'
        elif data[0]['plan_id'] == 6:
            code_susalud = 'Código de registro Susalud: 20031-0005'
        elif data[0]['plan_id'] == 7:
            code_susalud = 'Código de registro Susalud: 20031-0004'
        elif data[0]['plan_id'] == 8:
            code_susalud = 'Código de registro Susalud: 20031-0003'

    options = {
        'page-size': 'A4',
        'margin-top': '0.5in',
        'margin-right': '0.5in',
        'margin-bottom': '0.5in',
        'margin-left': '0.5in',
        'encoding': 'UTF-8',
        'footer-spacing': -2,
        'footer-html': ruta_footer,
        'page-offset': count_pdf,
        'replace': [('code', code_susalud)],
    }

    pdfkit.from_string(pdf_body, pdf_name, options)
    if 'qr_code_path' in data:
        qr_path = data.get('qr_code_path').split('/')
        return [pdf_name, qr_path[len(qr_path)-1]]
    else:
        return pdf_name

def send_documents(user, info, pdf_list):
    
    # affiliate_list = []
    # for affiliate in affiliates:
    #     affiliate_list.append({
    #         'names': affiliate.get('affiliate').get_names(),
    #         'last_names': affiliate.get('affiliate').get_last_names(),
    #     })
    
    user_nameDoctor = user.get('fullnameDoctor', '').title()
    user_namePaciente = user.get('fullnamePaciente', '').title()
    user_name = user.get('user_name', '').title()
    
    user_email = user.get('email', '')
    copy_email = user.get('copy_email', '')
    email_subject = 'Resumen de atención médica'

    data = {
        'user_nameDoctor': user_nameDoctor,
        'user_namePaciente': user_namePaciente,
        'user_name': user_name,
    }
    
    email_body = render_template('generar-orden.html', data=data)
    send_methods.sendCorreoAdjunto(
        email_body,
        email_subject,
        user_email,
        pdf_list,
        copy_email
    )

def download_file(filename, download_filename="file"):
    url =f'{STATIC_FILES_URL}{filename}'
    response = urlopen(url)
    general_pdf = f'{download_filename}.pdf'
    with open(general_pdf, 'wb') as pdf_file:
        pdf_file.write(response.read())
    return general_pdf




