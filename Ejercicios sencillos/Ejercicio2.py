# Calcular área de un triángulo dados los datos (base y altura)
base = float(input("Base: "))
altura = float(input("Altura: "))
# Usando coma
print("Área del triángulo: %.2f" % ((base * altura) / 2),"Perímetro: %.2f" % ((base + altura) * 2))
# Usando + y dejando espacio
print("Área del triángulo: %.2f " % ((base * altura) / 2) + "Perímetro: %.2f " % ((base + altura) * 2))
# Pasando los valores a String (menos correcto)
print("Área del triángulo: " + str(((base * altura) / 2)) + " Perímetro: " + str(((base + altura) * 2)))