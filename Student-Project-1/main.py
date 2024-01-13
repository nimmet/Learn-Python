import pandas as pd
import glob

from click import style
from fpdf import FPDF
from pathlib import Path
import re

filepaths = glob.glob("text/*.txt")


pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

pattern = "\\[\d\\]*"

for filepath in filepaths:
    with open(filepath) as file:
        # content = file.readline().split("[\\d]{1,2}")
        content  = re.split(pattern, file.readline())

        print(content)

        pdf.add_page()
        filename = Path(filepath).stem
        pdf.set_font(family="Times", style="B", size=16)
        # pdf.set_text_color(100, 100, 100)
        pdf.cell(w=50, h=8,
                 txt=f"{filename.capitalize()}", ln=1)



        yy=25
        for c in content:
            pdf.set_font(family="Times", style="", size=12)
            # pdf.text(txt=c.strip(),y=yy,x=10)
            # yy += 10
            pdf.multi_cell(w=0, h=6, txt=c)

        # pdf.cell(w=0, h=12,
        #          txt=str(row["product_id"])+"\t"+
        #          str(row["product_name"])+"\t"+str(row["amount_purchased"])+"\t"+str(row["price_per_unit"])+"\t"+
        #          str(row["total_price"]),
        #          align="L", ln=1, border=1)
        # # pdf.cell(w=0, h=12, txt=str(row["amount_purchased"]), align="L", ln=1, border=1)
        # # pdf.cell(w=0, h=12, txt=str(row["price_per_unit"]), align="L", ln=1, border=1)
        # # pdf.cell(w=0, h=12, txt=str(row["total_price"]), align="L", ln=1, border=1)
        # pdf.line(10, 22, 200, 22)


pdf.output(f"pdfs/animal.pdf")

