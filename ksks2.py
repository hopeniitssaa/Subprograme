def creare_lista():
    n=int(input('numarul de elemente: '))
    lista_creata=[]
    for i in range(n):
        element=eval(input('elementul '+str(i)+' este: '))
        while type(element)!=float:
            element=eval(input(' elemente integer! Elementul '+str(i)+' este: '))
            if type(element)==float:
                break
        lista_creata.append(element)
    return lista_creata
lista1=creare_lista()
print(lista1)