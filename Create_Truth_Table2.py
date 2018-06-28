import numpy as np

# Create combinations of true and false
number_of_variables = 7
number_of_states = 2**number_of_variables
truth_table = np.array(range(number_of_states*number_of_variables), dtype= object).reshape(number_of_states,number_of_variables)

def imprimir_verdadero_falso(contador, columna, arreglo):

    filas = 0
    cont = contador
    bandera  = False
    if (bandera==False):
        while(cont!=0):
            #incrementar la fila
            print('FALSO')
            truth_table[filas,columna] = 'FALSO'
            arreglo.append('FALSO')
            cont = cont-1
    bandera = True
    cont = contador
    if(bandera==True):
        while(cont!=0):
            # incrementar fila
            print('VERDADERO')
            truth_table[filas, columna] = 'VERDADERO'
            arreglo.append('VERDADERO')
            cont=cont-1
    bandera = False


x_out = []
for col in range(number_of_variables):
    print('+++++++++++++++')
    print('columna', col)
    for i in range(0,number_of_states,(2**(col+1))):
        print(i,':')
        imprimir_verdadero_falso(2**col, col, x_out)


print(x_out)

y  =  np.reshape(x_out,(number_of_variables,number_of_states))  # changes from array to matrix format
y2 = np.transpose(y)
#print('************\n',y2)

y3 = np.fliplr(y2)    #changes order of columns
print('************\n',y3)

np.savetxt('Tabla_Verdad.csv',y3, fmt = "%s", delimiter=',')
#np.savetxt('Tabla_Verdad.csv',y3, object, delimiter=',',header='v1,v2,v3,v4,v5,v6,v7,v8')


