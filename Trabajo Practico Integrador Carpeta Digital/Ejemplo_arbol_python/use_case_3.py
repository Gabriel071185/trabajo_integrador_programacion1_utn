from arbol import  mostrar_arbol,insertar


if __name__ == "__main__":
    # Ejecutar el caso de uso
    # Crear un árbol binario de ejemplo
    arbol= insertar(None,100 )
    insertar(arbol,80)
    insertar(arbol,150)
    insertar(arbol,25)
    insertar(arbol,75)
    insertar(arbol,125)
    insertar(arbol,175)
    

    mostrar_arbol(arbol)
