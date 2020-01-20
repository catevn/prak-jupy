'''
Messprotokoll:

1.
Kalibrierquellen:
Am 241
Ba 133
Cs 137

2.
Dicke des Alustabes: 6mm
Fehler auf Messschieber: 0.05 mm

Messzeit: soll 20 min sein
Die Messunsicherheit des Winkels von 90° sind ~2°

3. Zeitoptimierung:
Messzeit: ~1800s
Streumessung:
    linke Grenze des Streupeaks (Kanal): 886
    rechte Grenze des Streupeaks (Kanal): 1033
    Integral: 12935

Untergrund:
    selbe Grenzen
    Integral: 713
'''

# berechne optimale Messzeit:
N_g = 12935
N_0 = 713
t = 1800
rel_unsich = 0.03

t_opt = (N_g/t + N_0/t)/(rel_unsich**2 * (N_g/t - N_0/t)**2)
print(t_opt)
delta_t_opt = (((((N_g/t + 3*N_0/t)**2 * N_g/(t**2))) + ((N_0/t + 3*N_g/t)**2 * N_0/(t**2)))**0.5)/(rel_unsich**2 * (N_g/t - N_0/t)**3)
print(delta_t_opt)
print("relativer Fehler von t_opt:", (delta_t_opt/t_opt)*100, "%")

'''
4. Messung der Winkelabhängigkeit
Wir messen in Winkeln von 30° bis 130° in 10° Schritten.
Die Messunsicherheit des Winkels ist wieder ~2°

6. Einfluss des Streukörperdurchmessers
Durchmesser: 2mm
             (6mm)
             8mm
             15mm
             20mm
             Unsicherheit wieder 0.05mm
'''

# --> wir messen mindestens 185 s
