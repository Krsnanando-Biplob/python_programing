class Phone:
    catagory = "electronik"

    def __init__(self, model, price, batary, batary_persent=100):
        self.model = model
        self.price = price
        self.batary = batary
        self.batary_persent = batary_persent

    def charge(self, hour):
        self.batary_persent += hour
        print(f"charge by complite {hour} {self.model}")

    def chapture(self, photo):
        if self.batary_persent <= 0:
            print("no charge")
        else:
            self.batary_persent -= photo
            print("chaptur by photo")

    def game(self, gama):
        if self.batary_persent <= 30:
            print("you can't play game")
        else:
            self.batary_persent -= gama * 20
            print("you can play game")


apple = Phone("mod", 4455, "40ms")
print(apple.batary_persent)
# apple.charge(5)
apple.chapture(10)
print(apple.batary_persent)
apple.charge(5)
print(apple.batary_persent)
apple.game(2)
apple.game(2)
apple.game(2)
print(apple.batary_persent)
