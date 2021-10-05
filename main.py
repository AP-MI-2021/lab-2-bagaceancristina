def is_antipalindrome(n):
    '''
    determina inversul unui numar si verifica conditia de antipalindrom
    imput:
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


def main():
    test_is_antipalindrome()
    n=int(input('Dati un numar : '))
    if(is_antipalindrome(n)):
        print('Numarul introdus este antipalindrom')
    else:
        print('Numarul introdus nu este antipalindrom')
main()
