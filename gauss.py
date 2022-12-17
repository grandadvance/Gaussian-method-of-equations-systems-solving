import pandas
import random as rnd
import numpy as np
import mymethods as mth
choice = 1

# Блок где задается матрица через генератор
if choice == 1:
    matrix = [] 
    bufer = []
    rows = int(input("Choose equations number "))
    columns = rows+1
    for i in range(0, rows):
        matrix.append([])
        bufer.append([])
        for j in range(0,columns):
            matrix[i].append(float(rnd.randint(-10,10)))
            bufer[i].append(matrix[i][j])

    print('\nThe matrix coefficients before solving:\n')
    mth.print_matrix(matrix,4)

# Блок где задается матрица через файл
#if choice == 2:
#    input_file = pandas.read_csv('coefficients.csv',  encoding='utf-8', names = [0,1,2,3]) 
#    data_frame = pandas.DataFrame(input_file)
#    rows = len(data_frame)
#    columns = data_frame.size//rows

#    matrix = [] 
#    bufer = []
   
#    for i in range(0,rows):
#        bufer.append([])
#        matrix.append([])
#        for j in range(0, columns):     
#            matrix[i].append(data_frame[j][i])
#            bufer[i].append(float(matrix[i][j]))
        
#    print('\nДо преобразований:\n')
#    mth.print_matrix(matrix,4)


# Блок где задается матрица через написание строки
#if choice == 2:
#    equations = []
#    equations.append('-22.1*x1-3.5*x2-4*x3=5')
#    equations.append('2.1*x1+3*x2-3*x3=-12')
#    equations.append('-2*x1+3*x2+5*x3=0')

    
#    rows_coef = []
#    for j in range(0, len(equations)):
#        num = ''
#        flag = 0
#        rows_coef.append([])
#        for i in range(0, len(equations[j])):
#            equation = equations[j]
#            if equation[i] == '*':
#                for t in range(flag,i):
#                    num = num + equation[t]
#                rows_coef[j].append(float(num))
#                num = ''
#            if equation[i] == '=':
#                for t in range(i+1,len(equations[j])):
#                    num = num + equation[t]
#                rows_coef[j].append(float(num))
#            if equation[i] == '+' or equation[i] == '-':
#                flag = i
#    print(rows_coef)
#    
#    rows = len(rows_coef)
#    columns = rows+1
#    matrix = [] 
#    bufer = []       
#    
#    for i in range(0, rows):
#        matrix.append([])
#        bufer.append([])
#        for j in range(0,columns):
#            matrix[i].append(rows_coef[i][j])
#            bufer[i].append(matrix[i][j])
#
#    print('\nДо преобразований:\n')
#    mth.print_matrix(matrix,4)    
    
# Блок преобразований
for m in range(0, rows-1):    
    # Проверка на равенство элемента главной диагонали нулю и соответствующая смена строк
    if (matrix[m][m] == 0):
        mth.change_rows_if_cell_zero(matrix,m)
        bufer = np.array(matrix)

    for i in range(m+1, rows): 
        for j in range(m, columns):
            bufer[i][j] = matrix[i][j] - (matrix[i][m]/matrix[m][m]) * matrix[m][j]
#    print('\n m = ',m)
    matrix = np.array(bufer)
#    mth.print_matrix(matrix,2)
    
print('\nThe matrix coefficients after using Gaussian method:\n')
mth.print_matrix(matrix,2)

# Оформляем корни
my_root = []
my_root = mth.roots(matrix) 
print()
    
for i in range(0,rows):
    print(mth.X_with_index(my_root[i],i+1))

# Подставляем корни в первое уравнение и проверяем равенство
checking = 0
print()
for i in range(0,rows):
    checking = checking + matrix[0][i]* my_root[rows-1-i]
print("Left side of first equation is", checking)
print()
