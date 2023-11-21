
# drop table if exists empleado;
# create table empleado(
# 	nombre varchar(50) not null,
# 	edad integer not null,
# 	jefe varchar(50)
# );

# insert into empleado('nombre', 'edad', 'jefe') values
# ("marta",22,"andres"),
# ("andres",35,"juan"),
# ("diego",33,"juan"),
# ("juan",45,NULL);

# select * from empleado;

empleado = [
    ["nombre","edad","jefe"],
    ["marta",22,"andres"],
    ["andres",32,"juan"],
    ["diego",33,"juan"],
    ["juan",45,None]
]

def isSet(lista):
    return len(lista) == len(set(lista))

def isValid(tablaRelacional):
    header = tablaRelacional[0]
    if not isSet(header):
        return False
    length = len(header)
    for row in tablaRelacional[1:]:
        if len(row) != length:
            return False
    return True

def posiciones(Lista, sublista):
    resultado = []
    for item in sublista:
        if item in Lista:
            pass  # append(),,, index()...
    return resultado

if __name__ == "__main__":

    # print(isSet([11,22,33]))     # True
    # print(isSet([11,22,11,33]))  # False    
    # print(isSet([11]))           # True
    # print(isSet([]))             # True

    print(isValid(empleado))
    print(empleado) ## todo bonito con tabla markdown

    print(posiciones(empleado[0],["nombre","edad","jefe"]))
    print(posiciones(empleado[0],["nombre","jefe"]))    
    print(posiciones(empleado[0],["edad","jefe"]))    
    print(posiciones(empleado[0],["jefe", "nombre"]))    
    print(posiciones(empleado[0],["nombre"]))    
    print(posiciones(empleado[0],[]))    


    # print(select(empleado,["edad"]) 
    # print(select(empleado,["jefe"])           
    # print(select(empleado,["jefe, edad"])
          
