#PyBotTrainer
#03.02.2013 by Georg Dorndorf Licensed under the Creative Common License
#
#Feel free to copy and rewrite the code but please mention my name.

import pickle, sys

b = open(sys.argv[1])
lastword = ''
follow = {}

for line in b:
    for word in line.split():
        if lastword != '':              # word in die nachfolgerliste von lastword einfuegen
            if lastword not in follow:
                working = []
                working.append(word)
                follow[lastword] = working
            else:
                follow[lastword].append(word)
        lastword = word

b.close()

print "\n Lexicon erstellt wird in Datei:lexicon  geschrieben"
a = open('lexicon','wb')
pickle.dump(follow,a,2)
a.close()
