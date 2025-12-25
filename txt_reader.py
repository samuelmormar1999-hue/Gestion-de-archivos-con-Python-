with open ("datos_nba.txt", "r", encoding = "utf-8") as archivo:
    lines = archivo.readlines()
print (lines[:5])

header = lines [0].strip().split(",")
data = lines[1:]
print (header)
print (lines)

rows = [] #Creamos una variable para las celdas, en este caso filas vacías.

for line in data: #Aquí hemos creado un bucle para que python filtre los datos y nos devuelva aquellos que son válidos en forma de lista. For reccorre solo datos, no cabecera.
    values = line.strip().split (",") #El valor es una línea separa por comas.
    if len (values) == len(header): #Si tras recorrer la cadena los valores coinciden con la cabecera se le añade una celda.
        rows.append(values) #Solo se añaden filas válidas.
print (rows)


records = [] #Esta lista vacía contendrá los registros finales.

for row in rows:
    record = dict(zip(header, row)) #Dict convierte la información de zip es un diccionario. Zip empareja header (cabecera) con row (celda).
    records.append(record)

print (records[:3])

numeric_fields = ["points", "rebounds", "assists"]

for record in records:
    for field in numeric_fields:
        value = record[field]

        # Si ya es número, no hacemos nada
        if isinstance(value, (int, float)):
            continue

        # Si es string vacío o solo espacios
        if value.strip() == "":
            record[field] = None
        else:
            try:
                record[field] = float(value)
            except ValueError:
                record[field] = None
print(records[:3])
print(type(records[0]["points"]))


point_values = []

for records in records:
    if record ["points"] != None:
        point_values.append(records ["points"])
mean_points = sum(point_values) / len(point_values)
print (mean_points)