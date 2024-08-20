from pizza import Pizza

print(Pizza.precio)
print(Pizza.tamaño)

print(Pizza.validar("salsa de tomate", ["salsa de tomate", "salsa bbq"]))

pizza1 = Pizza()
pizza1.realizar_pedido()

print(f"El ingrediente proteico es {pizza1.ingrediente_proteico}")
print(f"El primer ingrediente vegetal es {pizza1.primer_ingrediente_vegetal}")
print(f"El segundo ingrediente vegetal es {pizza1.segundo_ingrediente_vegetal}")
print(f"El tipo de masa es {pizza1.tipo_masa}")
print(f"Pizza valida:{pizza1.pizza}")

print(Pizza.pizza)