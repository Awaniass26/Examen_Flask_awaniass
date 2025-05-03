J'ai cree une TODO list.
Tout d'abord on a la page de connexion avec nom d'utilisateur et mot de passe (base de donnees mysql : 
username: root et mdp:   ) , si on est pas inscrit , on ne peut pas se connecter alors il faudrait d'abord 
s'inscrire puis retourner vers la page de connexion pour se connecter et acceder a sa todolist
Alors j'ai creer un user : Aly et mdp: breukh.
Vous pouvez essayez de creer un user et vous connecter , vous aurez accez a votre todolist avec un crud complet
c'est a dire qu'on peut creer une tache , l'afficher dans la liste , la modifier ou la supprimer 
L'ajout et la modification se font via le meme popup
On peut filtrer la liste (tout , complete ou incomplete) , la pagination est aussi disponible, la limite par page 
est 6 .
Lorsqu'une tache est achevee , on a la possibilite de la cocher (checkbox) et non seulement elle se desactive mais 
aussi ell est barree.
Le formulaire searchnote : on peut rechercher une tache de notre todolist , si cette derniere n'est pas presente dans 
la liste, on t'affiche une image error 404 , cette tache n'est pas trouve (vous pouvez essayer de rechercher , rien 
qu'en commencant par une lettre , vous saurez si elle est presente ou pas)

Voila en gros ce sont toutes les fonctionnalites du projet sans oublier le bouton de deconnexion biensur sur le navbar.
Merci.