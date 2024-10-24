# sep, carácter de tipo string que se quiere usar para separar (por defecto es un espacio)
# end, carácter de tipo string que se quiere usar para el final (por defecto \n)
print(1,2,3,sep="-",end=".")

# %s indica que se va a introducir como primer valor un String
# %d como segundo valor un int
# %.2f la f indica que será un float y el .2 que tendrá 2 decimales
print("Producto: %s, Cantidad: %d, Precio: %.2f" % ("Boli", 4.2, 0.21132))
# Otra manera de formatear es usar la función format
print(format(0.123123,".2f"))