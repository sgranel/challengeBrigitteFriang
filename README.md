# Challenge Brigitte Friang

## Résumé
Après le challenge Richelieu, la DGSE a mis en ligne un nouveau challenge qui a lieu du 24/10/2020 au 11/11/2020.

On y accédait depuis le site https://challengecybersec.fr/

## Entrée dans le challenge.
En tapant l'url, nous arrivons sur la page suivante : ![Accueil](https://raw.githubusercontent.com/sgranel/challengeBrigitteFriang/main/Capture1.PNG?token=AG2F56EOUMQRDTGERQDUPFK7TAQI2)

Nous affichons le code source de la page afin de trouver des indices: ![CodeSource](https://raw.githubusercontent.com/sgranel/challengeBrigitteFriang/main/Capture2.PNG?token=AG2F56FJXFUL7KDV7M65WB27TAQ4G) 
Là, on voit une ligne commentée `/static/message-secret.html`

En tapant cette url dans le navigateur, nous arrivons sur la page suivante : ![Cesar](https://raw.githubusercontent.com/sgranel/challengeBrigitteFriang/main/Capture3.PNG?token=AG2F56B4EGG6U3PQY6754CK7TARDO)
Nous remarquons trois choses en arrivant sur la page : tout d'abord, la présence de 4 caractères en gras : `joha`. Nous les notons et les mettons de coté.
Ensuite, le message en lui-même. En effet, il n'est pas lisible mais n'a pas un chiffrement fort car la structure du texte est conservée, ce qui fait penser au chiffrement de César. Cette hypothèse est confirmée par le troisième point : le titre de la page, qui est Cesar.

Pour ceux qui ne connaissent pas le chiffrement de César, il s'agit d'un décallage de lettres par un nombre compris, entre 1 et 25, choisit par celui qui chiffre. Pour retrouver facilement, le chiffre du décallage, deux techniques s'offrent à nous : 
  * la première est de compter les occurances des lettres présentes dans le message. Celle qui apparait le plus a de grande chance de correspondre au E car c'est la lettre la plus utilisée en français. L'inconvénient de cette technique est qu'elle peut vite devenir longue si on le fait à la main et si le texte comporte des accents à la base, ça gêne cette analyse.
  * la deuxième, celle que j'ai utilisé, est de travailler à partir d'une hypothèse grâce à un mot. J'ai choisi le mot premier mot d'une phrase : `LssL`. Sa structure fait fortement penser au mot 'elle'. Pour vérifier cette hypothèse, on compte le décallage (nombre de lettres) entre le L et le E, ce qui nous donne 7. On fait le même calcule entre S et L, ça nous donne le même résultat. Il semble que nous ayons trouvé la clef.
Pour récupérer le code, il suffit d'utiliser un des nombreux sites qui le propose.
Le résultat est le texte suivant : ![Cesar déchiffré](https://github.com/sgranel/challengeBrigitteFriang/blob/main/Cesar_clair.txt).
 
Le texte nous raconte la vie de Briggite Friang. On y apprend qu'elle cachait des messages dans des foulards et que le texte comporte une url à taper pour accéder à la suite, suivi de la barre oblique.

Ce qui nous ramène aux 4 caractères trouvés avant. En appliquant le déchiffrement de César, on récupère le mot : chat.

En mettant, ce mot dans l'url, nous accédons au site suivant : ![Chat](https://raw.githubusercontent.com/sgranel/challengeBrigitteFriang/main/Capture4.PNG?token=AG2F56AHBHIUNYZQO4HTB2S7TAS2O) 

## Le chat
