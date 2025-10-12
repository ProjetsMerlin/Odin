# Odin

## Introduction
Odin est un module Odoo qui affiche une one-page dynamique et prêt à l'empploi.
Une fois le module installé, vous pouvez appeler le template "Odin" (<t t-call="odin" />) sur votre page principale pour obtenir un one-page dynamique.
L'idée est d'avoir un site prêt à l'emploi en attendant un site plus conséquant comme un multipage et en plusieurs langues par exemple.

## Contenu dynamique

Voilà la liste du contenu éditable depuis le dashborad d'Odoo : 

### Introduction
Le texte et le sous-titre sont éditable via une menu accessible si connecté, et nommé "contenu site"
<t t-set="paragraph" t-value="request.env['website.paragraph.text'].sudo().search([], limit=1)">

### Team
Boucle sur les utilisateurs de la plateforme (nom, email, website et avatar)
<t t-set="users" t-value="request.env['res.users'].sudo().search([('partner_id.function', '!=', False)])"/>

### Footer
Afficher de l'année courrante + le nom de la société
<t t-esc="datetime.datetime.now().year"/>
<span t-esc="website.company_id.name" />

### commerce : Boucle sur les produits de la plateforle (image, titre & description)

### newsletter & réseaux sociaux ?

### 404 pages

### Banner cookies ?

### e-commerce (image, titre & description)

## feature sections

Connexion API

## Memo command

### lancer docker

docker-compose up -d

### afficher les paquets

docker ps

### redémarrer les paquets

docker-compose restart

### supprimer tous les paquets

docker-compose down

### redmérarrer un conteneur spécifique
docker exec -it odin-odoo-1 odoo -u odin

## Résumé des opérateurs utiles dans search :
Opérateur Odoo	Signification
'='	Égal
'!='	Différent
'in'	Dans une liste
'not in'	Pas dans une liste
'ilike'	Contient (insensible à la casse)
'=', False	Vide / champ nul