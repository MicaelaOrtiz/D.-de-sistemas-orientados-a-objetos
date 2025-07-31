from models.room import Room

class RoomRepository:
    def __init__(self):
        self.rooms = []

    def add(self, room: Room):
        self.rooms.append(room)

    def get_all(self):
        return self.rooms

    def get_by_id(self, room_id: str):
        for room in self.rooms:
            if room.id == room_id:
                return room
        return None

    def get_by_name(self, name: str):
        for room in self.rooms:
            if room.name == name:
                return room
        return None