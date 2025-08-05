#Definicion de la clase
class usuario:
 def __init__(self, nombre, contraseña):
   self.nombre = nombre
   self.contraseña = contraseña

#Objeto usando clase usuario
usuario1 = usuario("Miren", "1234")

#Verificar los datos
print("Nombre de usuario:", usuario1.nombre)
print("Contraseña:", usuario1.contraseña)