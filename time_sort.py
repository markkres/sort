import sort
import time
import random

a=[10,100,1000,10000,10**7]
mas=[]
for n in a:
    mas.append([random.randint(-100,100) for _ in range(n)])
    print(n)
start=time.time()
print(start)
#sort.bubble_sort(mas[1])
#sort.select_sort(mas[3])
#sort.insertion_sort(mas[3])
sort.quick_sort(mas[4],0,len(mas[4])-1)
#sort.cocktailSort(mas[3])
end=time.time()
print(end)
T=end - start
print(T)
