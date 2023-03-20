#Economu Victor, grupa 134
#AFD

#Functii diverse:
def afisare_Delta(D):
    for d in D:
        print(d)
    print()

def afisare_Drum(dr, s):
    for tu in dr:
        print("q(" + str(tu[0]) + ") " + tu[1] + "-->", end = " ")
    print("q(" + str(s) + ")" + "\n")

#Main-ul:
fisier_ales = "Prezentare_in.txt"
f1 = open(fisier_ales, "r")
Q = int(f1.readline()) #Citim numarul total de stari.
F = set(int(F_i) for F_i in f1.readline().split()) #Citim un set cu toate starile finale(acceptoare).
#print(F)
"""
    Mai jos, citim toate valorile functiei Delta(regasite si in tabelul prezentat in curs) si
construim o lista de dictionare care retin in mod optim toate aceste valori(cate 3 pe rand).
"""
Delta = [{} for i in range(Q)]
for line in f1:
    line = line.split()
    line[0] = int(line[0])
    line[2] = int(line[2])
    #print(line)
    if line[1] not in Delta[line[0]]:
        Delta[line[0]][line[1]] = line[2]
f1.close() 

#afisare_Delta(Delta) #afisam automatul nostru(AFD).

word_file = "Prezentare_in_cuv.txt"
f2 = open(word_file, "r")
cuv = f2.readline().strip() #Citim cuvantul si mai jos analizam daca va fi acceptat de AFD-ul nostru sau nu.
f2.close()
#print("Cuvantul citit este: ", cuv, "\n")
stare = 0
flag = True
Drum = []
ind = 0
while ind < len(cuv) and flag:
    caracter = cuv[ind]
    if caracter not in Delta[stare]:
        flag = False
        break
    else:
        Drum.append((stare, caracter))
        stare = Delta[stare][caracter]
    ind += 1

    ## Verificare in cazul cuvantului "vid"!
if cuv == "vid" and 0 in F:
    print("Cuvantul vid este acceptat!")
elif cuv == "vid" and 0 not in F:
    print("Cuvantul vid NU este acceptat!")
    ##
elif flag == False or stare not in F:
    print("Neacceptat!")
else:
    print("Acceptat!")
    print("Drumul folosit este:")
    afisare_Drum(Drum, stare)

    


