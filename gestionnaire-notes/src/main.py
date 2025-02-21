import argparse
from src.services.note_manager import NoteManager

def main():
    parser = argparse.ArgumentParser(description="Gestionnaire de Notes")
    subparsers = parser.add_subparsers(dest="command")

    create_parser = subparsers.add_parser("create", help="Créer une nouvelle note")
    create_parser.add_argument("titre", help="Titre de la note")
    create_parser.add_argument("contenu", help="Contenu de la note")

    delete_parser = subparsers.add_parser("delete", help="Supprimer une note")
    delete_parser.add_argument("titre", help="Titre de la note")

    args = parser.parse_args()

    manager = NoteManager()

    if args.command == "create":
        manager.creer_note(args.titre, args.contenu)
        print(f"Note '{args.titre}' créée avec succès.")
    elif args.command == "delete":
        manager.supprimer_note(args.titre)
        print(f"Note '{args.titre}' supprimée avec succès.")
    else:
        parser.print_help()

if __name__ == "__main__":
    main()