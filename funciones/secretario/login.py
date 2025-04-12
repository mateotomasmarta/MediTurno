from datos import matriz_secretario

def validar_credenciales(usuario, password):
    """Valida las credenciales del secretario contra la matriz"""
    for secretario in matriz_secretario:
        if secretario['usuario'] == usuario and secretario['password'] == password:
            return True
    return False