import csv
import json
import xml.etree.ElementTree as ET
from inventory_report.reports.complete_report import CompleteReport
from inventory_report.reports.simple_report import SimpleReport

# https://www.guru99.com/manipulating-xml-with-python.html
# parse to xml by element tree


class Inventory:
    @classmethod
    def xml_parsed_file(cls, path):
        data = []
        tree = ET.parse(path)
        root = tree.getroot()
        for el in root:
            pspsps = {}
            for item in el:
                pspsps[item.tag] = item.text
            data.append(pspsps)
        return data

    @classmethod
    def parse_file(cls, path):
        def extend(extension):
            return path.endswith(extension)

        with open(path, "r") as f:
            if extend(".csv"):
                data = list(csv.DictReader(f))
            if extend(".json"):
                data = json.load(f)
            if extend(".xml"):
                data = cls.xml_parsed_file(f)
        return data

    @classmethod
    def import_data(cls, path, type):
        data = cls.parse_file(path)
        if type == "simples":
            return SimpleReport.generate(data)
        if type == "completo":
            return CompleteReport.generate(data)
