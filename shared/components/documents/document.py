import os
from docx.shared import Mm
from docxtpl import DocxTemplate, InlineImage
from path_utils import get_project_root

import datetime

from shared.components.mongo.mongo import send_doc

ROOT_DIR = get_project_root()
DOCUMENT_PATH = os.path.join(ROOT_DIR, 'resources/template/template_holiday/holiday_template.docx')
IMAGE_PATH = os.path.join(ROOT_DIR, 'resources/template/img/izgotovlenie-faksimile-300x300-2.png')
SAVE_FILLED_DOCS = os.path.join(ROOT_DIR, "resources/filled_docs")


def generate_document(date_start, date_end, name):
    doc = DocxTemplate(DOCUMENT_PATH)
    shtamp = InlineImage(doc, image_descriptor=IMAGE_PATH, width=Mm(40), height=Mm(40))
    date_start_split = date_start.split(".")
    date_end_split = date_end.split(".")

    datetime_conv_start = datetime.date(int(date_start_split[2]), int(date_start_split[1]), int(date_start_split[0]))
    datetime_conv_end = datetime.date(int(date_end_split[2]), int(date_end_split[1]), int(date_end_split[0]))

    delta = datetime_conv_end - datetime_conv_start
    days_count = delta.days
    days_word = ''

    if days_count is not None:
        if int(days_count) + 1 > 3 or not int(days_count) == 1:
            days_word = 'днів'
        elif int(days_count) + 1 % 10 == 2:
            days_word = 'дні'
        else:
            days_word = 'день'

    context = {
        'company_name': 'OATS',
        'person_name': f'{name}',
        'date_start': f'{date_start}',
        'date_end': f'{date_end}',
        'days_count': f'{int(days_count) + 1 if days_count is not None else "-"}',
        'days_word': f'{days_word}',
        'date': datetime.datetime.now().strftime("%m.%d.%Y"),
        'print': shtamp,
    }
    doc.render(context)
    new_file_path = os.path.join(SAVE_FILLED_DOCS,
                                 f'Заява на відпустку {name} {datetime.datetime.now().strftime("%m.%d.%Y")}.docx')
    doc.save(new_file_path)
    send_doc(new_file_path, datetime.datetime.now().strftime("%m.%d.%Y"), name)
    remove_file_after_fill(new_file_path)


def remove_file_after_fill(path):
    os.remove(path)


generate_document('20.01.2022', '22.02.2022', 'test')
