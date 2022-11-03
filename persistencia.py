import pickle, glob

def guardar(nombre, elemento):
#el archivo se crea con el nombre que se le asigna al archivo .pickle, elemento seria, lo que queremos guardar en ese archivo
  with open(f"{nombre}.pickle", "wb") as f:
    #El Dump, vuelca los elementos al archivo
    pickle.dump(elemento, f)

def cargar(nombre):
  #nos da la info de todo lo que se almaceno en el archivo que creamos
  with open(f"{nombre}.pickle", "rb") as f:
    return pickle.load(f)

def cargar_todos():

  elementos = {}
  
  #nos muestra en un diccionario, todos los archivos que guardamos

  for path in glob.glob("*.pickle"):
    nombre = path.replace(".pickle", "")
    elementos[nombre] = cargar(nombre)

  return elementos

