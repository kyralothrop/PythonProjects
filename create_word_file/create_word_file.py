import datetime
from docx import Document
import os
from docx2pdf import convert

template_document = "template_document.docx"

def main():
    """
        template_document contains the base word document with some placeholders for personalized information that will be populated in the newly created document with the information provided by the user.
    """

    todays_date = datetime.datetime.now()
    date = str(todays_date.year) + "-" + str(todays_date.month) + "-" + str(todays_date.day)

    print("\nFirst Name:")
    first_name = input()
    print("\nLast Name:")
    last_name = input()
    print("\nEvent Name:")
    event_name = input()
    print("\nEvent Location:")
    event_location = input()
    print("\nEvent Date:")
    event_date = input()
    print("\nEvent Time:")
    event_time = input()
    print("\nAuthor:")
    author = input()

    variables = {
        "${DATE}"           :   date,
        "${FIRST_NAME}"     :   first_name,
        "${LAST_NAME}"      :   last_name,
        "${EVENT_NAME}"     :   event_name,
        "${EVENT_LOCATION}" :   event_location,
        "${EVENT_DATE}"     :   event_date,
        "${EVENT_TIME}"     :   event_time,
        "${AUTHOR}"         :   author
    }

    copy_file_name = first_name + last_name + ".docx"
    fill_template(variables, copy_file_name)

def fill_template(variables, copy_file_name):
    """
        Creates a new docx document and a pdf file from template_document with the new variable values.

        Parameters:
            variables (dictionary): word document placeholder and the associated variable for the new value
            copy_file_name (str): filename for the new file
    """
    try:
        template_document = Document("template_document.docx")
    except:
        print("Issue getting template, exiting...")
        exit()

    for variable_key, variable_value in variables.items():
        for paragraph in template_document.paragraphs:
            replace_text_in_paragraph(paragraph, variable_key, variable_value)

    if copy_file_name in os.listdir():
        print("Error a file with the name " + copy_file_name + "already exists, exiting...")
        exit()
    else:
        template_document.save(copy_file_name)

    convert(copy_file_name)


def replace_text_in_paragraph(paragraph, key, value):
    """
        Replaces the placeholders in template_document with the new given value.
        
        Parameters:
            paragraph (str): paragraph in the template to review
            key (str): placeholder
            value (str): new value for the placeholder
    """
    if key in paragraph.text:
        inline = paragraph.runs
        for item in inline:
            if key in item.text:
                item.text = item.text.replace(key, value)

if __name__ == '__main__':
    main()