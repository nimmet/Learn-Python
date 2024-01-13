
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
    pdf.add_page()
    filename = Path(filepath).stem
    invoice_nr, date = filename.split("-")

    pdf.set_font(family="Times", style="B", size=16)
    # pdf.set_text_color(100, 100, 100)
    pdf.cell(w=50, h=8,
             txt=f"Invoice nr. {invoice_nr}", ln=1)
    pdf.set_font(family="Times", style="B", size=16)
    # pdf.set_text_color(100, 100, 100)
    pdf.cell(w=50, h=8, txt=f"Date: {date}",ln=1)

        # Header
    columns = list(df.columns)
    columns = [name.replace("_"," ").title() for name in columns]


    pdf.set_font(family="Times", style="B", size=10)
    pdf.set_text_color(80, 80, 80)
    pdf.cell(w=30, h=8, txt=columns[0], border=1)
    pdf.cell(w=60, h=8, txt=columns[1], border=1)
    pdf.cell(w=40, h=8, txt=columns[2], border=1)
    pdf.cell(w=30, h=8, txt=columns[3], border=1)
    pdf.cell(w=30, h=8, txt=columns[4], border=1, ln=1)

    for index,row in df.iterrows():
        pdf.set_font(family="Times", size=10)
        pdf.set_text_color(80, 80, 80)



        # Cell Data
        pdf.cell(w=30, h=8, txt=str(row['product_id']), border=1)
        pdf.cell(w=60, h=8, txt=row["product_name"], border=1)

        pdf.cell(w=40, h=8, txt=str(row['amount_purchased']), border=1)
        pdf.cell(w=30, h=8, txt=str(row["price_per_unit"]), border=1)

        pdf.cell(w=30, h=8, txt=str(row['total_price']), border=1, ln=1)






        # pdf.cell(w=0, h=12,
        #          txt=str(row["product_id"])+"\t"+
        #          str(row["product_name"])+"\t"+str(row["amount_purchased"])+"\t"+str(row["price_per_unit"])+"\t"+
        #          str(row["total_price"]),
        #          align="L", ln=1, border=1)
        # # pdf.cell(w=0, h=12, txt=str(row["amount_purchased"]), align="L", ln=1, border=1)
        # # pdf.cell(w=0, h=12, txt=str(row["price_per_unit"]), align="L", ln=1, border=1)
        # # pdf.cell(w=0, h=12, txt=str(row["total_price"]), align="L", ln=1, border=1)
        # pdf.line(10, 22, 200, 22)


    pdf.output(f"pdfs/{filename}.pdf")

