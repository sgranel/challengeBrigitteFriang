# -*- coding: utf-8 -*-
"""
Created on Mon Nov  9 10:03:09 2020

@author: s.granel
"""

with open('fichier_d_gros.in') as f:
    first_line = f.readline()
    first_line = first_line.split( )
    max_val = int(first_line[0])
    nb_object = int(first_line[1])
    second_line = f.readline()
    second_line = second_line.split( )
    second_line_sorted = second_line.copy()
    second_line_sorted.sort()
    second_line_sorted.reverse()
    take = second_line.copy()
    
    result_array = []
    result = 0
    
    cpt = 0
    while cpt < nb_object:
        index_array = []
        i = 0
        temp_array = []
        max_val_temp = max_val
        while max_val_temp > 0 and i < nb_object :
            if (cpt != i and max_val_temp >= int(second_line_sorted[i]) and not(i in index_array)):
                max_val_temp -= int(second_line_sorted[i])
                temp_array.append(second_line_sorted[i])
                index_array.append(i)
                if(max_val_temp ==0):
                    i = nb_object
                    cpt = nb_object
            else:
                i = i + 1
        cpt = cpt +1
        result_array.append(temp_array)
   
    i = 0
    winner = -1
    max_result = 0
    winner_array = []
    while i < len(result_array):
        temp_resul = 0
        j = 0
        while j < len(result_array[i]):
            temp_resul = temp_resul + int(result_array[i][j])
            j = j+1
        if(temp_resul == max_val or max_result < temp_resul):
            winner = i
            max_result = temp_resul
            winner_array = result_array[i]
            print(i)
            print(max_result)
        i = i+1
            
    final_array = []
    for i in range(len(winner_array)):
        if(not(second_line.index(winner_array[i]) in final_array)):
            final_array.append(second_line.index(winner_array[i]))
            second_line[second_line.index(winner_array[i])] = '0'
    final_array.sort()
    
    result_file = open('result_d_fichier.txt', 'w')
    result_file.write(str(len(final_array)))
    result_file.write('\n')
    for i in range(len(final_array)):
        result_file.write(str(final_array[i]))
        if(i+1 < len(final_array)):
            result_file.write(' ')
    result_file.close()
    