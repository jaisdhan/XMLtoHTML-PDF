"""
import pdfkit
# also wkhtmltopdf to install, to add in path envirionment variables

pdfkit.from_file('output.html', 'output.pdf')
"""

from weasyprint import HTML

def html_to_pdf(html_file, pdf_file):
    HTML(html_file).write_pdf(pdf_file)
    print(f"PDF successfullly generated in {pdf_file}")

if __name__ == "__main__":
    html_file = "output.html"
    pdf_file = "output.pdf"
    html_to_pdf(html_file, pdf_file)