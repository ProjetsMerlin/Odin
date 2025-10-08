import os

# Définir la structure du dossier et des fichiers
structure = {
    "odin": {
        "__init__.py": "",
        "__manifest__.py": "",
        "static": {
            "src": {
                "scss": {
                    "odin.scss": "",
                },
                "js": {},
            },
            "description": {
                "icon.png": "",
            },
        },
        "views": {
            "templates.xml": "",
            "assets.xml": "",
        },
    }
}

# Fonction pour créer les fichiers et dossiers récursivement
def create_structure(base_path, structure):
    for name, value in structure.items():
        path = os.path.join(base_path, name)
        
        if isinstance(value, dict):
            # Si c'est un dossier, on le crée
            os.makedirs(path, exist_ok=True)
            # On appelle récursivement la fonction pour créer les sous-dossiers et fichiers
            create_structure(path, value)
        else:
            # Si c'est un fichier, on le crée avec son contenu vide
            with open(path, 'w') as f:
                f.write(value)
            print(f"Fichier créé : {path}")

# Créer la structure dans le dossier actuel
create_structure(".", structure)

print("La structure a été créée avec succès !")