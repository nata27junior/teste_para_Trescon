""""Dear applicant,
This technical test is for the full time position as Python/Django backend developer in ZINA Development
team, please read it carefully and follow all the instructions in order to apply to this job position:
To pass this test you must write a Python script to solve the next mathematical problem,
You can use any library you need to acomplish this task. Please try to solve the test. Do not copy the
solution from INTERNET, this may lead you to be disqualified.
Problem:
Working from left-to-right if no digit is exceeded by the digit to its left it is called an increasing number;
for example, 134468. Similarly if no digit is exceeded by the digit to its right it is called a decreasing number;
for example, 66420.
We shall call a positive integer that is neither increasing nor decreasing a "bouncy" number;
for example, 155349. Clearly there cannot be any bouncy numbers below one-hundred, but just
over half of the numbers below one-thousand (525) are bouncy. In fact, the least number for which the
proportion of bouncy numbers first reaches 50% is 538.
Surprisingly, bouncy numbers become more and more common and by the time we reach 21780 the
proportion of bouncy numbers is equal to 90%.
Find the least number for which the proportion of bouncy numbers is exactly 99%.
Please host the solution in a git cloud based repository like Github/Gitlab/Bitbucket as a public repository
and send us the URL so we can analyse your code. Add a requirements.txt file if you are using any
third party library and add a Readme.md explaining how to run your solution.
Best regards,
ZINA Team Development"""



def incrementa(numero):
    flag = True
    strNumero = str(numero)
    for i in range(len(strNumero)-1):
        if int(strNumero[i]) > int(strNumero[i+1]):
            flag = False
            break
    return flag
def decrementa(numero):
    flag = True
    strNumero = str(numero)
    for i in range(len(strNumero)-1):
        if int(strNumero[i]) < int(strNumero[i+1]):
            flag = False
            break
    return flag
def Numerosaltitante():
    contador = 0
    percentagemContador = 0
    n = 99
    while percentagemContador != 99:   
        n = n + 1
        if incrementa(n) == False and decrementa(n) == False:
            contador += 1
        percentagemContador = (contador*100)/n
    return n

if __name__ == '__main__':
    print(f'O menor número é {Numerosaltitante()} para a proporção de números saltitantes for exatamente 99% ')
    
