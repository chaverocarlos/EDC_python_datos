# Programa de agenda de contactos
# Métodos: Leer, Agregar, Actualizar y Eliminar

class Agenda:
    
    contactos = {"data":[]}

    # Metodos
    def leer(self):
        for i in self.contactos:
            print("Nombre: ", i["nombre"])
            print("Telefono: ", i["telefono"])
            print("Direccion: ", i["direccion"])
    
    def agregar(self):
        # diccionario["clave"] = valor
        datos = {}
        nombre_inp = input("Ingrese el nombre del nuevo contacto: ")
        telefono_inp = input("Ingrese el telefono del nuevo contacto: ")
        direccion_inp = input("Ingrese la direccion del nuevo contacto: ")
        self.identificador = self.identificador + 1
        datos["id"] = self.identificador
        datos["nombre"] = nombre_inp
        datos["telefono"] = telefono_inp
        datos["direccion"] = direccion_inp
        self.contactos["data"].append(datos)
        
    def editar(self, ident):
        for i in self.contactos:
            if(i["id"]) == ident):
                # diccionario["clave"] = valor
                nombre_inp = input("Ingrese el nombre del nuevo contacto: ")
                telefono_inp = input("Ingrese el telefono del nuevo contacto: ")
                direccion_inp = input("Ingrese la direccion del nuevo contacto: ")
                self.contactos["nombre"] = nombre_inp
                self.contactos["telefono"] = telefono_inp
                self.contactos["direccion"] = direccion_inp

    def eliminar(self, ident):
        for i in self.contactos:
            if(i[""])