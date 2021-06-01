from filme import Filme, Serie, Playlist


filme = Filme("A culpa é das estrelas", 2019, 160)

serie  = Serie ("vikings", 2014, 7)

programas = [filme, serie]

print ("Tamanho da playlist: {}". format(len(programas)))
for item in programas:
    print(item)
