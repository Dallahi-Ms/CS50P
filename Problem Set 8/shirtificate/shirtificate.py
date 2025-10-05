from fpdf import FPDF

name = input("Name: ").strip()

pdf = FPDF("P", "mm", "A4")
pdf.add_page("portrait")
pdf.image("shirtificate.png", x=10, y=70, w=190)
pdf.set_font("Arial", size=45)
pdf.cell(0, 0, "CS50 Shirtificate", ln=True, align='C')
pdf.set_font("helvetica", "B", 25)
pdf.set_text_color(255, 255, 255)
pdf.cell(0, 240, f"{name} took CS50", ln=1, align="C")

pdf.output("shirtificate.pdf")

