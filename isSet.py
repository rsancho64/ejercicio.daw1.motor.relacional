def isSet(lista):
    return len(lista) == len(set(lista))


if __name__ == "__main__":

    print(isSet([11, 22, 33]))     # True
    print(isSet([11, 22, 11, 33]))  # False
    print(isSet([11]))           # True
    print(isSet([]))             # True
