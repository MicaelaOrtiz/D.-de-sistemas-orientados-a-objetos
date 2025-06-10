from writer import Writer
from reader import Reader

writer = Writer()
reader = Reader()

writer.addNote("Estudiar para el parcial")
notas = reader.getAllNotes()

print("Notas guardadas:")
for nota in notas:
    print("-", nota)
