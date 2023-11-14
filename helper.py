def trier(liste : list[list]):
    liste_triee = sorted(liste, key=lambda x: x[1])
    return liste_triee

def selectionner_n_premiers(n, liste : list[list]) : 
    l=[]
    for i in range(n):
        l.append(liste[i])
    return l

print(selectionner_n_premiers(4,[1,2,3,5,6,5,56,7]))