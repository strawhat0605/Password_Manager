import hashlib
import secrets

class PasswordManager:
    def __init__(self):
        self.passwords = {}

    def add_password(self, website, username, password):
        encrypted_password = self._encrypt_password(password)
        self.passwords[website] = {'username': username, 'password': encrypted_password}
        print(f"Password for {website} added successfully!")

    def get_password(self, website):
        if website in self.passwords:
            decrypted_password = self._decrypt_password(self.passwords[website]['password'])
            print(f"Username: {self.passwords[website]['username']}, Password: {decrypted_password}")
        else:
            print(f"No password found for {website}.")

    def generate_strong_password(self):
        alphabet = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789!@#$%^&*()_+=-"
        strong_password = ''.join(secrets.choice(alphabet) for i in range(16))
        return strong_password

    def _encrypt_password(self, password):
        hashed_password = hashlib.sha256(password.encode()).hexdigest()
        return hashed_password

    def _decrypt_password(self, encrypted_password):
        return "Decryption not supported"

    def menu(self):
        while True:
            print("\nPassword Manager Menu:")
            print("1. Add Password")
            print("2. Get Password")
            print("3. Generate Strong Password")
            print("4. Exit")

            choice = input("Enter your choice: ")

            if choice == "1":
                website = input("Enter website name: ")
                username = input("Enter username: ")
                password = input("Enter password: ")
                self.add_password(website, username, password)
            elif choice == "2":
                website = input("Enter website name: ")
                self.get_password(website)
            elif choice == "3":
                strong_password = self.generate_strong_password()
                print(f"Generated Strong Password: {strong_password}")
            elif choice == "4":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    password_manager = PasswordManager()
    password_manager.menu()
