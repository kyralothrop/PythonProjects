import datetime
from docx import Document
import os
from docx2pdf import convert

template_document = "template_document.docx"

#TODO: apply this to a use, add comments & clean code, ensure file name formatting properly - no dups/ overrite file

def main():
    todays_date = datetime.datetime.now()
    date = str(todays_date.year) + "-" + str(todays_date.month) + "-" + str(todays_date.day)

    print("\nFirst Name:")
    first_name = input()
    print("\nLast Name:")
    last_name = input()

    variables = {
        "${DATE}"         :   date,
        "${FIRST_NAME}"   :   first_name,
        "${LAST_NAME}"    :   last_name,
    }

    fill_template(variables)

def fill_template(variables):
    try:
        template_document = Document("template_document.docx")
    except:
        print("Issue getting template, exiting...")
        exit()

    for variable_key, variable_value in variables.items():
        for paragraph in template_document.paragraphs:
            replace_text_in_paragraph(paragraph, variable_key, variable_value)

    template_document.save("template_document" + str(1) + ".docx")

    # Uncomment the following line to convert the file to a pdf ____________
    #convert("template_document" + str(1) + ".docx")


def replace_text_in_paragraph(paragraph, key, value):
    if key in paragraph.text:
        inline = paragraph.runs
        for item in inline:
            if key in item.text:
                item.text = item.text.replace(key, value)

if __name__ == '__main__':
    main()