import os
from src.models.note import Note
from src.exceptions.note_exceptions import NoteNotFoundError, InvalidNoteFormatError

class NoteManager:
    def __init__(self, dossier="data"):
        self.dossier = dossier
        if not os.path.exists(self.dossier):
            os.makedirs(self.dossier)

    def creer_note(self, titre, contenu, categorie=None, tags=None):
        note = Note(titre, contenu, categorie, tags)
        note.save(self.dossier)
        return note

    def supprimer_note(self, titre):
        filename = f"{self.dossier}/{titre}.md"
        if os.path.exists(filename):
            os.remove(filename)
        else:
            raise NoteNotFoundError(f"La note '{titre}' n'existe pas.")

    def modifier_note(self, titre, nouveau_contenu):
        filename = f"{self.dossier}/{titre}.md"
        if os.path.exists(filename):
            with open(filename, "r") as f:
                lines = f.readlines()
            metadata = "".join(lines[1:lines.index("---\n", 1)])
            contenu = "".join(lines[lines.index("---\n", 1) + 1:])
            note = Note(titre, nouveau_contenu)
            note.save(self.dossier)
        else:
            raise NoteNotFoundError(f"La note '{titre}' n'existe pas.")