from PyPDF2 import PdfFileReader, PdfFileWriter

def extract_information(pdf_path):
    with open(pdf_path, 'rb') as f:
        pdf = PdfFileReader(f)
        information = pdf.getDocumentInfo()
        number_of_pages = pdf.getNumPages()

    txt =f"""
    Information about {pdf_path}
    Author: {information.author}
    Creator: {information.creator}
    Producer: {information.producer}
    Subject: {information.subject}
    Title: {information.title}
    Number of pages: {number_of_pages}
    """

    print(txt)
    return information

def page_size_dict_func(path):
    pdf = PdfFileReader(open(path, 'rb'))
    number_of_pages = pdf.getNumPages()
    page_dim_dict = {}
    page_size_dict = {}
    for num in range(number_of_pages):
        page_height = int(float(pdf.getPage(num).mediaBox.getHeight())*0.352)
        page_width = int(float(pdf.getPage(num).mediaBox.getWidth())*0.352)
        page_dim_dict[num] = [int(float(pdf.getPage(num).mediaBox.getHeight())*0.352),
                              int(float(pdf.getPage(num).mediaBox.getWidth())*0.352)]
        if page_height <= 298 and page_width <= 210:
            try:
                page_size_dict["A4"].append(num+1)
            except KeyError:
                page_size_dict["A4"]  = [num+1]
        elif page_height <= 298 and page_width <= 420:
            try:
                page_size_dict["A3"].append(num+1)
            except KeyError:
                page_size_dict["A3"]  = [num+1]
        elif page_height <= 297:
            try:
                page_size_dict["297"].append(num+1)
            except KeyError:
                page_size_dict["297"]  = [num+1]
        elif page_height <= 420:
            try:
                page_size_dict["420"].append(num+1)
            except KeyError:
                page_size_dict["420"]  = [num+1]
        elif page_height <= 610:
            try:
                page_size_dict["610"].append(num+1)
            except KeyError:
                page_size_dict["610"]  = [num+1]
        else:
            try:
                page_size_dict["big"].append(num+1)
            except KeyError:
                page_size_dict["big"]  = [num+1]

    return page_size_dict

def split(path, name_of_split):
    pdf = PdfFileReader(path)
    for page in range(pdf.getNumPages()):
        pdf_writer = PdfFileWriter()
        pdf_writer.addPage(pdf.getPage(page))

        output = f'{name_of_split}{page}.pdf'
        with open(output,'wb') as output_pdf:
            pdf_writer.write(output_pdf)

def split_pages(path, page_size_dict):
    pdf = PdfFileReader(path)
    for key in page_size_dict:
        print(f"{key}:{page_size_dict[key]}")
        pdf_writer = PdfFileWriter()
        for page_num in page_size_dict[key]:
            pdf_writer.addPage(pdf.getPage(page_num-1))
            filename = path.split("\\")[-1][:-4]
            output = f'{filename}_{key}.pdf'
            with open(output, 'wb') as output_pdf:
                pdf_writer.write(output_pdf)


if __name__ == '__main__':
    path = r'D:\SONY\Nauka\Python\11.Projekty\01.PDF_Program\LTS.135013A.MONAN-KS 1T-07-a Launching Station 01-TD 2020-06-10.pdf'
    extract_information(path)

    print(page_size_dict_func(path))

    split_pages(path, page_size_dict_func(path))

    filename = path.split("\\")[-1][:-4]
    print(filename)