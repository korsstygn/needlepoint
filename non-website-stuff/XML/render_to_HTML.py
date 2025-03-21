import os
from lxml import etree

def tei_to_html(tei_file, xsl_file, output_file):
    # Print the current working directory
    print("Current working directory:", os.getcwd())
    
    # List the files in the current directory
    print("Files in the current directory:", os.listdir())

    # Print the content of the TEI file
    with open(tei_file, 'r', encoding='UTF-8') as f:
        print("TEI file content preview:", f.read(500))

    # Parse the TEI and XSL files
    tei_doc = etree.parse(tei_file) 
    xsl_doc = etree.parse(xsl_file)  
    transform = etree.XSLT(xsl_doc)
    result = transform(tei_doc)

    # Write the transformation result to the output file
    with open(output_file, 'wb') as f:
        f.write(etree.tostring(result, pretty_print=True, encoding='UTF-8', xml_declaration=True))

if __name__ == "__main__":
    # Use absolute paths to the TEI and XSL files
    tei_file = "TEI_Encoded.XML"
    xsl_file = "stylesheet.xsl"
    output_file = "index.html"  

    tei_to_html(tei_file, xsl_file, output_file) 
