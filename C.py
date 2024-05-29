def main():
    print("Se está ejecutando el módulo C")
    # Aquí coloca el código que deseas ejecutar en el módulo C

# Definimos la función 'gestionar_lista_compra' con 'accion' e 'item', el 'none' porque empieza con la Lista vacia
    def gestionar_lista_compra(accion, item=None):
        # Nombre del archivo
        archivo = 'lista_compra.txt'
    
        # Acción 'agregar'
        if accion == 'agregar':
            # Abrimos el archivo en modo de append/ajuntar ('a')
            with open(archivo, 'a') as f:
                # Escribimos el item
                f.write(item + '\n')
            # Ensenamos que el item fue agregado
            print(f'Item {item} agregado a la lista de la compra.')
        
        # Acción 'eliminar'
        elif accion == 'eliminar':
            # Abrimos el archivo en modo de lectura ('r') y leemos todas las líneas
            with open(archivo, 'r') as f:
                lines = f.readlines()
            # Abrimos el archivo en modo de escritura ('w'), lo que significa que el contenido existente del archivo se borrará
            with open(archivo, 'w') as f:
                # Escribimos todas las líneas en el archivo, excepto la que coincide con el item que se quiere eliminar
                for line in lines:
                    if line.strip("\n") != item:
                        f.write(line)
            # Ensenamos que el item fue eliminado
            print(f'Item {item} eliminado de la lista de la compra.')
        
        # Acción 'ver'
        elif accion == 'ver':
            # Abrimos el archivo en modo de lectura ('r') y leemos todas las líneas
            with open(archivo, 'r') as f:
                lines = f.readlines()
            # Ensenamos lista
            print('Lista de la compra:')
            for line in lines:
                print(line.strip("\n"))
            
        # Si la acción no es 'agregar', 'eliminar' ni 'ver'
        else:
            # No 
            print('Acción no reconocida. Las acciones posibles son: agregar, eliminar, ver.')

    # Aca puedes poner en accion las 3 herramientas Joan (qgregar, eliminar y ver)

    # Agregar
    gestionar_lista_compra('agregar', '[Aca el Item que tu quieras]')
    # Ver
    gestionar_lista_compra('ver')
    # Eliminar
    gestionar_lista_compra('elimnar', '[Aca el Item que tu quieras eliminar (que exista en la lista)]')