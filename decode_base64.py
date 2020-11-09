# En parcourant la chaine carac(tère par caractère :
import base64

base64_file  = open('message_recuperere_without_start_v2.txt', 'r')
base64_original = base64_file.read()
data_clear =base64.b64decode(base64_original)
print(data_clear)

msg_file = open('message_decode.txt', 'w')
msg_file.write(str(data_clear))
msg_file.close()