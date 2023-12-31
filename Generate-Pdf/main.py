import pandas
from fpdf import FPDF
import pandas as pd

df = pandas.read_csv("topics.csv")




pdf = FPDF(orientation="P", unit="mm", format="A4")

for index, row in df.iterrows():

    pdf.add_page()

    pdf.set_font(family="Times",style="B", size=24)
    pdf.set_text_color(100,100,100)
    pdf.cell(w=0,h=12, txt=str(row["Order"]), align="L", ln=1)
    pdf.line(10,22,200,22)
    pdf.cell(w=0,h=12, txt=row["Topic"], align="L", ln=1)
    pdf.line(10,34,200,34)
    pdf.cell(w=0,h=12, txt=str(row["Pages"]), align="L", ln=1)
    pdf.line(10,46,200,46)

pdf.output("output.pdf")