# -*- coding: utf-8 -*-
"""
Created on Wed May  4 16:45:14 2016

@author: Nikolay
"""

heap = 'opisanidiot'
ndl = 'an'

##brute-force:
#ind = -1
#for i in range(len(heap)):
#    success = True
#    for j in range(len(ndl)):
##        print(ndl[j], heap[i+j])
#        if ndl[j] != heap[i+j]:
#            success = False
#            break
#    if success:
#        ind = i
#        break
#print(ind)

#### Knuth-Morris-Pratt:
#Пусть S[0..m–1] – образец, T[0..n–1] – строка, в которой
# ведется поиск. Рассмотрим сравнение строк на позиции i,
# то есть образец S[0..m–1] сопоставляется с частью строки
# T[i..i+m–1]. Предположим, первое несовпадение произошло 
# между символами S[j] и T[i+j], где i < j < m.
# Обозначим P = S[0..j–1] = T[i..i+j–1]. 
# При сдвиге можно ожидать, что префикс S сойдется с каким-либо
# суффиксом строки P. Поскольку длина наиболее длинного префикса,
# являющегося одновременно суффиксом, есть префикс-функция от
# строки S для индекса j, приходим к следующему алгоритму:
#Построить префикс-функцию образца S, обозначим ее F.

#Положить k = 0, i = 0.
#Сравнить символы S[k] и T[i]. Если символы равны, увеличить k на 1. Если при этом k стало равно длине образца, то вхождение образца S в строку T найдено, индекс вхождения равен i – |S| + 1. Алгоритм завершается. Если символы не равны, используем префикс-функцию для оптимизации сдвигов. Пока k > 0, присвоим k = F[k–1] и перейдем в начало шага 3.
#Пока i < |T|, увеличиваем i на 1 и переходим в шаг 3.


def prefix(s):
    v = [0]*len(s)
    for i in range(1,len(s)):
        k = v[i-1]
        while k > 0 and s[k] != s[i]:
            k = v[k-1]
        if s[k] == s[i]:
            k = k + 1
        v[i] = k
    return v


def kmp(s,t):
    index = -1
    f = prefix(s)
    k = 0
    for i in range(len(t)):
        while (k > 0) & (s[k] != t[i]):
            k = f[k-1]
        if s[k] == t[i]:
            k = k + 1
        if k == len(s):
            index = i - len(s) + 1
            break
    return index
        
print(kmp(ndl, heap))