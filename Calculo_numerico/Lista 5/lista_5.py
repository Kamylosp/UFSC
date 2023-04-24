import numpy as np
tol = 9.3132257e-10

# Questão 1
def newton (f, f_p, x):
    return x - f(x)/f_p(x)


# Questão 2
def Q2_f(t, p):
    return 75*np.exp(-1.5*t) + 20*np.exp(-0.075*t)/95 - p

def Q2_f_(t):
    return (-112.5/np.exp(1.5* t) - 1.5/np.exp(0.075* t))/95

def lista_5_ex_2 (p):
    t, t_anterior = 2, 0

    while abs((t-t_anterior)/t) > tol:
        t_anterior = t
        t = t - Q2_f(t, p)/Q2_f_(t)

    return t

# Questão 3
def Q3_f(M, c, v, t):
    return (9.81*M/c)*(1-np.exp(-(c/M)*t)) - v

def Q3_f_(M, c, t):
    return (9.81 - 9.81/np.exp((c*t)/M))/c - (9.81*t)/(np.exp((c *t)/M)*M)

def lista_5_ex_3 (c, v, t):
    M, M_anterior = 10, 1

    while abs((M-M_anterior)/M) > tol:
        M_anterior = M
        M = M - Q3_f(M, c, v, t)/Q3_f_(M, c, t)

    return M

# print(lista_5_ex_3(1, 100, 50))



# Questão 4
R = 0.518
T = 273.15 - 40
p = 65000

def Q4_f(v, a, b):
    return (R*T)/(v - b) - a/(v*(v+b)*np.sqrt(T)) - p

def Q4_f_(v, a, b):
    return -(R*T)/np.power(v - b, 2) - (a/np.sqrt(T)) * (b+2*v)/((v*v) * (b+v)**2)


def Q4_a(Tc, Pc):
    return 0.727*(R**2) * np.power(Tc, 2.5) / Pc

def Q4_b(Tc, Pc):
    return 0.0866 * R * Tc / Pc

def lista_5_ex_4 (temp_crit, pres_crit):
    a = Q4_a(temp_crit, pres_crit)
    b = Q4_b(temp_crit, pres_crit)

    print("a: ", a)
    print("b: ", b)

    v, v_anterior = 0.006, 0

    # print("f(): ", Q4_f(v, a, b))
    # print("f'(): ", Q4_f_(v, a, b))

    while abs((v-v_anterior)/v) > tol:
        # print("v: ", v)
        v_anterior = v
        v = v - Q4_f(v, a, b)/Q4_f_(v, a, b)

    return(3/v)

temp_cri = 500
p_cri = 10000

# print(Q4_f(v, Q4_a(temp_cri, p_cri), Q4_b(temp_cri, p_cri)) + 65000)
# print(lista_5_ex_4(temp_cri, p_cri))

# def teste(v, a, b):
#     return (120.7717)/(v - b) - a/(v*(v+b)*np.sqrt(233.15))

# print(teste(0.00253683, 64.04900765142928, 0.0022429399999999997))


# Questão 5
def Q5_f(q, j, n, p):
    return (1- 1/np.power(1+j, n))*p / j - q

def Q5_f_(q, j, n, p):
    return ((-1 + 1/np.power(1 + j, n) + j * 1/np.power(1 + j, 1+n) * n)* p) / (j**2)

def calculadora_do_cidadao (valor = None, juros = None, tempo = None, prestacao = None):
    if not valor:
        return (1 - np.power(1+juros, - tempo)) * (prestacao) / (juros)
    
    elif not juros:
        j, j_anterior = 0.001, 0

        # print(Q5_f(valor, j, tempo, prestacao), Q5_f_(valor, j, tempo, prestacao))

        while abs((j-j_anterior)/j) > tol:
            j_anterior = j
            j = j - Q5_f(valor, j, tempo, prestacao)/Q5_f_(valor, j, tempo, prestacao)

        return j

    elif not tempo:
        return abs(np.log(1- valor*juros/prestacao) / np.log(1+juros))

    elif not prestacao:
        return valor / ( (1-1/np.power(1+juros, tempo)) / juros)



# Questão 6