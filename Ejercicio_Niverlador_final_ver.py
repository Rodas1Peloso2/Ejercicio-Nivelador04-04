estudiantes = {    
    "Juan Pérez": {"edad": 17, "materias": ["Matemáticas", "Física"]},    
    "Ana Gómez": {"edad": 16, "materias": ["Química", "Historia"]},    
    "Pedro López": {"edad": 18, "materias": ["Biología", "Inglés"]}
    }
def agregar_estudiante():    
    nombre = input("Ingrese el nombre del estudiante: ")   
    edad = int(input("Ingrese la edad del estudiante: "))   
    materias = input("Ingrese las materias aprobadas separadas por coma: ").split(",")    
    estudiantes[nombre] = {"edad": edad, "materias": [materia.strip() for materia in materias]}   
    print(f"Estudiante {nombre} agregado con éxito.")

def mostrar_estudiante():
    if estudiantes:        
     for nombre, info in estudiantes.items():           
         print(f"\nNombre: {nombre}")            
         print(f"Edad: {info['edad']}")           
         print(f"Materias: {', '.join(info['materias'])}")   
    else:        
     print("No hay estudiantes registrados.")
     
def eliminar_estudiante():   
     nombre = input("Ingrese el nombre del estudiante a eliminar: ")   
     if nombre in estudiantes:       
         del estudiantes[nombre]       
         print(f"Estudiante {nombre} eliminado con éxito.")   
     else:        
      print(f"No se encontró al estudiante {nombre}.")

def buscar_estudiante():   
     nombre = input("Ingrese el nombre del estudiante a buscar: ")   
     if nombre in estudiantes:       
         info = estudiantes[nombre]       
         print(f"\nNombre: {nombre}")        
         print(f"Edad: {info['edad']}")      
         print(f"Materias: {', '.join(info['materias'])}")   
     else:       
         print(f"No se encontró al estudiante {nombre}.")

def buscar_por_palabra_clave():    
    palabra = input("Ingrese la palabra clave para buscar: ").lower()    
    encontrados = False    
    for nombre in estudiantes:       
         if palabra in nombre.lower():            
            print(f"\nNombre: {nombre}")          
            info = estudiantes[nombre]           
            print(f"Edad: {info['edad']}")
            print(f"Materias: {', '.join(info['materias'])}")          
            encontrados = True    
    if not encontrados:       
            print("No se encontró ningún estudiante con esa palabra clave.")

def menu():   
     while True:       
         print("\n--- Menú ---")       
         print("1. Agregar nuevo estudiante")        
         print("2. Mostrar lista de estudiantes")        
         print("3. Eliminar estudiante")       
         print("4. Buscar estudiante por nombre")   
         print("5. Buscar estudiantes por palabra clave en el nombre")   
         print("6. Salir")                
         opcion = input("Elija una opción (1-6): ")
         match opcion:            
             case "1":              
                 agregar_estudiante()           
             case "2":                
                 mostrar_estudiante()            
             case "3":               
                 eliminar_estudiante()           
             case "4":                
                 buscar_estudiante()            
             case "5":                
                 buscar_por_palabra_clave()           
             case "6":                
                 print("Saliendo del programa...")                
                 break            
             case _:                
                 print("Opción no válida. Por favor, elija entre 1 y 6.")   

menu()