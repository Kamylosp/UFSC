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

print(lista_5_ex_3(1, 100, 50))

# Questão 4

def Q4_f(v, a, b):
    return (120.7717)/(v - b) - a/(v*(v+b)*np.sqrt(233.15)) - 65

def Q4_f_(v, a, b):
    return -120.772/np.power(v - b, 2) - (a/np.sqrt(233.15))* (b+2*v)/((v*v) * (b+v)**2)


def Q4_a(Tc, Pc):
    return 0.114574348 * np.power(Tc, 2.5) / Pc

def Q4_b(Tc, Pc):
    return 0.0448588 * Tc / Pc

def lista_5_ex_4 (temp_crit, pres_crit):
    a = Q4_a(temp_crit, pres_crit)
    b = Q4_b(temp_crit, pres_crit)

    print("a: ", a)
    print("b: ", b)

    v, v_anterior = 0.5, 0

    print("f(): ", Q4_f(v, a, b))
    print("f'(): ", Q4_f_(v, a, b))

    while abs((v-v_anterior)/v) > tol:
        print("v: ", v)
        v_anterior = v
        v = v - Q4_f(v, a, b)/Q4_f_(v, a, b)

    return(3/v)

# temp_cri = 500
# p_cri = 10000

# # print(Q4_f(v, Q4_a(temp_cri, p_cri), Q4_b(temp_cri, p_cri)) + 65000)
# print(lista_5_ex_4(temp_cri, p_cri))

# def teste(v, a, b):
#     return (120.7717)/(v - b) - a/(v*(v+b)*np.sqrt(233.15))

# print(teste(0.00253683, 64.04900765142928, 0.0022429399999999997))