import math

print(f"Le nombre d'Euler vaut environ : {math.e}")
phrase = f"Le nombre d'Euler vaut environ : {math.e}"
print("-" * len(phrase))
print()

def factorial(n):
    if n == 0: return 1
    else:
        facto = 1
        for i in range(1, n+1): facto = facto * i
        return facto

#for i in range(10): print(f"{i}! = {factorial(i)}")

def approx_e(n):
    s = 0
    for i in range(n): s += 1/factorial(i)
    return s

for i in range(10): 
    print(f"Approximation du nombre d'Euler après {i} itérations : {approx_e(i)}")
    phrase = f"Approximation du nombre d'Euler après {i} itérations : {approx_e(i)}"
    print("-" * len(phrase))
    print(f"Ecart absolu par rapport à la vraie valeur : {abs(approx_e(i) - math.e)}")
    phrase = f"Ecart absolu par rapport à la vraie valeur : {abs(approx_e(i) - math.e)}"
    print("=" * len(phrase))
    print()


def pouces_cm(nb_inch):
    return 2.54*nb_inch

print("Les écrans d'ordinateurs standard ont une diagonale de :")
for size in range(11, 22, 2): print(f'{size}" = {pouces_cm(size)} cm')


def cm_pouces(nb_cm):
    return 0.39*nb_cm

print("Quelques conversion des cm vers les pouces (inches en anglais)")
for cm in range(1, 60, 2): print(f'{cm} cm = {cm_pouces(cm):.2f}"')


print(f"Le nombre π vaut environ : {math.pi}")
phrase = f"Le nombre π vaut environ : {math.pi}"
print("-" * len(phrase))
print()

def approx_pi(n):
    s = 0
    for i in range(1, n+1): s += 1/i**2
    return (6*s)**(0.5)

for i in range(10,20): 
    print(f"Approximation du nombre π après {i} itérations : {approx_pi(i)}")
    phrase = f"Approximation du nombre π après {i} itérations : {approx_pi(i)}"
    print("-" * len(phrase))
    print(f"Ecart absolu par rapport à la vraie valeur : {abs(approx_pi(i) - math.pi)}")
    phrase = f"Ecart absolu par rapport à la vraie valeur : {abs(approx_pi(i) - math.pi)}"
    print("=" * len(phrase))
    print()
