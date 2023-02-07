# You are the hero

Have you ever played with a RPG book "You are the hero" ?

I found some pdf, i try to parse them and make it an api

____


So i downloaded a bunch of books "You are the hero" (in french)
at this address https://bibl.remz.ca/

only 'Defi fantastiques' for now

run 
`python main.py <book.pdf>`

to get a usable json like :

```json

# book.json
{
  "title": " La Citadelle du Chaos",
  "1": {
    "text": "Le soleil se couche ; et tandis que l'obscurit\u00e9 s'installe, vous \nentreprenez l'escalade de la montagne en direction de la silhouette \nmena\u00e7ante qui se dresse dans la nuit. La Citadelle du Chaos se trouve \u00e0 \nmoins d'une heure  de marche.  \u00c0 quelque distance des remparts, vous \nvous arr\u00eatez pour vous reposer et la Citadelle vous semble alors un \nimmense et redoutable fant\u00f4me auquel il serait impossible d'\u00e9chapper.  \nVous contemplez cette masse imposante et un frisson de peur vous \nparcourt l'\u00e9chin\u00e9.  Vous avez honte cependant d'\u00e9prouver cette crainte \net, avec une froide d\u00e9termination, vous continuez \u00e0 grimper jusqu'au \nportail d'entr\u00e9e dont vous savez qu'il est surveill\u00e9 par des gardes. En \nm\u00eame temps, vous r\u00e9fl\u00e9chissez \u00e0 ce que vous all ez dire. Vous avez \npens\u00e9 \u00e0 vous faire passer pour un herboriste venu soigner l'un des \ngardes atteint de fi\u00e8vre. Vous pourriez \u00e9galement vous pr\u00e9senter \ncomme un marchand ou un artisan - un charpentier par exemple.  \nVous pourriez m\u00eame vous pr\u00e9tendre un vagab ond en qu\u00eate d'un abri \npour la nuit.  Tout en r\u00e9fl\u00e9chissant \u00e0 ces trois mensonges, vous atteignez \nle sentier qui m\u00e8ne au portail. Deux flambeaux br\u00fblent de chaque c\u00f4t\u00e9 \nde la herse.  \u00c0 mesure que vous avancez, vous percevez des \ngrognements \u00e9touff\u00e9s et vous di stinguez bient\u00f4t deux cr\u00e9atures \nhybrides. \u00c0 gauche, il s'agit d'un animal repoussant \u00e0 la t\u00eate de chien \npos\u00e9e sur un corps de grand singe.  Du c\u00f4t\u00e9 oppos\u00e9 se tient son contraire \n: un monstre \u00e0 t\u00eate de singe et au corps de molosse. Ce dernier s'avance \nvers v ous, s'arr\u00eate \u00e0 quelques m\u00e8tres, puis, se dressant sur ses pattes de \nderri\u00e8re, vous demande qui vous \u00eates. Quelle r\u00e9ponse allez -vous faire ?  \nPr\u00e9tendre \u00eatre un herboriste ?   Rendez -vous au  261 \nVous faire passer pour un marchand ?  Rendez -vous au  230 \nDemander l'hospitalit\u00e9 pour la nuit ?   Rendez -vous au  20 \n \n",
    "options": [
      261,
      230,
      20
    ]
  },
  "2": {
    "text": "Un peu plus loin dans le passage, \u00e0 droite, se trouve une porte sur \nlaquelle sont trac\u00e9es d'\u00e9tranges inscriptions dans une langue inconnue. \nAllez -vous essayer d'ouvrir la porte (rendez -vous au  142), ou pr\u00e9f\u00e9rez -\nvous poursuivre votre chemin (rendez -vous au  343)  \n",
    "options": [
      142,
      343
    ]
  },
  # ...
}
```

You can now display the game with something like this
(just to get an idea)
```

print(book.json['1'])

# You are in a forest, 
# go left => 15
# go right => 21

print(book.json['1']['options']

# [15, 21]

next = get_user_input() # 15

print(book.json['next'])

```
