# src/exceptions/note_exceptions.py
class NoteError(Exception):
    pass

class NoteNotFoundError(NoteError):
    pass

class InvalidNoteFormatError(NoteError):
    pass