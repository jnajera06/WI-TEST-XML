# pip install --upgrade lxml

import lxml.etree
tree = lxml.etree.parse('example.xml')

for i in tree.xpath('//ASSESSMENTS'):
    print(i)