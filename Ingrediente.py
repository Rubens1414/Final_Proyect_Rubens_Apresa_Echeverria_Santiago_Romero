name = input("Me podria decir su nombre?")



def holaConNombre(name):
  print("Hola bienvenido a su tienda de fritos favorita, ¿como se encuentra " + name + "?")

holaConNombre(name)  

salsa = input("Me podria decir que salsa desea?")
masa = input("Me podria decir que tipo de masa desea?")
tipo = input("Me podria decir tipo de frito quiere comer?")
relleno = input("Me podria decir con que desea rellenar su frito?")

def armado(name,salsa,masa,tipo,relleno):
    print("Usuario "+ name + " su frito sera un " + tipo + " con una masa hecha a base de " + masa + " rellena con " + relleno + " acompañado con salsa " + salsa)
armado(name,salsa,masa,tipo,relleno)
