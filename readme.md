# Docker

### lancer docker

docker-compose up -d

### afficher les paquets

docker ps

### redémarrer les paquets

docker-compose restart

### supprimer les paquets

docker-compose down

## Oddo par la pratique

Afficher la date
str(datetime.datetime.now().year)

Afficher le nom de ma société
<span t-esc="website.company_id.name"/>