import numpy as np
import matplotlib.pyplot as plot

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

def g(m, x):
    G = np.zeros((len(x),m), dtype="float")
    for i in range(len(x)):
        for j in range(m):
            G[i][j] = x[i]**j
    return G

def fx(x, koef):
    y=0
    koef = koef.flatten()
    expr=""
    for i in range(len(koef)):
        y+= koef[i]*(x**i)
        if i < len(koef)-1:
            temp="{koef:e}*x^{deg:d}".format(koef=koef[i], deg=i)
            expr+=temp+"+"
        else:
            temp="{koef:e}*x^{deg:d}".format(koef=koef[i], deg=i)
            expr+=temp
    print("\n%d-os eilės daugianaris"%(len(koef)-1))
    print(expr)
    return y

years= [data[i]['Year'] for i in range(len(data))]
emissions= [data[i]['Emission'] for i in range(len(data))]

def approx(m):
    x = np.arange(0, 21)
    G = g(m, x)
    Gtranspose = G.T
    # Koeficientai
    temp = Gtranspose.dot(G)
    temp2 = Gtranspose.dot(emissions)
    koef = np.linalg.solve(temp, temp2)
    print(koef)
    return koef

pirma = approx(2)
antra = approx(3)
trecia = approx(4)
penkta = approx(6)

xx=np.linspace(0, 21, 500)
taskai = plot.plot(years, emissions, "ro")
plot1 = plot.plot(xx+1998, fx(xx, pirma))
plot2 = plot.plot(xx+1998, fx(xx, antra))
plot3 = plot.plot(xx+1998, fx(xx, trecia))
plot5 = plot.plot(xx+1998, fx(xx, penkta))
plot.legend([taskai, plot1, plot2, plot3, plot5], labels = ['Taškai', 'Pirmo lygio', 'Antro lygio', 'Trečio lygio', 'Penkto lygio'])
plot.xlabel('Metai')
plot.ylabel('Emisijos')
plot.title('Austrijos šiltnamio dujų duomenys')
plot.show()
