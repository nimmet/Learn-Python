
import pandas as pd
from fpdf import FPDF

df = pd.read_excel("Invoice-Generation/invoices/10001-2023.1.18.xlsx")

pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)


for index, row in df:
    print(row)
