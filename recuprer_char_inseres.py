# En parcourant la chaine carac(tère par caractère :

original_file  = open('original.txt', 'r')
intercept_file = open('intercepte.txt', 'r')
msg_file = open('message_recuperere.txt', 'w')
chaine_original = original_file.read()
chaine_intercepte = intercept_file.read()
msg = []

j = 0;
for i in range(len(chaine_original)):
    # Note : dans votre code vous faisiez 'for i in chaine:'. i est alors de type str et non int donc chaine[i] va générer une erreur.
    # https://docs.python.org/3.4/library/functions.html#func-range
    if(chaine_original[i] != chaine_intercepte[j]):
        msg.append(chaine_intercepte[j]);
        j = j+1;
    j = j +1
    
print(''.join(msg))

msg_file.write(''.join(msg))
msg_file.close()