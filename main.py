#1-Kullanıcının girdiği boy ve ağırlık değerlerine göre vücut kitle indeksini (VKİ = ağırlık/(boy*boy)) hesaplayınız.
boy = float(input("Lütfen boyunuzu giriniz(metre cinsinden): "))
kilo = float(input("Lütfen kilonuzu giriniz: "))
vki = kilo / (boy * boy)
print(vki)

#2-Maaşı ve zam oranı girilen işçinin zamlı maaşını hesaplayarak ekranda gösteriniz.
maas = float(input("Lütfen maasşınızı giriniz: "))
zamOrani = float(input("Lütfen zam oranınızı giriniz: "))
zamliMaas = maas + (maas * (zamOrani / 100))
print(zamliMaas)

#3-Kullanıcının girdiği üç sayı arasında en büyük olanı bulan ve sonucu yazdıran bir program yazınız.
number1 = int(input("Lütfen ilk sayıyı giriniz: "))
number2 = int(input("Lütfen ikinci sayıyı giriniz: "))
number3 = int(input("Lütfen üçüncü sayıyı giriniz: "))
TheBiggestNumber = 0

if number1 > number2:
     TheBiggestNumber = number1
else:
     TheBiggestNumber = number2
if number3 > TheBiggestNumber:
     TheBiggestNumber = number3
else:
    TheBiggestNumber = TheBiggestNumber
 print(TheBiggestNumber)

#4-Dairenin alanını ve çevresini hesaplayan python kodunu yazınız.(Dairenin yarıçapını kullanıcıdan alınız)

yariCap = float(input("Yarıçap giriniz: "))
alan = 3.14 * (yariCap * yariCap)
print(f"Alan: {alan}")

cevre = 2 * 3.14 * yariCap
print(f"Çevre: {cevre}")


#5-Kullanıcıdan alınan bir sayının palindrom olup olmadığını bulan bir program yazınız.
def palindrom_mu(sayi):
    sayi_str = str(sayi)
    ters_sayi_str = sayi_str[::-1]  
    return sayi_str == ters_sayi_str

sayi = int(input("Bir sayı girin: "))

if palindrom_mu(sayi):
    print("Girdiğiniz sayı bir palindromdur.")
else:
    print("Girdiğiniz sayı bir palindrom değildir.")
