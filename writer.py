class Writer:
    def __init__(self, filename='notes.txt'):
        self.filename = filename

    def addNote(self, note: str):
        with open(self.filename, 'a', encoding='utf-8') as file:
            file.write(note + '\n')
