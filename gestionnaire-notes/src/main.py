import os
import yaml
import argparse
import shutil
from datetime import datetime
from src.models.note import Note
from src.services.note_manager import NoteManager

class NoteSearchEngine:
    def __init__(self, dossier="data"):
        self.dossier = dossier

    def rechercher_notes(self, query):
        notes_trouvees = []
        for fichier in os.listdir(self.dossier):
            if fichier.endswith(".md"):
                with open(os.path.join(self.dossier, fichier), "r") as f:
                    contenu = f.read()
                    if query.lower() in contenu.lower():
                        notes_trouvees.append(fichier.replace(".md", ""))
        return notes_trouvees

class BackupManager:
    def __init__(self, source="data", backup_dir="backup"):
        self.source = source
        self.backup_dir = backup_dir
        if not os.path.exists(self.backup_dir):
            os.makedirs(self.backup_dir)
    
    def creer_sauvegarde(self):
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        backup_path = os.path.join(self.backup_dir, f"backup_{timestamp}")
        shutil.copytree(self.source, backup_path)
        print(f"Sauvegarde créée : {backup_path}")

def afficher_menu():
    print("\nMenu Principal")
    print("1. Créer une note")
    print("2. Supprimer une note")
    print("3. Rechercher une note")
    print("4. Créer une sauvegarde")
    print("5. Quitter")

def main():
    manager = NoteManager()
    search_engine = NoteSearchEngine()
    backup_manager = BackupManager()

    while True:
        afficher_menu()
        choix = input("\nSélectionnez une option: ")

        if choix == '1':
            titre = input("Titre: ")
            contenu = input("Contenu: ")
            categorie = input("Catégorie (facultatif): ")
            tags = input("Tags (séparés par des espaces, facultatif): ").split()
            note = manager.creer_note(titre, contenu, categorie, tags)
            print(f"Note '{titre}' créée avec succès sous la catégorie '{categorie}' avec les tags {tags}.")
        elif choix == '2':
            titre = input("Titre de la note à supprimer: ")
            manager.supprimer_note(titre)
            print(f"Note '{titre}' supprimée avec succès.")
        elif choix == '3':
            query = input("Terme de recherche: ")
            resultats = search_engine.rechercher_notes(query)
            if resultats:
                print("Notes trouvées:")
                for note in resultats:
                    print(f"- {note}")
            else:
                print("Aucune note ne correspond à la recherche.")
        elif choix == '4':
            backup_manager.creer_sauvegarde()
        elif choix == '5':
            print("Merci d'avoir utilisé le gestionnaire de notes. À bientôt! ( Mettez moi une bonne note 🙏🏽 )")
            break
        else:
            print("Option invalide. Veuillez réessayer.")

if __name__ == "__main__":
    main()
