
import pandas as pd
import glob
from fpdf import FPDF
from pathlib import Path

filepaths = glob.glob("invoices/*.xlsx")


pdf = FPDF(orientation="P", unit="mm", format="A4")
pdf.set_auto_page_break(auto=False, margin=0)

total = 0.0;
for filepath in filepaths:
    df = pd.read_excel(filepath,sheet_name="Sheet 1")
    total_prices= df["total_price"].sum
    print(df)

    for index,row in df.iterrows():
        pdf.add_page()
        filename = Path(filepath).stem
        invoice_nr = filename.split("-")[0]
        pdf.set_font(family="Times", style="B", size=16)
        pdf.set_text_color(100, 100, 100)
        pdf.cell(w=50, h=8,
                 txt=f"Invoice nr. {invoice_nr}")
        # pdf.cell(w=0, h=12,
        #          txt=str(row["product_id"])+"\t"+
        #          str(row["product_name"])+"\t"+str(row["amount_purchased"])+"\t"+str(row["price_per_unit"])+"\t"+
        #          str(row["total_price"]),
        #          align="L", ln=1, border=1)
        # # pdf.cell(w=0, h=12, txt=str(row["amount_purchased"]), align="L", ln=1, border=1)
        # # pdf.cell(w=0, h=12, txt=str(row["price_per_unit"]), align="L", ln=1, border=1)
        # # pdf.cell(w=0, h=12, txt=str(row["total_price"]), align="L", ln=1, border=1)
        pdf.line(10, 22, 200, 22)


        pdf.output(f"pdfs/{filename}.pdf")

