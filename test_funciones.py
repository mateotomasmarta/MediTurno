from funciones.secretario.login import validar_credenciales
from utils.auxiliares import obtener_id_por_dni

def test_validar_credenciales_correctas():
    assert validar_credenciales("admin", "admin123") == True
    assert validar_credenciales("admind", "1234") == False
    assert validar_credenciales("admin", "123") == False

def test_obtener_id_por_dni():
    assert obtener_id_por_dni("30123456") == 1
    assert obtener_id_por_dni("123456") == None
    assert obtener_id_por_dni("ah") == None
    
#CORRER CON python -m pytest