olom = 18 # cm^3
rez = 23 # cm^3
suruseg_olom = 11.34 # g/cm^3
suruseg_rez = 8.69 # g/cm^3

tomeg_olom = olom * suruseg_olom
tomeg_rez = rez * suruseg_rez
print(tomeg_olom > tomeg_rez)