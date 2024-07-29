from unittest import main, TestCase
from src.expenses import ExpensesGroup
from src.user import User


class ExpensesTest(TestCase):

    def setUp(self):
        test_user = User("tester")
        self.my_expense_group = ExpensesGroup(test_user)

    def test_add_expense(self):
        pass

    def test_delete_expense(self):
        pass

    def test_add_member(self):
        self.my_expense_group.add_member("Marcos")
        self.my_expense_group.add_member("marcos")
        self.my_expense_group.add_member("maRcos2")
        members_list = self.my_expense_group.get_members()
        members_list = [member.lower() for member in members_list]
        members_set = set(members_list)
        self.assertEqual(len(members_set), len(members_list), "There are duplicate members on same expense list!")

    def test_delete_member(self):
        pass


if __name__ == "__main__":
    main()
