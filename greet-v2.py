# PYTHON3 FILE

def greet(lang) :
    if lang == 'es' :
        return 'Hola'
    elif lang == 'de' :
        return 'Hallo'
    elif lang == 'fr' :
        return 'Salut'
    else :
        return 'Hello'

print('Espagnol :', greet('es'), 'Martina') 
print('Anglais :', greet('en'), 'Suzi')
print('Français :', greet('fr'), 'Marie')
print('Allemand :', greet('de'), 'Milena')
