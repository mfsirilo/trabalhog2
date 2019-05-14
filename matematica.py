import math
import csv

fx = lambda x: 2**x - 3
fx2 = lambda x:  x**3 + 4*x**2 - 10
fx4 = lambda x: math.cos(x)-x


def bisection_method(fx, a, b, tol, N):
        i = 1
        FA = fx(a)
        try:
            while i <= N:
                p = (a+b)/2.0
                FP = fx(p)
                print(i,': ', 'x:', p, '; f(x):', FP)
                arq = csv.writer(open("bisseccao.csv", 'ab+'))
                arq.writerow([i, p, FP])
                if FP == 0 or (b-a)/2.0 < tol:
                    return p
                i+=1

                if FA*FP > 0:
                    a = p
                else:   
                    b = p
        except:
            return 'The procedure was unsuccessful.'
# abmais 
def fixed_point(p0, g, tol, N):
    i = 1
    try:
        while i <= N:
            p = g(p0)
            print('i:',i, 'p:',p)
            # criacao do arquivo
            arq = csv.writer(open("ponto_fixo.csv", 'ab+'))
            arq.writerow([i, p])
            if math.fabs(p-p0) < tol:
                return p
            i += 1
            p0 = p
    except: print("Error")
    return 'The procedure was unsuccessful'

#
def rewriteB():
    linhas = []
    with open("bisseccao.csv", 'r') as file:
        spamreader = csv.reader(file, delimiter=',')
        for linha in spamreader:
            linhas.append({'iteracao': linha[0], 'x': linha[1], 'f(x)': linha[2]})
        file.close()
    with open("bisseccao.csv", 'wb') as file:
        field = ['iteracao', 'x', 'f(x)']
        writer = csv.DictWriter(file, fieldnames=field)
        writer.writeheader()
        for i in linhas:
            writer.writerow(i)

# Ponto Fixo
# RESCREVENDO O ARQUIVO 
def rewriteP():
    linhas = []
    with open("ponto_fixo.csv", 'r') as file:
        spamreader = csv.reader(file, delimiter=',')
        for linha in spamreader:
            linhas.append({'iteracao': linha[0], 'x': linha[1]})
        file.close()
    with open("ponto_fixo.csv", 'wb') as file:
        field = ['iteracao', 'x']
        writer = csv.DictWriter(file, fieldnames=field)
        writer.writeheader()
        for i in linhas:
            writer.writerow(i)

f = lambda x: x**3 - (9*x) - 3

# bisection_method(f, 280, 300, 0.0000000000000000000000000000000001, 200)
bisection_method(f, 1.0, 2.0, 0.000000000000000000001, 47)


# rewrite()
# print(bisection_method(f2, 280, 300, 0.0000000001, 200))
# print(fixed_point(0, f2, 0.0000000000000001, 1000))
#fixed_point(280, f2, 0.0000000000000000000000000000000000001, 2000)
#rewriteP()
rewriteB()
# print(bisection_method(f2, 0, 1, 0.0000001, 200))

# symbolab - site de criacao de funcao