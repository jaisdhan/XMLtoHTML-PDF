import os
import pytest
from xmltohtml import xml_to_html
from xmltopdf import html_to_pdf

# File paths
XML_FILE = 'test.xml'
HTML_OUTPUT = 'output.html'
PDF_OUTPUT = 'output.pdf'

#PRUEBAS DE VALIDACION DEL XML
"""
def test_validate_xml():
    To verify that the XML exists and it is valid
    assert os.path.exists(XML_) """