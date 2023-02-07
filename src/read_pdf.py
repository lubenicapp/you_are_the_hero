import PyPDF2


def pdf_to_raw_text(source_file, dest_file):
    reader = PyPDF2.PdfReader(open(source_file, "rb"))
    page_count = len(reader.pages)

    content = ''

    for page in reader.pages:
        text = page.extract_text()
        content += text

    with open(dest_file, 'w') as file:
        file.write(content)
