import unittest
from models.user import User
from repositories.user_repository import UserRepository

class TestUserRepository(unittest.TestCase):
    def setUp(self):
        self.repo = UserRepository()

    def test_add_and_get_by_id(self):
        user = User("Juan")
        self.repo.add(user)

        found = self.repo.get_by_id(user.id)
        self.assertIsNotNone(found)
        self.assertEqual(found.name, "Juan")

    def test_get_by_name(self):
        user = User("Juan")
        self.repo.add(user)

        found = self.repo.get_by_name("Juan")
        self.assertIsNotNone(found)
        self.assertEqual(found.id, user.id)

if __name__ == '__main__':
    unittest.main()
    main()