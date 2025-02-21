import yaml
from datetime import datetime

class Note:
    def __init__(self, titre, contenu, categorie=None, tags=None, auteur="Utilisateur"):
        self.titre = titre
        self.contenu = contenu
        self.categorie = categorie
        self.tags = tags if tags else []
        self.auteur = auteur
        self.date_creation = datetime.now().strftime("%Y-%m-%d")
        self.date_modification = self.date_creation
        self.version = 1.0

    def to_dict(self):
        return {
            "titre": self.titre,
            "contenu": self.contenu,
            "categorie": self.categorie,
            "tags": self.tags,
            "auteur": self.auteur,
            "date_creation": self.date_creation,
            "date_modification": self.date_modification,
            "version": self.version,
        }

    def to_yaml(self):
        return yaml.dump(self.to_dict(), default_flow_style=False)

    def save(self, dossier="data"):
        filename = f"{dossier}/{self.titre}.md"
        with open(filename, "w") as f:
            f.write("---\n")
            f.write(self.to_yaml())
            f.write("---\n")
            f.write(self.contenu)