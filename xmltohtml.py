# To create a script to read xml and convert to HTML
import xml.etree.ElementTree as ET
from xml.etree.ElementTree import Element, SubElement

"""
tree = ET.parse('test.xml')
root = tree.getroot()
print(root.tag)
print(root.attrib)
"""
def xml_to_html(xml_file, html_file):
    # Parse the XML file
    tree = ET.parse(xml_file)
    root = tree.getroot()

    # Create HTML root element
    html_root = Element('html')
    body = SubElement(html_root, 'body')

    title_in_xml= root.find("title")
    title = SubElement(body, 'h1')
    title.text = title_in_xml.text


    SubElement(title, 'br')

    # Convert XML elements to HTML
    for food in root.findall('food'):
        food_div = SubElement(body, 'div')

        abreak = SubElement(food_div, 'br')

        name = SubElement(food_div, 'p')
        name.text = f"Name: {food.find('name').text}"

        price = SubElement(food_div, 'p')
        price.text=f"Price: {food.find('price').text}"

        description = SubElement(food_div, 'p')
        description.text = f"Description: {food.find('description').text}"

        calories = SubElement(food_div, 'p')
        calories.text = f"Calories: {food.find('calories').text}"

    #Create and write the HTML file
    html_tree = ET.ElementTree(html_root)
    with open(html_file, 'wb') as html_output:
        html_tree.write(html_output)

if __name__ == "__main__":
    xml_file = "test.xml"
    html_file = "output.html"

    xml_to_html(xml_file, html_file)
    print(f"Conversion completed. HTML file saved as {html_file}.")