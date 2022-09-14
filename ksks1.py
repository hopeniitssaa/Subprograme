def lista():
    n=int(input('numarul de elemente: '))
    lista1=[]
    for i in range(n):
        element=eval(input('elementul '+str(i)+' este: '))
        while type(element)!=int:
            element=eval(input('elemente int '+str(i)+' este: '))
            if type(element)==int:
                break
        lista1.append(element)
    return lista1
lista1=lista()
print(lista1)