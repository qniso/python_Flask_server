import requests
from docx.shared import Mm
from docxtpl import DocxTemplate, InlineImage

import datetime
from datetime import timedelta


def generate_document_to_holiday(operation, data, message, bot):
    if(operation == "holiday"):
        date_start = data["date_start"]
        date_end = data["date_end"]
        full_name = data['userName']
        days_count = '-'
        a = ''
        doc = DocxTemplate('shared/components/documents/template/template_holiday/holiday_template.docx')
        shtamp = InlineImage(doc, image_descriptor='shared/components/documents/template/img/izgotovlenie-faksimile-300x300-2.png', width=Mm(40), height=Mm(40))
        datetime_conv_start = datetime.date(int(date_start.split(".")[2]), int(date_start.split(".")[1]), int(date_start.split(".")[0]))
        datetime_conv_end = datetime.date(int(date_end.split(".")[2]), int(date_end.split(".")[1]),int(date_end.split(".")[0]))

        delta = datetime_conv_end - datetime_conv_start
        for i in range(delta.days + 1):
            day = datetime_conv_start + timedelta(days=i)
            days_count = str(delta.days)
        print(int(days_count))
        if (int(days_count) + 1 > 3 or not int(days_count) == 1):
            a = 'днів'
        elif(int(days_count) + 1 % 10 == 2):
            a = 'дні'
        else:
            a = 'день'

        context = {'company_name': 'OATS',
                   'person_name': f'{full_name}',
                   'date_start': f'{date_start}',
                   'date_end': f'{date_end}',
                   'days_count': f'{int(days_count)+1}',
                   'days_word' : f'{a}',
                   'date': datetime.datetime.now().strftime("%m.%d.%Y"),
                   'print': shtamp,
                    }
        print(a)
        print(int(days_count)+1 % 10 == 2)
        doc.render(context)
        doc.save(f'Заява на відпустку {full_name} {datetime.datetime.now().strftime("%m.%d.%Y")}.docx')
        # send_doc(f'Заява на відпустку {full_name} {datetime.datetime.now().strftime("%m.%d.%Y")}.docx', datetime.datetime.now().strftime("%m.%d.%Y"), full_name)

        bot.send_message(message.chat.id, "Ваш документ на відпустку сформований, якщо зʼявляються питання щодо документу, то скористуйтеся командою /send_report, щоб оповістити адміна про помилку")

        url = f'https://api.telegram.org/bot5747097442:AAFaW6N9A1Q3L5pfdb6fYlQ9OZ9IaSgA6hI/'
        method = url + 'sendDocument'

        with open(f'Заява на відпустку {full_name} {datetime.datetime.now().strftime("%m.%d.%Y")}.docx', "rb") as file:
            files = {"document": file}
            title = f"Ваш документ на відпустку"
            chat_id = message.chat.id
            r = requests.post(method, data={"chat_id": chat_id, "caption": title}, files=files)
            if r.status_code != 200:
                raise Exception("send error")
