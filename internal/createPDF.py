from fpdf import FPDF

def createPDF(image_filename, text, output_filename):
    A4_WIDTH = 210.0 #mm
    A4_HEIGHT = 297.0
    A4_HALF_HEIGHT = A4_HEIGHT / 2.0
    IMAGE_SIZE = A4_HALF_HEIGHT * 0.8
    FONT_SIZE = 16

    pdf = FPDF(format = 'A4')
    pdf.add_page()

    # add image on top half
    pdf.set_xy( (A4_WIDTH - IMAGE_SIZE) / 2.0,
                (A4_HALF_HEIGHT - IMAGE_SIZE) / 2.0)
    pdf.image(image_filename, link = '', type = '', w = IMAGE_SIZE, h = IMAGE_SIZE)

    # add text on bottom half
    pdf.set_xy(A4_WIDTH * 0.05, A4_HALF_HEIGHT)
    pdf.set_font('Courier', '', FONT_SIZE)
    pdf.multi_cell(w=A4_WIDTH*0.9, h=10, align='C', txt=format_hex_text(text))

    # save to file
    pdf.output(output_filename,'F')

def format_hex_text(text):
    output = ''
    chars_per_block = 4
    blocks_per_line = 10
    i = 0
    while i*chars_per_block < len(text):
        output += text[i*chars_per_block:(i+1)*chars_per_block] + ' '
        i += 1
        if i % blocks_per_line == 0:
            output += '\n'

    return output
