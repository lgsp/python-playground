def insertion_sort(tab):
    for i in range(1, len(tab)):
        j = i - 1
        tmp = tab[i]
        while j >= 0 and tmp < tab[j]:
            tab[j+1] = tab[j]
            j -= 1
        tab[j+1] = tmp

tab = [1, 9, 8, 2, 7, 6, 3, 5, 4, 0]
print("Initial table")
for elt in tab: print(elt, end=" ")
print("\nSorted table")
for elt in tab: print(elt, end=" ")
