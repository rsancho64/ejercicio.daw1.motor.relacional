from isSet import isSet

def isValid(tablaRelacional):
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

def indexes(Lista, sublista):
    """lista de los indices de posicion 
        de los datos de una sublista 
        en una Lista (busca items de sublista en Lista)"""
    resultado = []
    for item in sublista:
        if item in Lista:
            resultado.append(Lista.index(item))
    return resultado

if __name__ == "__main__":

    emp = [
        ["nombre", "edad", "jefe"],
        ["marta", 22, "andres"],
        ["andres", 32, "juan"],
        ["diego", 33, "juan"],
        ["juan", 45, None]
    ]

    print(isValid(emp))
    print(emp)  # TODO: bonito con tabla markdown

    print(indexes(emp[0], ["nombre", "edad", "jefe"]))
    print(indexes(emp[0], ["nombre", "jefe"]))
    print(indexes(emp[0], ["edad", "jefe"]))
    print(indexes(emp[0], ["jefe", "nombre"]))
    print(indexes(emp[0], ["jefe", "nombre", "jefe",]))      
    print(indexes(emp[0], ["nombre"]))
    print(indexes(emp[0], []))

    # print(select(emp,["edad"])
    # print(select(emp,["jefe"])
    # print(select(emp,["jefe, edad"])
