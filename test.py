'''Este algoritmo permite administar el stock de la tienda'''
import os

print('*'*20)
print('STOCK'.center(20, '*'))
print('*'*20)
productos = {'harina': 10, 'huevos': 30, 'escoba':15, 'jugo de naranja': 7}
menup = ['Ver Productos', 'Agregar Producto', 'Eliminar Producto', 'Salir']
while True:
    for ind in range(len(menup)):
        print(f'{ind+1}. {menup[ind]}')
    ans= input('¿Qué quieres hacer?:\n')
    if ans== '1':
        os.system('cls')
        for a, b in productos.items():
            print(f'{a.center(20, ' ')}: {b}')
        print()
    elif ans== '2':
        os.system('cls')
        while True:
            nom= input('Indice el nombre del producto a agregar:\n')
            if nom.replace(' ', '').isalpha():
                break
        if nom.lower() in productos:
            os.system('cls')
            print('Error: El producto ya existe\n')
            continue
        else:
            os.system('cls')
            productos[nom.lower()] = 0
            print('Producto agregado exitosamente!\n')
    elif ans== '3':
        os.system('cls')
        while True:
            nom= input('Indice el nombre del producto a eliminar:\n')
            if nom.replace(' ', '').isalpha():
                break
        if nom.lower() in productos:
            os.system('cls')
            del productos[nom.lower()]
            print('Producto borrado existosamente!\n')
        else:
            os.system('cls')
            print('Error: el producto no existe\n')
    elif ans== '4':
        os.system('cls')
        exit('Adios!')
    else:
        os.system('cls')
        print('Error: opción inválida\n')

