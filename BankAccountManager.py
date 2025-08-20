
class User:
    """User class"""
    def __init__(self, name, surname, address, tel, email):
        self.name = name
        self.surname = surname
        self.address = address
        self.tel = tel
        self.email = email

    def print_user_info(self):
        print(f'Όνομα: {self.name}, Επώνυμο: {self.surname}, Διεύθυνση: {self.address}, Τηλέφωνο: {self.tel}, Email: {self.email}')


class Account:
    """Account class"""
    next_id = 1

    def __init__(self, user, balance):
        self.aid = Account.next_id
        Account.next_id += 1
        self.user = user
        self.balance = balance

    def print_account_info(self):
        print(f'Λογαριασμός ID: {self.aid}, Υπόλοιπο: {self.balance:.2f}€, Κάτοχος: {self.user.name} {self.user.surname}')

    def print_balance(self):
        print(f'Τρέχον Υπόλοιπο: {self.balance:.2f}€')


class AccountManager:
    """Account Manager"""
    def __init__(self):
        self.accounts = []

    def create_account(self):
        name = input("Όνομα: ")
        surname = input("Επώνυμο: ")
        address = input("Διεύθυνση: ")
        tel = input("Τηλέφωνο: ")
        email = input("Email: ")
        try:
            balance = float(input("Αρχικό Υπόλοιπο: "))
        except ValueError:
            print("Μη έγκυο ποσό.")
            return

        user = User(name, surname, address, tel, email)
        acc = Account(user, balance)
        self.accounts.append(acc)
        print("Ο λογαριασμός δημιουργήθηκε με επιτυχία.")
        acc.print_account_info()

    def deposit(self, aid, amount):
        for acc in self.accounts:
            if acc.aid == aid:
                acc.balance += amount
                print("Κατάθεση επιτυχής.")
                acc.print_balance()
                return
        print(f"Ο λογαριασμός με ID {aid} δεν βρέθηκε.")

    def withdraw(self, aid, amount):
        for acc in self.accounts:
            if acc.aid == aid:
                if acc.balance >= amount:
                    acc.balance -= amount
                    print("Ανάληψη επιτυχής.")
                else:
                    print("Ανεπαρκές υπόλοιπο.")
                acc.print_balance()
                return
        print(f"Ο λογαριασμός με ID {aid} δεν βρέθηκε.")

    def print_all_accounts(self):
        if not self.accounts:
            print("Δεν υπάρχουν λογαριασμοί.")
        for acc in self.accounts:
            acc.print_account_info()


def main():
    manager = AccountManager()

    while True:
        print("\n--- Τραπεζικό Σύστημα ---")
        print("1: Δημιουργία λογαριασμού")
        print("2: Ανάληψη")
        print("3: Κατάθεση")
        print("4: Εμφάνιση όλων των λογαριασμών")
        print("5: Έξοδος")

        choice = input("Επιλογή: ")

        if choice == "1":
            manager.create_account()
        elif choice == "2":
            try:
                aid = int(input("ID Λογαριασμού: "))
                amount = float(input("Ποσό ανάληψης: "))
                manager.withdraw(aid, amount)
            except ValueError:
                print("Μη έγκυα δεδομένα.")
        elif choice == "3":
            try:
                aid = int(input("ID Λογαριασμού: "))
                amount = float(input("Ποσό κατάθεσης: "))
                manager.deposit(aid, amount)
            except ValueError:
                print("Μη έγκυα δεδομένα.")
        elif choice == "4":
            manager.print_all_accounts()
        elif choice == "5":
            print("Έξοδος...")
            break
        else:
            print("Μη έγκυρη επιλογή.")


if __name__ == "__main__":
    main()
