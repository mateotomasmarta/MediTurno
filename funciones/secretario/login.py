
secretaria = ("admin", "admin123")
def validar_credenciales(usuario, contrasena):
    return usuario == secretaria[0] and contrasena == secretaria[1]