from fpdf import FPDF
import pandas as pd
import pathlib
import glob

filepaths = glob.glob("Text+Files/*.txt")
pdf = FPDF(orientation="P", unit="mm", format="A4")


for filepath in filepaths:
    file_name = pathlib.Path(filepath).stem
    page_name = file_name.split(".")[0].title()

    pdf.add_page()

    pdf.set_auto_page_break(auto=False, margin=5)

    pdf.set_font(family="Times", style="B", size=20)
    pdf.set_text_color(120, 120, 120)
    pdf.cell(w=0, h=10, txt=page_name, align="L", ln=1)
    with open(filepath, "r") as file:
        pdf.set_font(family="Arial", size=10)
        read = file.readline()
        pdf.multi_cell(w=0, h=10, txt=read)
        file.close()

pdf.output("output.pdf")




