import csv

columns = ['descripcion','monto','categoria']

#crear archivo csv o escribir si ya existe
with open('gastos.csv', 'a', newline='') as file:
    writer = csv.DictWriter(file, fieldnames=columns)
    
    #escribir encabezado si el archivo está vacío
    file.seek(0,2) #mover el cursor al final del archivo
    if file.tell() == 0: #verificar si el archivo está vacío
        writer.writeheader()
    
    #pedir datos al usuario
    descripcion = input("Ingrese la descripción del gasto: ")
    monto = input("Ingrese el monto del gasto: ")
    categoria = input("Ingrese la categoría del gasto: ")
    
    #escribir los datos en el archivo
    writer.writerow({'descripcion': descripcion, 'monto': monto, 'categoria': categoria})
    print("Gasto registrado exitosamente.")

#leer y mostrar los datos del archivo
with open('gastos.csv', 'r') as file:
    reader = csv.DictReader(file)
    print("\nGastos registrados:")
    for row in reader:
        print(f"Descripción: {row['descripcion']}, Monto: {row['monto']}, Categoría: {row['categoria']}")

#calcular y mostrar el total de gastos
total = 0
with open('gastos.csv', 'r') as file:
    reader = csv.DictReader(file)
    for row in reader:
        total += float(row['monto'])
print(f"\nTotal de gastos: {total}")
