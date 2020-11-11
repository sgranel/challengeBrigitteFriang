import urllib3
http = urllib3.PoolManager()

const = ["0","1","2","3","4","5","6","7","8","9","a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]

i = 0
while i < len(const):
    j  = 0
    while j < len(const):
        url = 'https://challengecybersec.fr/1410e53b7550c466c76fc7268a8160ae/'+const[i]+'f39'+const[j]+'9527e73ad93b73b070bb12cde1292bbcde5'
        r = http.request('GET', url)
        if r.status == 404:
            print('Essaie : ' +url)
        else :
            print(url)
            i = len(const)
            j = len(const)
        j = j + 1
    i = i + 1

print('finie')