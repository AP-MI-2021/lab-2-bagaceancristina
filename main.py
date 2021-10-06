def is_antipalindrome(n):
    '''
    determina inversul unui numar si verifica conditia de antipalindrom
    input:
    - n
    output:
    - este sau nu antipalindrom
    '''
    i=0
    cn=n
    c=0
    while n:
        i=i*10+n%10
        n=n//10
        c=c+1
    if(c>1):
        c=c//2
    for p in range(c):
        if(i%10==cn%10):
            return False
        i=i//10
        cn=cn//10
    return True

def test_is_antipalindrome():
    assert is_antipalindrome(989)==False
    assert is_antipalindrome(11*11)==False
    assert is_antipalindrome(18679)==True
    assert is_antipalindrome(12)==True
    assert is_antipalindrome(8)==False
    assert is_antipalindrome(6754326)==False
    assert is_antipalindrome(12098)==True
    assert is_antipalindrome(10000+876)==True

alpha="0123456789"
def get_base_2(n):
    '''
    Transforma un numar din baza 10 in baza 2 cu ajuutorul unui sir
    de caractere ce are pe pozitia x numarul corespunzator cu aceasta
    input:
    - n
    output:
    - forma numarului in baza 2
    '''
    converted =""
    n2=int(n)
    while n2>0:
        converted+=alpha[n2%2]
        n2=n2//2
    if len(converted)==0:
        return "0"
    return converted[::-1]
def test_get_base_2():
    assert get_base_2(75)=="1001011"
    assert get_base_2(7)=="111"
    assert get_base_2(123)=="1111011"
    assert get_base_2(88)=="1011000"
def rest_modulo16(x:int):
    '''
    calculeaza restul modulo 16
    Input:
    -n un numar de maxim 4 cifre
    output:
    -restul
    '''
    p2=1 #puterea lui 2
    nr=0
    while x:
        nr=x%10*p2+nr
        p2=p2*2
        x=x//10
    return nr

def convert_base2_to_base16(n):
    '''
    Transforma un numar din baza 2 in baza 10
    Input:
    -n numarul din baza 2 pe care il avem de convertit
    Output:
    -numarul convertit in baza 16
    '''
    nr16=""  #numarul in baza 16
    m=int(n)
    while m:
        x=m%10000
        nr=rest_modulo16(x)
        if nr==10:
            cif='A'
        elif nr==11:
            cif='B'
        elif nr==12:
            cif='C'
        elif nr==13:
            cif='D'
        elif nr==14:
            cif='E'
        elif nr==15:
            cif='F'
        else:
            cif=str(nr)
        nr16=cif+nr16
        m=m//10000
    return nr16
def test_convert_base2_to_base16():
    assert convert_base2_to_base16(11111)=='1F'
    assert convert_base2_to_base16(10101010)=='AA'
    assert convert_base2_to_base16(11001010)=='CA'
    assert convert_base2_to_base16(11001111)=='CF'
    assert convert_base2_to_base16(10111001)=='B9'
    assert convert_base2_to_base16(10001110)=='8E'
def main():
    while(True):
        print('7.Verificare antipalindrom.')
        print('8.Transformarea unui numar din baza 10 in baza 2.')
        print('9.Transformarea unui numar din baza 2 in baza 16.')
        print('X.Iesire din program.')
        optiune= input('Alege optiunea : ')
        if optiune=='7':
            test_is_antipalindrome()
            n=int(input('Dati un numar : '))
            if(is_antipalindrome(n)):
                print('Numarul introdus este antipalindrom.')
            else:
                print('Numarul introdus nu este antipalindrom.')
        elif optiune=='8':
            test_get_base_2()
            print(get_base_2(input('Dati un numar : ')))
        elif optiune=='9':
            test_convert_base2_to_base16()
            print(convert_base2_to_base16(input('Dati un numar : ')))
        elif optiune=='X':
            break
        else:
            print('Alegere invalida.')
main()
