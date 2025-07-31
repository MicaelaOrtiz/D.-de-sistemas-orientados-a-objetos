import unittest
from models.room import Room
from repositories.room_repository import RoomRepository

class TestRoomRepository(unittest.TestCase):
    def setUp(self):
        self.repo = RoomRepository()

    def test_add_and_get_by_id(self):
        room = Room("Sala A", 10)
        self.repo.add(room)

        found = self.repo.get_by_id(room.id)
        self.assertIsNotNone(found)
        self.assertEqual(found.name, "Sala A")
        self.assertEqual(found.capacity, 10)

    def test_get_all(self):
        self.repo.add(Room("Sala B", 5))
        self.repo.add(Room("Sala C", 8))

        all_rooms = self.repo.get_all()
        self.assertEqual(len(all_rooms), 2)

if __name__ == '__main__':
    unittest.main()
    main()