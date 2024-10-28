def bubble_sort(mas):
    n=len(mas)
    unordered=True
    while unordered:
        unordered=False
        for j in range(n-1):
            if mas[j]>mas[j+1]:
                mas[j],mas[j+1]=mas[j+1],mas[j]
                unordered=True
        n-=1
    return mas
def select_sort(mas):
    for i in range(len(mas)-1):
        imin=i
        for j in range(i+1,len(mas)):
            if mas[j]<mas[imin]:
                imin=j
        mas[i],mas[imin]=mas[imin],mas[i]
    return mas
def insertion_sort(mas):
    for i in range(1,len(mas)):
        tmp=mas[i]
        j=i-1
        while j>=0 and mas[j]>tmp:
            mas[j+1]=mas[j]
            j-=1
        mas[j+1]=tmp
    return mas
print(insertion_sort([3,8,5,4]))
