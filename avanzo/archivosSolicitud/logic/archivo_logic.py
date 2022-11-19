from ..models import ArchivoSolicitud

def get_archivos():
    archivos = ArchivoSolicitud.objects.all()
    return archivos

def get_archivo(archivo_pk):
    archivo = ArchivoSolicitud.objects.get(nombre=archivo_pk)
    return archivo

def create_archivo(pArchivo):
    archivo = ArchivoSolicitud(
        nombre = pArchivo["nombre"],
        archivo = pArchivo["archivo"]
    )
    archivo.save()
    return archivo

def update_archivo(archivo_pk, new_archivo):
    archivo = get_archivo(archivo_pk)
    archivo.nombre = new_archivo["nombre"]
    archivo.archivo = new_archivo["archivo"]
    archivo.save()
    return archivo

def delete_archivo(archivo_pk):
    archivo = get_archivo(archivo_pk)
    archivo.delete()
    return archivo