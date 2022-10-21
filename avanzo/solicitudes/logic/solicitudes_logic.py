from clientes.models import Cliente
from ..models import Solicitud
import PyPDF2 as pypdf

def get_solicitudes():
    solicitudes = Solicitud.objects.all()
    return solicitudes

def get_solicitud(sol_pk):
    solicitud = Solicitud.objects.get(pk=sol_pk)
    return solicitud

def update_solicitud(sol_pk, new_sol):
    solicitud = get_solicitud(sol_pk)
    solicitud.monto = new_sol["monto"]
    solicitud.interes = new_sol["interes"]
    solicitud.plazo = new_sol["plazo"]
    solicitud.estado = new_sol["estado"]
    solicitud.cliente = new_sol["cliente"]
    solicitud.save()
    return solicitud

def create_solicitud(sol):
    cliente = Cliente(
        cedula = sol["cedula"],
        nombre = sol["nombre"],
        telefono = sol["telefono"],
        correo = sol["correo"],
        direccion = sol["direccion"],
        password = sol["password"]
    )
    solicitud = Solicitud(
        monto = sol["monto"],
        interes = sol["interes"],
        plazo = sol["plazo"],
        estado = sol["estado"],
        cliente = cliente
    )
    solicitud.save()
    return solicitud

def delete_solicitud(sol_pk):
    solicitud = get_solicitud(sol_pk)
    solicitud.delete()
    return solicitud

# ================ #
#  LÓGICA ARCHIVO  #
# ================ #

def pdf_to_txt(pdf_file, txt_file):
    pdf_file_obj = open(pdf_file, 'rb')
    pdf_reader = pypdf.PdfFileReader(pdf_file_obj)
    x = pdf_reader.numPages
    file = open(txt_file, 'a')

    for i in range(x):
        page_obj = pdf_reader.getPage(i)
        file.write(page_obj.extractText())


def analysis(pdf_file, txt_file):
    pdf_to_txt(pdf_file, txt_file)
    #pdf_to_txt('Formato-Solicitud-de-Credito (AVANZO).pdf', r'C:/Users/Nico/Código_más_parte/pdf_convertor/pdf_1_txt.txt')
    txt = open(txt_file, 'r')
    lines = txt.readlines()
    monto = int(lines[len(lines) - 2].replace('\n', ''))
    plazo = int(lines[len(lines) - 1].replace('\n', ''))

    # interés y estado
    interes = 0.18 # temporal, no está en el formato.
    estado = True # True = aprobado, False = rechazado.

    return (monto, interes, plazo, estado)

def create_solicitud_analyzed(pdf_file, txt_file):
    analyzed = analysis(pdf_file, txt_file)
    monto = analyzed[0]
    interes = analyzed[1]
    plazo = analyzed[2]
    estado = analyzed[3]

    sol = {
        'cedula':1007530085,
        'nombre':'Nicolás',
        'telefono':3219109239,
        'correo':'nklopstock@',
        'direccion':'Cra 19',
        'password':'estrellita,dimedondeestas',
        'monto':monto,
        'interes':interes,
        'plazo':plazo,
        'estado':estado
    }

    solicitud = create_solicitud(sol)
    
    open(txt_file, "w").close() # vaciar el txt.

    return solicitud