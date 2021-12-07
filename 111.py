#exercice 111

def somme_produits(t1, t2):
    somme = 0
    for a in t1:
        for b in t2:
            somme = somme + a * b
    return somme


def produit_sommes(t1, t2):
    somme1 = 0
    somme2 = 0
    for a in t1:
        somme1 = somme1 + a
    for b in t2:
        somme2 = somme2 + a
    return somme1 * somme2


#exercice 112

def multiplication():
    n = 11
    for i in range(1, n):
        print("Table de", i, ":")
        for j in range(1, n):
            print(i, "x", j, "=", i*j)
            
            
#exercice 113
            
def ex113(h, l):
    for i in range(h):
        print(l * "#")
        
        
#exercice 114

#figure 1
def ex114_1(n):
    for i in range(1, n+1):
        print(i * "#")
        
#figure 2
def ex114_2(n):
    for i in range(1, n+1):
        print((n-i) * "#")
        
#figure 3
def ex114_3(n):
    for i in range(1, n+1):
        print(i * ".", (n-i) * "#")
        
        
        
        
        
        
            
            
            
            
            
            
            
            
            
            
            
            
