import pandas as pd
import glob

from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("text/*.txt")


pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

for filepath in filepaths:
    with open(filepath) as file:

        content =file.read()

        pdf.add_page()
        filename = Path(filepath).stem
        pdf.set_font(family="Times", style="B", size=16)
        # pdf.set_text_color(100, 100, 100)
        pdf.cell(w=50, h=8,
                 txt=f"{filename.capitalize()}", ln=1)

        # Add content to pdf file
        pdf.set_font(family="Times", style="", size=12)
        pdf.multi_cell(w=0, h=6, txt=content)

pdf.output(f"pdfs/animal.pdf")

