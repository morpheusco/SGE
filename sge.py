# Sistema de Gestión de Estudiantes (SGE) básico
# Edison Monsalve | ALGORITMOS Y PROGRAMACIÓN
#
# El programa permite agregar hasta cinco estudiantes, mostrar la lista
# y buscar una ficha por su ID. La lista se crea vacía cada vez que se abre
# el programa y los datos se pierden al salir.
#
# Primero están las funciones que usa el menú. Al final está main(),
# que muestra las opciones y controla cuándo termina el programa.
#
# Ejemplo: para DVV007, las notas 4.0, 5.0 y 4.5 dan una nota final
# de 4.50 con pesos de 30 %, 30 % y 40 %.


# Esta búsqueda sirve para consultar una ficha y para revisar IDs repetidos.
def buscar_estudiante(estudiantes, identificacion):
    for estudiante in estudiantes:
        if estudiante["id"] == identificacion:
            # El ID es único, así que podemos dejar de buscar al encontrarlo.
            return estudiante
    # None indica que recorrimos toda la lista sin encontrar el ID.
    return None


# Uso la misma forma de mostrar la ficha en el listado y en la búsqueda.
def mostrar_estudiante(estudiante):
    print(f"\nID: {estudiante['id']}")
    print(f"Nombre: {estudiante['nombre']}")
    print(f"Edad: {estudiante['edad']}")
    print(f"Carrera: {estudiante['carrera']}")
    nota1, nota2, nota3 = estudiante["notas"]

    # Nota para mí
    # En esa notación {nota1:.2f} al principio no me salía, pero en la documentación y lo que salía con IA parecía que si, 
    # finalmente parecía que tuve un error con espacios o algo.
    print(f"Notas (30 %, 30 %, 40 %): {nota1:.2f}, {nota2:.2f}, {nota3:.2f}")
    print(f"Nota final: {estudiante['nota_final']:.2f}")


def agregar_estudiante(estudiantes, contador):
    # Reviso el cupo antes de pedir los datos para evitar escribir una
    # ficha que no se puede guardar.
    if contador >= 5:
        print("Se alcanzó el cupo de 5 estudiantes.")
        return

    # strip() quita los espacios de los extremos. upper() hace que
    # Voy a usar esas funciones para mejorar el tema
    # "dvv007" y "DVV007" se comparen como el mismo ID.
    identificacion = input("ID del estudiante: ").strip().upper()
    if not identificacion.isalnum():
        print("El ID debe contener solo letras o números.")
        return
    if buscar_estudiante(estudiantes, identificacion) is not None:
        print("El ID ya está registrado.")
        return

    # Al quitar los espacios de los extremos, un nombre que contiene
    # solo espacios también queda vacío.
    nombre = input("Nombre completo: ").strip()
    carrera = input("Carrera: ").strip()
    if not nombre or not carrera:
        print("El nombre y la carrera son obligatorios.")
        return

    # input() entrega texto. Si int() no puede convertirlo, except
    # muestra el aviso y return devuelve el control al menú.
    try:
        edad = int(input("Edad: "))
    except ValueError:
        print("La edad debe ser un número entero.")
        return
    if not 15 <= edad <= 90:
        print("La edad debe estar entre 15 y 90 años.")
        return

    # Pido las tres notas con un ciclo porque todas tienen el mismo rango.
    # Si alguna falla, todavía no se ha guardado la ficha del estudiante.
    notas = []
    for numero in range(1, 4):
        try:
            # Acepto tanto 4,5 como 4.5 para escribir un decimal.
            nota = float(input(f"Nota {numero}: ").replace(",", "."))
        except ValueError:
            print("La nota debe ser numérica.")
            return
        if not 0 <= nota <= 5:
            print("La nota debe estar entre 0.0 y 5.0.")
            return
        notas.append(nota)

    # Multiplico cada nota por su peso en decimal y sumo los resultados.
    # La tercera nota tiene más peso porque vale el 40 %.
    nota_final = notas[0] * 0.30 + notas[1] * 0.30 + notas[2] * 0.40

    # Guardo todos los datos en un diccionario para que cada estudiante
    # tenga su propia ficha. Solo la agrego cuando los datos son válidos.
    estudiantes.append({
        "id": identificacion,
        "nombre": nombre,
        "edad": edad,
        "carrera": carrera,
        "notas": notas,
        "nota_final": nota_final,
    })
    print("Estudiante registrado.")


def main():
    estudiantes = []
    contador = 0
    salir = False

    # La bandera empieza en False para mostrar el menú al menos una vez.
    # Cuando cambia a True, el while termina al revisar su condición.
    while not salir:
        print("\nSistema de Gestión de Estudiantes")
        print(f"Estudiantes registrados: {contador}/5")
        print("1. Agregar estudiante")
        print("2. Mostrar todos")
        print("3. Buscar por ID")
        print("4. Salir")
        opcion = input("Opción: ").strip()

        # input() devuelve texto, por eso las opciones se comparan con
        # "1", "2", "3" y "4". case _ recibe cualquier otra entrada.
        match opcion:
            case "1":
                agregar_estudiante(estudiantes, contador)
                # Si agregar falla, la lista sigue igual. Al consultar su
                # tamaño, el contador solo refleja las fichas guardadas.
                contador = len(estudiantes)
            case "2":
                if contador == 0:
                    print("No hay estudiantes registrados.")
                else:
                    for estudiante in estudiantes:
                        mostrar_estudiante(estudiante)
            case "3":
                # Aplico el mismo formato que al guardar el ID para poder
                # encontrarlo aunque el usuario escriba en minúsculas.
                identificacion = input("ID que desea buscar: ").strip().upper()
                estudiante = buscar_estudiante(estudiantes, identificacion)
                if estudiante is None:
                    print("No se encontró el ID.")
                else:
                    mostrar_estudiante(estudiante)
            case "4":
                print("Programa finalizado.")
                salir = True
            case _:
                print("Opción inválida.")


# Este bloque arranca el menú al ejecutar el archivo directamente.
if __name__ == "__main__":
    main()
