import json
import xmltodict
import xml.etree.ElementTree as ET

with open("file.xml") as f:
    d = f.read()
    tree2 = ET.fromstring(d)
    dict_data = xmltodict.parse(d)
    json_data = json.dumps(dict_data)
    with open("file.json", "w+") as new_f:
        new_f.write(json_data)