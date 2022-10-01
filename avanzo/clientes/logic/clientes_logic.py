from ..models import Cliente

def get_clientes():
    clientes = Cliente.objects.all()
    return clientes

def get_cliente(sol_pk):
    cliente = Cliente.objects.get(pk=sol_pk)
    return cliente

def update_cliente(sol_pk, new_sol):
    cliente = get_cliente(sol_pk)
    cliente.cedula = new_sol["cedula"]
    cliente.nombre = new_sol["nombre"]
    cliente.telefono = new_sol["telefono"]
    cliente.correo = new_sol["correo"]
    cliente.direccion = new_sol["direccion"]
    cliente.password = new_sol["password"]
    cliente.save()
    return cliente

def create_cliente(sol):
    cliente = Cliente(
        cedula = sol["cedula"],
        nombre = sol["nombre"],
        telefono = sol["telefono"],
        correo = sol["correo"],
        direccion = sol["direccion"],
        password = sol["password"]
    )
    cliente.save()
    return cliente

def delete_cliente(sol_pk):
    cliente = get_cliente(sol_pk)
    cliente.delete()
    return cliente