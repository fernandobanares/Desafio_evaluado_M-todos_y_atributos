from ingredientes import ingredientes_proteicos, ingredientes_vegetales, tipo_de_masa

class Pizza():
    precio = 10000
    tamaño = "familiar"
    
    @staticmethod
    def validar(texto,lista):
        if texto in lista:
            return True
        else:
            return False
        
    def realizar_pedido(self):
        ingrediente_proteico = input("Ingrese ingrediente proteico:\n")
        primer_ingrediente_vegetal = input("Ingrese el primer ingrediente vegetal:\n")
        segundo_ingrediente_vegetal = input("Ingrese el segundo ingrediente vegetal:\n")
        tipo_masa = input("Ingrese el tipo de masa:\n")
        #self.ingrediente_proteico = ingrediente_proteico
        #self.primer_ingrediente_vegetal = primer_ingrediente_vegetal
        #self.segundo_ingrediente_vegetal = segundo_ingrediente_vegetal
        #self.tipo_masa = tipo_masa
        valido1 = self.validar(ingrediente_proteico,ingredientes_proteicos)
        if valido1:
            self.ingrediente_proteico = ingrediente_proteico
        else:
            print("El ingrediente proteico ingresado no esta en el menu")
            self.pizza = False
            return
        
        valido2 = self.validar(primer_ingrediente_vegetal,ingredientes_vegetales)
        if valido2:
            self.primer_ingrediente_vegetal = primer_ingrediente_vegetal
        else:
            print("El primer ingrediente vegetal ingresado no esta en el menu")
            self.pizza = False
            return
        
        valido3 = self.validar(segundo_ingrediente_vegetal,ingredientes_vegetales)
        if valido3:
            self.segundo_ingrediente_vegetal = segundo_ingrediente_vegetal
        else:
            print("El segundo ingrediente vegetal ingresado no esta en el menu")
            self.pizza = False
            return
        
        valido4 = self.validar(tipo_masa,tipo_de_masa)
        if valido4:
            self.tipo_masa = tipo_masa
        else:
            print("El tipo de masa ingresado no esta en el menu")
            self.pizza = False
            return
                    
        self.pizza = True    