import os
import img2pdf


def get_images(folder):
    return [os.path.join(folder, im) for im in os.listdir(folder)]


def create_pdf(pdfname, img_folder):
    images = get_images(img_folder)
    with open(pdfname, 'wb+') as f:
        f.write(img2pdf.convert(images))


if __name__ == "__main__":
    create_pdf('final.pdf', 'images')
