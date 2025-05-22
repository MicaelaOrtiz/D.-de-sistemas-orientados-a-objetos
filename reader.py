class Reader:
    def __init__(self, filename='notes.txt'):
        self.filename = filename

    def getAllNotes(self):
        try:
            with open(self.filename, 'r', encoding='utf-8') as file:
                notes = file.readlines()
                return [note.strip() for note in notes]
        except FileNotFoundError:
            return []
