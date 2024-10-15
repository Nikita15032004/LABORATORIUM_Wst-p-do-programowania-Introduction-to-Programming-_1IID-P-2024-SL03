
# A) Sprawdź w interpreterze typ wyników określonych działań - type( x ) i wyjaśnij, co
# oznaczają poszczególne operatory?
print(type(1 + 2)) #<class 'int'>
print(type(1 + 4.5)) #<class 'float'>
print(type(3 / 2)) #<class 'float'>
print(type(4 / 2)) #<class 'float'>
print(type(3 // 2)) #<class 'int'>
print(type(-3 // 2)) #<class 'int'>
print(type(11 % 2)) #<class 'int'>
print(type(2 ** 10)) #<class 'int'>
print(type(8 ** (1/3))) #<class 'float'>

# B) Sprawdź i wyjaśnij działanie następujących instrukcji:
print('------------------------ \n')

print(int(3.0))
print(float(3))
print(float("3"))
print(str(12.4))
print(bool(0))


print("------------------")
#Zad. 2:
#Do zmiennej o nazwie uczelnia przypisz zdanie Studiuję na WSIiZ, Następnie korzystając z
#funkcji print() wydrukuj ten tekst do konsoli.
uczelnia = "Studiuję na WSIiZ"
print(uczelnia)


#Zad. 3:
#Podane są poniższe zmienne:
imię = "Jan"
wiek = 30
wzrost = 175

print(f"Nazywam się {imię} i mam {wiek} lat.\nMój wzrost to {wzrost} cm.")

#Zad. 4:
#Do zmiennej Cena przypisz cenę produktu równą 39.99 PLN oraz do zmiennej Rabat przypisz
#wartość 0.2 (rabat 20%). Następnie policz cenę tego produktu po zastosowaniu podanego
#rabatu. Wynik wydrukuj do konsoli. Zwróć uwagę na odpowiednie formatowanie tekstu w
#funkcji print() tak, aby końcowa cena produktu została wyświetlona tylko do drugiego
#miejsca po przecinku.

Cena = 39.99
Rabat = 0.2
discountedPrice = Cena * (1 - Rabat)
print(f"Price with discount: {discountedPrice:.2f} PLN")


