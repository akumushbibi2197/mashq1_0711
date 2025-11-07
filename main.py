#1-misol
def faktorial(n):
    result = 1
    for i in range(1, n + 1):
        result *= i
    return result

son = int(input("Son kiriting: "))
print("Faktorial =", faktorial(son))

#2-misol
def palindrommi(satr):
    satr = satr.lower().replace(" ", "")
    return satr == satr[::-1]

s = input("Satr kiriting: ")
print("Palindrom:", palindrommi(s))

#3-misol
def katta_kichik(royxat):
    return max(royxat), min(royxat)

r = [int(x) for x in input("Raqamlarni bo‘sh joy bilan kiriting: ").split()]
katta, kichik = katta_kichik(r)
print("Eng katta:", katta, "Eng kichik:", kichik)

#4-misol
def unli_soni(satr):
    unlilar = "aeiouAEIOUаеиоуўияюАЕИОУЎИЯЮ"
    return sum(1 for harf in satr if harf in unlilar)

satr = input("Satr kiriting: ")
print("Unli harflar soni:", unli_soni(satr))

#5-misol
def tubmi(n):
    if n < 2:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

son = int(input("Son kiriting: "))
print("Tub son:", tubmi(son))
