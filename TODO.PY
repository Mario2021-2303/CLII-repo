import json
import os
from datetime import date
import argparse
import sys

def cargar_datos():
    ruta_archivo = "tarea.json"
    
    if os.path.exists(ruta_archivo):
        with open(ruta_archivo, "r") as f:
            lista_tareas = json.load(f)
    else:
        lista_tareas = []
    
    return lista_tareas, ruta_archivo


def guardar_tareas(lista_tareas, ruta_archivo):
    with open(ruta_archivo, "w") as f:
        json.dump(lista_tareas, f, indent=4)


def crear_tarea():
    lista_tareas, ruta_archivo = cargar_datos()
 
    nombre = input("Ingresa tu nombre por favor: ")
    descripcion = input("¿De qué va la tarea?: ")

    nuevo_id = max([t["id"] for t in lista_tareas], default=0) + 1

    id_estado = int(input("Estado de la TAREA:\n" 
                    "1.TERMINADO\n"
                    "2.EN PROGRESO\n"
                    "3.SIN TERMINAR"))
    
    
        
    if id_estado == 1:
           estado = "Terminado"
    elif id_estado == 2:
           estado = "En progreso"
    elif id_estado == 3:
           estado = "Sin terminar"
    else: 
        
        print("ESTADO NO EXISTENTE")
        return
        
    today = str(date.today())

    
  
    tarea = {
        "id": nuevo_id,
        "nombre": nombre,
        "descripcion": descripcion,
        "estado": estado,
        "fecha": today,
        "modificado": ""
    }

    lista_tareas.append(tarea)

    guardar_tareas(lista_tareas, ruta_archivo)

def borrar_tarea(id_borrado):
    lista_tareas, ruta_archivo = cargar_datos()
    
    
    
    # Comprobamos si el ID existe en alguno de los diccionarios
    existe = any(t["id"] == id_borrado for t in lista_tareas)

    if existe:
        # Aquí va tu lógica de filtrado que ya tenías
        lista_tareas = [tarea for tarea in lista_tareas if tarea["id"] != id_borrado]
        guardar_tareas(lista_tareas, ruta_archivo)
        print(f"Tarea {id_borrado} borrada con éxito.")
    else:
        print("ID no encontrado")
        return
    
    return id_borrado
  

def mostrar_tareas():
    lista_tareas = cargar_datos()
    for tarea in lista_tareas[0]:
        print(tarea)

def modificar_tareas(id_editor, nuevo_nombre, nueva_descripcion):
    lista_tareas, ruta_archivo = cargar_datos()
    today = str(date.today())

    
    
    existe = any(t["id"] == id_editor for t in lista_tareas)
   
    if existe:
      
     

      lista_tareas = [
            {**t, "nombre": nuevo_nombre, "descripcion": nueva_descripcion, "modificado":today} 
            if t["id"] == id_editor else t 
            for t in lista_tareas
        ]
    else:
       print("ID no encontrado")
       return
    
    guardar_tareas(lista_tareas, ruta_archivo) 
    
    return id_editor, nuevo_nombre, nueva_descripcion







def cambiar_estado(id_editor, nuevo_estado):
    lista_tareas, ruta_archivo = cargar_datos()
    today = str(date.today())

    existe = any(t["id"] == id_editor for t in lista_tareas)
    if existe:

               
    
        
               if nuevo_estado == 1:
                    nuevo_estado = "Terminado"
               elif nuevo_estado == 2:
                    nuevo_estado = "En progreso"
               elif nuevo_estado == 3:
                    nuevo_estado = "Sin terminar"
               else:
                print("ID no encontrado")
                return 
    else:
        print("TAREA NO EXISTE")
        return 
    
    
    lista_tareas = [
        {**t, "estado": nuevo_estado, "modificado":today} if t["id"] == id_editor else t 
        for t in lista_tareas
    ]

    
    guardar_tareas(lista_tareas, ruta_archivo)

    return id_editor, nuevo_estado
 
        
       
    
    

   

   
    
    
def mostrar_ayuda():
    print("\n" + "="*30)
    print("   GESTOR DE TAREAS CLI")
    print("="*30)
    print("Uso: python TODO.PY [OPCIÓN]")
    print("\nOpciones disponibles:")
    print("  --list      : Listar todas las tareas")
    print("  --create    : Añadir una nueva tarea")
    print("  --modify    : Editar una tarea existente")
    print("  --status    : Cambiar el estado de una tarea")
    print("  --delete    : Eliminar una tarea por ID")
    print("="*30 + "\n")
   



    
 


if __name__ == "__main__":
     
     parser = argparse.ArgumentParser(description="Gestor de Tareas")
     parser.add_argument("--list", action="store_true", help="Muestra todas las tareas")
     parser.add_argument("--create", action="store_true", help="Crea una tarea")
     parser.add_argument("--modify", type=int, help="Modifica una tarea")
     parser.add_argument("--status", type=int, help="ID de la tarea a cambiar")
     parser.add_argument("--set", type=int, help="Nuevo estado (1: Terminado, 2: Proceso, 3: Pendiente)")
     parser.add_argument("--nombre", type=str, help="PARAMETRO DE LA TAREA: NOMBRE")
     parser.add_argument("--des", type=str, help="PARAMETRO DE LA TAREA: DESCRIPCION")
     parser.add_argument("--delete", type=int, help="BORRA UNA TAREA")    
     parser.add_argument("--help_custom", action="store_true")

     if len(sys.argv) == 1:
        mostrar_ayuda()
        sys.exit()
    
    
     args = parser.parse_args()
     if args.list:
       mostrar_tareas()
     elif args.create:
      crear_tarea()
     elif args.modify:
      modificar_tareas(args.modify, args.nombre, args.des)
     elif args.status:
      cambiar_estado(args.status, args.set)
     elif args.delete:
      borrar_tarea(args.delete)
     elif args.help_custom:
         help()

        
     

      
     


     


