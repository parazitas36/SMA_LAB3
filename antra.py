import numpy as np
import matplotlib.pyplot as plot

def AkimaSpline(X, Y):
    n = len(X)
    DY = np.zeros(n)
    f = lambda x, xi, xim1, xip1, yi, yim1, yip1: (2 * x - xi - xip1) / ((xim1 - xi) * (xim1 - xip1)) * yim1 + (
                2 * x - xim1 - xip1) / ((xi - xim1) * (xi - xip1)) * yi + (2 * x - xim1 - xi) / (
                                                              (xip1 - xim1) * (xip1 - xi)) * yip1

    for i in range(0, n):
        if i == 0:
            xim1 = X[0]
            xi = X[1]
            xip1 = X[2]
            yim1 = Y[0]
            yi = Y[1]
            yip1 = Y[2]
            DY[i] = f(xim1, xi, xim1, xip1, yi, yim1, yip1)
        elif i == n - 1:
            xim1 = X[n - 3]
            xi = X[n - 2]
            xip1 = X[n - 1]
            yim1 = Y[n - 3]
            yi = Y[n - 2]
            yip1 = Y[n - 1]
            DY[n - 1] = f(xip1, xi, xim1, xip1, yi, yim1, yip1)
        else:
            xim1 = X[i - 1]
            xi = X[i]
            xip1 = X[i + 1]
            yim1 = Y[i - 1]
            yi = Y[i]
            yip1 = Y[i + 1]
            DY[i] = f(xi, xi, xim1, xip1, yi, yim1, yip1)

    return DY

def Hermite(X, j, x):
    N=size(X)
    L=Lagr(X, j, x)
    DL=D_Lagr(X, j, X[j])
    U=(1-2*DL*(x-X[j]))*np.square(L)
    V=(x-X[j])*np.square(L)
    return U,V

def Lagrandis(X, j, x):
    n = len(X)
    L = 1
    for i in range(n):
        if i == j:
            continue
        else:
            L = L * (x - X[i]) / (X[j] - X[i])
    return L


def dLagrandis(X, j, x):
    n = len(X)
    dL = 0
    for i in range(n):
        if i != j:
            Lds = 1
            for k in range(n):
                if k != j and k != i:
                    Lds = Lds * (x - X[k])
        else:
            continue
        dL = dL + Lds
    Ldv = 1

    for k in range(n):
        if k != j:
            Ldv = Ldv * (X[j] - X[k])
    dL = dL / Ldv

    return dL

data = [
    {"Year": 1998, "Emission": 79850},
    {"Year": 1999, "Emission": 78030},
    {"Year": 2000, "Emission": 78240},
    {"Year": 2001, "Emission": 82550},
    {"Year": 2002, "Emission": 83860},
    {"Year": 2003, "Emission": 88940},
    {"Year": 2004, "Emission": 89750},
    {"Year": 2005, "Emission": 89790},
    {"Year": 2006, "Emission": 87470},
    {"Year": 2007, "Emission": 84390},
    {"Year": 2008, "Emission": 83950},
    {"Year": 2009, "Emission": 77000},
    {"Year": 2010, "Emission": 82720},
    {"Year": 2011, "Emission": 80790},
    {"Year": 2012, "Emission": 77570},
    {"Year": 2013, "Emission": 78120},
    {"Year": 2014, "Emission": 74350},
    {"Year": 2015, "Emission": 75480},
    {"Year": 2016, "Emission": 75660},
    {"Year": 2017, "Emission": 77830},
    {"Year": 2018, "Emission": 74980}
    ]

years= [data[i]['Year'] for i in range(len(data))]
emissions= [data[i]['Emission'] for i in range(len(data))]

DY = AkimaSpline(years, emissions)
print(DY)
n = len(years)
nnn = 100

for i in range(n - 1):
    xxx = np.linspace(years[i], years[i + 1], nnn)
    dl = dLagrandis(years[i:i + 2], 0, xxx)
    l = Lagrandis(years[i:i + 2], 0, xxx)
    U0 = (1 - 2 * dl * (xxx - years[i])) * l ** 2
    U1 = (1 - 2 * dLagrandis(years[i:i + 2], 1, xxx) * (xxx - years[i + 1])) * Lagrandis(years[i:i + 2], 1, xxx) ** 2
    V0 = (xxx - years[i]) * l ** 2
    V1 = (xxx - years[i + 1]) * Lagrandis(years[i:i + 2], 1, xxx) ** 2
    yyy = U0 * emissions[i] + V0 * DY[i] + U1 * emissions[i + 1] + V1 * DY[i + 1]

    plot.plot(xxx, yyy, linewidth=3)
    
plot.xticks(np.arange(1998, 2019, 2))

plot.xlabel('Metai')
plot.ylabel('Emisijos')
plot.title('Austrijos šiltnamio dujų duomenys')
plot.plot(years, emissions, "ro")
plot.show()