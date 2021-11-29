# 1 Uzduotis, 8 variantas
# Bazine funkcija - Vienanariu
# Funckija = (ln(x) / (sin(2x) + 1.5)) + x/5
# intervalas 2 <= x <= 10

import numpy as np
import matplotlib.pyplot as plot

def fx(x):
    return (np.log(x) / (np.sin(2*x) + 1.5)) + x/5

#intervalas
xmin = 2
xmax = 10

N = 15 # Tasku skaicius

# tolygiai pasiskirste taskai
X = np.linspace(xmin, xmax, N)

# Ciobysevo taskai
i = np.arange(0, N)
Xc = ((xmax - xmin) / 2) * np.cos(np.pi * (2 * i + 1) / (2 * N)) + ((xmax + xmin) / 2)

def interpolate(x, n):
    # bazine funkcija
    bazineMat = []
    ones = np.ones(n)
    for i in range(n):
        bazineMat.append(ones)
    bazineMat = np.matrix(bazineMat).astype(float)

    for i in range(0, n):
        for j in range(1, n):
            bazineMat[i, j] = x[i] ** j

    f = fx(x)
    f.shape = (n, 1)
    A = (bazineMat**-1) * f
    return A

print("Tolygiai pasiskirste taskai:")
A = interpolate(X, N)
A.shape = (1, N)
A = np.array(A)
A = A[0]
print(A)
print("Ciobysevo taskai:")
Ac = interpolate(Xc, N)
Ac.shape = (1, N)
Ac = np.array(Ac)
Ac = Ac[0]
print(Ac)


Y = [];
YC = [];
Y_NET = [];
YC_NET = [];
x = np.linspace(xmin, xmax, 1000)
for j in range(len(x)):
    y = 0;
    yc = 0;
    for k in range(N):
        y +=(x[j]**k)*A[k]
        yc +=(x[j]**k)*Ac[k]
    Y.append(y)
    YC.append(yc)
    Y_NET.append(fx(x[j])-y)
    YC_NET.append(fx(x[j])-yc)

ciobysevas = True

if ciobysevas:
    fja = plot.plot(x, fx(x)) # duota f-ja
    ciob = plot.plot(Xc, fx(Xc), 'bo') # taskai pagal cebyseva
    ciobInter = plot.plot(x, YC) # interpoliavimas per ciobyseva paskirsciusius taskuss
    ciobNet = plot.plot(x, YC_NET) # netikitis interpoliuojant per ciobyseva pasiskirsciusus taskus
    plot.legend([fja, ciob, ciobInter, ciobNet], labels=['Funkcija', 'Taškai', 'Interpoliuojanti kreivė', 'Netektis'], title='Čiobyšebo abscisės')
    plot.title('Pagal Čiobyševo taškus')
else:
    fja = plot.plot(x, fx(x)) # duota f-ja
    taskai = plot.plot(X, fx(X), 'ro')  # tolygiai pasiskirste taskai
    interpolTask = plot.plot(x, Y) # interpoliavimas per tolygiai paskirsciusius taskuss
    netikTask = plot.plot(x, Y_NET) # netikitis interpoliuojant per tolygiai pasiskirsciusus taskus
    plot.legend([fja, taskai, interpolTask, netikTask], labels=['Funkcija', 'Taškai', 'Interpoliuojanti kreivė', 'Netektis'])
    plot.title('Pagal tolygiai pasiskirsčiusius taškus')
plot.ylim(-10,10)
plot.show()