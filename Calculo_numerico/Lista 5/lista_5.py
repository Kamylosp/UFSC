import numpy as np
tol = 9.3132257e-10

# Questão 1
def newton (f, f_p, x):
    return x - f(x)/f_p(x)

# Questão 2
def lista_5_ex_2 (p):
    t, t_anterior = 1, 0

    while abs((t-t_anterior)/t) > tol:
        t_anterior = t

        Q = (75*np.exp(-1.5*t) + 20*np.exp(-0.075*t))/95 - p
        Q_ = -1.18421/np.exp(1.5*t) - 0.0157895/np.exp(0.075*t)

        t = t - Q/Q_

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
    
# Questão 4
R = 0.518
T = 273.15 - 40

def lista_5_ex_4 (temp_crit, pres_crit):

    a = (0.427 * (R*R) * np.power(temp_crit, 2.5)) / (pres_crit)
    b = (0.0866 * R * temp_crit) / (pres_crit)

    # Cálculo do chute inicial, com análise gráfica
    delta=0.1
    v = b+delta
    while (R*T)/(v - b) - a / (v * (v+b) * np.sqrt(T)) - 65000 <0:
        delta/=2
        v = b+delta

    while abs(delta) > tol:

        f = (R*T)/(v - b) - a / (v * (v+b) * np.sqrt(T)) - 65000
        f_ = (a*(b + 2*v)) / (np.sqrt(T) * (v**2) * ((b+v)**2)) - (R*T) / ((b-v)**2)

        delta = (f/f_)
        v = v - delta

    return(3/v)


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

        while abs((j-j_anterior)/j) > tol:
            j_anterior = j
            j = j - Q5_f(valor, j, tempo, prestacao)/Q5_f_(valor, j, tempo, prestacao)

        return j

    elif not tempo:
        return abs(np.log(1- valor*juros/prestacao) / np.log(1+juros))

    elif not prestacao:
        return valor / ( (1-1/np.power(1+juros, tempo)) / juros)


# Questão 6
def l(n):
    if (n==1):
        return 0
    return n*l(n-1) + 3*(n-1) + 2

def lista_5_ex_6_lap(t):
    n_operacoes = t* 1.0e8
    i = 1

    while n_operacoes - l(i)  > 0: i += 1

    return(i-1)

def l2(n):
    return (n-1)*(4*n*n + n + 6)/6

def lista_5_ex_6_esc(t):
    n_operacoes = t* 1.0e8

    delta = 10000
    n = 100000

    while delta >= 1:
        while (n_operacoes - l2(n)) > 0: n += delta
        
        while (n_operacoes - l2(n)) < 0: n -= delta
        
        delta /= 10
    
    return n