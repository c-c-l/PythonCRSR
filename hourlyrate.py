# PYTHON3 FILE

hrs = input('Enter hours:')
h = float(hrs)
rate = input('Enter rate:')
r = float(rate)

# Dans le cas où l'on a fait plus de 40 heures
# les heures au dessus de 40 sont comptées 1.5 plus
if h > 40 :
    # On obtient le nombre d'heures sup
    nbhsup = h - 40
    ratesup = r * 1.5
    paysup = nbhsup * ratesup
    # On enlève les heures supplémentaires
    h = h - nbhsup
else :
    paysup = 0
pay = h * r
pay = pay + paysup
print(pay)
