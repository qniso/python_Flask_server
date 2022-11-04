import requests
from docx.shared import Mm
from docxtpl import DocxTemplate, InlineImage

import datetime
from datetime import timedelta

from shared.components.mongo.mongo import send_doc


def generate_document(date_start, date_end, name):
    days_count = '-'
    a = ''
    doc = DocxTemplate('shared/components/documents/template/template_holiday/holiday_template.docx')
    shtamp = InlineImage(doc,
                         image_descriptor='shared/components/documents/template/img/izgotovlenie-faksimile-300x300-2.png',
                         width=Mm(40), height=Mm(40))
    datetime_conv_start = datetime.date(int(date_start.split(".")[2]), int(date_start.split(".")[1]),
                                        int(date_start.split(".")[0]))
    datetime_conv_end = datetime.date(int(date_end.split(".")[2]), int(date_end.split(".")[1]),
                                      int(date_end.split(".")[0]))

    delta = datetime_conv_end - datetime_conv_start
    for i in range(delta.days + 1):
        day = datetime_conv_start + timedelta(days=i)
        days_count = str(delta.days)
    if (int(days_count) + 1 > 3 or not int(days_count) == 1):
        a = 'днів'
    elif (int(days_count) + 1 % 10 == 2):
        a = 'дні'
    else:
        a = 'день'

    context = {
        'company_name': 'OATS',
        'person_name': f'{name}',
        'date_start': f'{date_start}',
        'date_end': f'{date_end}',
        'days_count': f'{int(days_count) + 1}',
        'days_word': f'{a}',
        'date': datetime.datetime.now().strftime("%m.%d.%Y"),
        'print': shtamp,
    }
    doc.render(context)
    doc.save(f'Заява на відпустку {name} {datetime.datetime.now().strftime("%m.%d.%Y")}.docx')
    send_doc(f'Заява на відпустку {name} {datetime.datetime.now().strftime("%m.%d.%Y")}.docx',
             datetime.datetime.now().strftime("%m.%d.%Y"), name)
