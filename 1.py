#! /usr/bin/phthon3

from isSet import isSet
# from indexes import indexes
from py_markdown_table.markdown_table import markdown_table


class tablaRelacional:

    def __init__(self, rawList):
        if not self.isValid(rawList):
            return None
        self.schema = rawList[0]
        self.rows = rawList[1:]

    def isValid(self, tablaRelacional):
        """estado valido de una tabla:
                los metadatos son un set AND
                todo dato tiene la cantidad de elementos correcta
                    (la longitud de los metadatos)
        """
        header = tablaRelacional[0]
        if not isSet(header):
            return False
        length = len(header)
        for row in tablaRelacional[1:]:
            if len(row) != length:
                return False
        return True

    def basicJsonFormat(self):
        """fmt as list of dicts"""
        dd = []
        for r in self.rows:
            dd.append(dict(zip(self.schema, r)))
        return dd

    def __str__(self):
        """nice MD format:
        https://pypi.org/project/py-markdown-table/
        """
        return markdown_table(self.basicJsonFormat()).get_markdown()


if __name__ == "__main__":

    # relational schema + population as rawList
    emp = [
        ["nombre", "edad", "jefe"],
        ["marta", 22, "andres"],
        ["andres", 32, "juan"],
        ["diego", 33, "juan"],
        ["juan", 45, None]
    ]

    tr = tablaRelacional(emp)
    print(tr)
    print(tr.basicJsonFormat())

    # print(select(emp,["edad"])
    # print(select(emp,["jefe"])
    # print(select(emp,["jefe, edad"])
