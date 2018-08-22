def checkio(data: str) -> bool:

    #replace this for solution
    upper = False
    lower = False
    if len(data) >= 10 and len(data) <=64 and not data.isalpha() and not data.isdigit():
        for i in data:
            if i.isupper():
                upper = True
            if i.islower():
                lower = True
    if upper and lower:
        return True
    else:
        return False

#Some hints
#Just check all conditions


if __name__ == '__main__':
    #These "asserts" using only for self-checking and not necessary for auto-testing
    assert checkio('A1213pokl') == False, "1st example"
    assert checkio('bAse730onE4') == True, "2nd example"
    assert checkio('asasasasasasasaas') == False, "3rd example"
    assert checkio('QWERTYqwerty') == False, "4th example"
    assert checkio('123456123456') == False, "5th example"
    assert checkio('QwErTy911poqqqq') == True, "6th example"
    print("Coding complete? Click 'Check' to review your tests and earn cool rewards!")

"""   Stephan and Sophia forget about security and use simple passwords for everything. 
Help Nikola develop a password security check module. 
The password will be considered strong enough if its length is greater than or equal to 10 symbols, it has at least one 
digit, as well as containing one uppercase letter and one lowercase letter in it. The password contains only ASCII latin letters or digits.

Input: A password as a string.

Output: Is the password safe or not as a boolean or any data type that can be converted and 
processed as a boolean. In the results you will see the converted results.

How it is used: If you are worried about the security of your app or service, you can check your users' 
passwords for complexity. You can use these skills to require that your users passwords meet more conditions (punctuations or unicode).

Precondition:
re.match("[a-zA-Z0-9]+", password)
0 < len(password) ≤ 64 """