#Importovanje ugradjenih paketa
import pandas as pd
import numpy as np

#Kreiranje niza
ocene = np.array([6,7,10,8,6,9,8,7,8,8,9,8,10])

#Kreiranje indeksiranog jednodimenzionalnog niza
s = pd.Series(ocene)

#Izracunavanje deskriptivne statistike pomocu postojecih funkcija u okviru paketa Pandas
s.mean()
s.var()
s.std()

s.mode()

s.median()
s.quantile([.25, .75])


s.max()
s.min()
minimum=min(s)
minimum
opseg=s.max()-s.min()
opseg

s.kurt()
s.skew()
s.describe()

#ImporStovanje tacno odredjenih funkcija iz paketa scipy
from scipy.stats import skew,kurtosis
# Izraunavanje skweness-a
print(skew(s, axis=0, bias=True))
# Izracunavanje kurtosisa 
print(kurtosis(s, axis=0, fisher=False))
print(kurtosis(s, axis=0, fisher=True, bias=False))
print(kurtosis(s, axis=0, fisher=True, bias=True))
