import os
import yaml
import argparse
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

def main():
    parser = argparse.ArgumentParser(description="Gestionnaire de Notes Avancé")
    subparsers = parser.add_subparsers(dest="command")

    create_parser = subparsers.add_parser("create", help="Créer une note")
    create_parser.add_argument("titre", help="Titre de la note")
    create_parser.add_argument("contenu", help="Contenu de la note")
    create_parser.add_argument("--categorie", help="Catégorie de la note", default=None)
    create_parser.add_argument("--tags", nargs="*", help="Tags associés", default=[])

    delete_parser = subparsers.add_parser("delete", help="Supprimer une note")
    delete_parser.add_argument("titre", help="Titre de la note")

    args = parser.parse_args()
    manager = NoteManager()

    if args.command == "create":
        note = manager.creer_note(args.titre, args.contenu, args.categorie, args.tags)
        print(f"Note '{args.titre}' créée avec succès sous la catégorie '{args.categorie}' avec les tags {args.tags}.")
    elif args.command == "delete":
        manager.supprimer_note(args.titre)
        print(f"Note '{args.titre}' supprimée avec succès.")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()
