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

    empSchema = ["nombre", "edad", "jefe"]

    print(indexes(empSchema, ["nombre", "edad", "jefe"]))
    print(indexes(empSchema, ["nombre", "jefe"]))
    print(indexes(empSchema, ["edad", "jefe"]))
    print(indexes(empSchema, ["jefe", "nombre"]))
    print(indexes(empSchema, ["jefe", "nombre", "jefe",]))      
    print(indexes(empSchema, ["nombre"]))
    print(indexes(empSchema, []))

