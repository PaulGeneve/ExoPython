a = 1

while a > 0:
    a = int(input('Entrez une année : '))
    if( a%4==0 and a%100!=0 or a%400==0):
        print("L'annee est une annee bissextile!")
    else:
        print("L'annee n'est pas une annee bissextile!")



