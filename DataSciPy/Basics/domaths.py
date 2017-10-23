# PYTHON3

# La fonction suivante ajoute deux valeurs si la valeur de "kind" est "add" ou
# non définie, sinon elle soustrait la seconde valeur à la première

def do_maths(a, b, kind='add'):
    if(kind=='add'):
        return a+b
    else:
        return a-b

# TEST
print ('La valeur doit être ajoutée : 1 + 2 :')
print(do_maths(1,2))
print ('La valeur doit être soustraite : 1 - 2 :')
print(do_maths(1, 2, kind='stuff'))
