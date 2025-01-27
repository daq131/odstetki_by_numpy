# Porównanie odsetek kredytowych
import numpy_financial as npf
import numpy as np

freq = 12
rate = 0.0675
years = 30
pv = 200000

rate /= freq  # konwersja stopy do okresu miesięcznego
print(rate)
nper = years * freq  # liczba wszystkich okresów
print(nper)
# licznik płatności
periods = np.arange(1,nper+1,dtype=int)
print(periods)
# część odstetkowa raty w płatnościach równych
interest_equal = - np.around(npf.ipmt(rate,periods,nper,pv),2)
print(interest_equal[:10])
# część odstekowa - raty malejące
np.set_printoptions(suppress=True)

principal_decreasing = np.around(np.zeros(nper)+(pv/nper),2)
print(principal_decreasing[:10])
# bilans końcowy transakcji
balance = np.zeros(nper) + pv
# bilans otwarcia (końcowy :)
balance_close = np.around(balance - np.cumsum(principal_decreasing),2)
print(balance_close[[0,1,2,-3,-2,-1]])
