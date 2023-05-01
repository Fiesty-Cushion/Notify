import requests
import pdf2image
import os


def create_files(url, filename):
    response = requests.get(url)
    with open(f"docs/{filename}", 'wb') as pdf:
        pdf.write(response.content)
    pdf.close()
    images = pdf2image.convert_from_path(f"docs/{filename}", poppler_path=r"poppler\Library\bin")
    for i in range(len(images)):   
         images[i].save('images/'+'page'+ str(i) +'.jpg', 'JPEG')



def del_files():
    imgDirectory = os.fsencode("images")
    for file in os.listdir(imgDirectory):
        filename = os.fsdecode(file)
        path = f"images/{filename}"
        os.remove(path)

    docsDirectory = os.fsencode("docs")
    for file in os.listdir(docsDirectory):
        filename = os.fsdecode(file)
        path = f"docs/{filename}"
        os.remove(path)