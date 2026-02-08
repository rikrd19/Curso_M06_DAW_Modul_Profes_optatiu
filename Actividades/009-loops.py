 # loops.py o bucles

  #tipos while se repite mientras uan condicion sea verdadera 

# my_condition = 0 
# while my_condition < 10:
#     print(my_condition).  Incorrecto

my_condition = 0 

while my_condition < 10:
    print(my_condition)
    my_condition += 2

    # else se utiliza en estructuras if pero en python con while y for 

    my_condition = 0 

while my_condition < 10:
    print(my_condition)
    my_condition += 2
else:
    print("mi condicion es mayor o igual que 10")

print("la ejecucion continua")    