import numpy as np
##############################################################
# Функция symbol_lenght_array() принимает на вход 
# двумерный массив с точностью  каждого числа 
# до number_precision знаков после запятой
# Возвращает одномерный массив, состоящий из 
# длинн символов входного массива

def symbol_lenght_array(Array, number_precision): 

    returned_mass = []
    
    rows_len = len(Array)
    
    columns_len = len(Array[0])
    
    for i in range(0, rows_len):
    
        for j in range(0, columns_len):
        
            number = round(Array[i][j], number_precision)
            
            returned_mass.append(len(str(number)))
            
    return returned_mass
    

##############################################################
# Функция minmax() принимает на вход одномерный массив и слово
# 'min' или 'max' и в соответствии выдает мин или макс элемент

def minmax(Array, MinOrMax):

    for i in range(len(Array)):
    
        for j in range(0,len(Array)-1-i):
        
            if Array[j] > Array[j+1]:
            
                Buffer = Array[j+1]
            
                Array[j+1] = Array[j]
            
                Array[j] = Buffer

    if MinOrMax == 'min':
    
        return Array[0]
    
    if MinOrMax == 'max':
    
        return Array[len(Array)-1]
        
##############################################################        
# Функция print_matrix() принимает на вход двумерный массив
# а так же заданную точность для элементов. Возвращает 
# выровненную матрицу, в которой элементы представлены, как 
# вещественные числа с точностью до number_precision знаков
# после запятой и отодвинутые друг от друга на расстояние
# наибольшего по количеству знаков числа

def print_matrix(massiv, number_precision):   
 
    symbol_max_len = minmax(
                             symbol_lenght_array( 
                             massiv, number_precision), 'max' )
                             
    rows_len = int(len(massiv))
    
    columns_len = int(len(massiv[0]))
    
    for i in range(0, rows_len):
    
        for j in range(0, columns_len):
        
            f = round(massiv[i][j],number_precision)
            
            print((symbol_max_len - len(str(f)))*" ", f, end='')
            
        print()
        
##############################################################
# Функция change_rows_if_cell_zero() принимает на вход 
# двумерный массив и рассматриваемый член главной диагонали
# Если элемент главной диагонали равен 0, то его строка
# меняется на любую другую строку так, чтобы A[i][i] != 0
# Для этого:
# 1. Проверяем ячейку на наличие нуля и запускаем проверку 
#    элементов по данному столбцу
# 2. Если находим элемент, отличный от нуля, то меняем его строку
#    на строку, ячейка в которой оказалась равной нулю

def change_rows_if_cell_zero(massiv,diagonal_index):

    temp = []

    m = diagonal_index

    t = diagonal_index

    while(massiv[t][m] == 0):

        t+=1

        if (massiv[t][m] != 0):

            temp = np.array(massiv[m])

            massiv[m] = np.array(massiv[t])

            massiv[t] = np.array(temp)

            break
            
##############################################################
# Функция massiv_recosting() принимает на вход один
# из элементов start_point перебираемого массива, а так же
# длину самого массива massiv_len и возвращает массив,
# заполненный по порядку слева направо от числа start_point
# Например, input_mass = [0,1,2,3,4]
# start_point = 2
# Получим temp_massiv = [2,3,4,0,1]

def massiv_recosting(start_point, massiv_len): 

    return_massiv = []

    for i in range(start_point, massiv_len):

        return_massiv.append(i)

        if i == massiv_len - 1:
        
            massiv_len = start_point
        
            start_point = 0
        
            for i in range(start_point, massiv_len):
        
                return_massiv.append(i)
                
    return return_massiv
    
    
##############################################################
# Функция нахождения корней уравнения
def roots(array):
    X = []
    rows = len(array)-1 
    c = len(array[0])-1

    X.append(round(array[rows][c]/array[rows][rows],3))

    for r in range(1, rows+1):
        remainder_summ = 0
        Xonce1 = array[rows-r][c]/array[rows-r][rows-r]
        Xonce2 = 1/array[rows-r][rows-r]
        for i in range(0,r):
            remainder_summ = remainder_summ + array[rows-r][c-(1+i)]*X[i]
        X.append(round(Xonce1 - Xonce2*remainder_summ,3))
    return X
    
##############################################################
# Функция показа буквы вместе с индексом в системе юникода    
def X_with_index(digit: int, index: int):

    indexes = {"0": "\u2080",
               "1": "\u2081",
               "2": "\u2082",
               "3": "\u2083",
               "4": "\u2084",
               "5": "\u2085",
               "6": "\u2086",
               "7": "\u2087",
               "8": "\u2088",
               "9": "\u2089"
               }

    degrees = ""
    
    for char in str(index):
    
        degrees += indexes[char] 
        
    return "X" + degrees + " = " + str(digit) 
    
    

