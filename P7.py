#exercice P7

#exercice 114

#figure 3

def fig3(n):
    print(n*("#"))
    for i in range(n-2):
        print("#", (n-2)*".", "#" )
    print(n*("#"))
    
    
    
  #exercice 115

def ex115():
    for a in range(1, 101):
        for b in range(a, 101):
            for c in range(b, 101):
                if a**2 + b**2 == c**2:
                    print(a, b, c)
    
def ex115prim():
    acc = 0
    for a in range(1, 101):
        for b in range(a, 101):
            for c in range(b, 101):
                if a**2 + b**2 == c**2:
                    acc += 1
    return acc


#exercice 116

def ex116():
    t = [True]*100
    t[0] = False
    t[1] = False
   
    for i in range(100):
        if t[i] == True:
            for j in range(i+1, 100):
                if j%i == 0:
                    t[j] = False
    acc = 0         
    for i in range(100):
        if t[i] == True:
            print(i)
            acc += 1
    
    return "nombre de nombres premiers:", acc


#exercice 118

def inclus(t1, t2):
    acc = 0
    for i in range(len(t1)):
        for j in range(len(t2)):
            if t1[i] == t2[j]:
                acc += 1
    if acc == len(t1):
        return True
    else:
        return False
            


    
    
  

    

    
            
        
