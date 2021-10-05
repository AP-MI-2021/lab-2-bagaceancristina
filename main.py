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

def main():
    while(True):
        print('7.Verificare antipalindrom.')
        print('8.Transformarea unui numar din baza 10 in baza 2.')
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
        elif optiune=='X':
            break
        else:
            print('Alegere invalida.')
main()
