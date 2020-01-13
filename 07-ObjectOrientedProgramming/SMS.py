import message

class SMS(message.Message):
    def __init__(self, nadawca, odbiorca):
        super().__init__()
        self.nadawca = nadawca
        self.odbiorca = odbiorca
    def send(self):
        print("Wysyłanie SMS...")
        print(f"Od: {self.nadawca}")
        print(f"Do: {self.odbiorca}")
        print(f"Treść: {self.message}")