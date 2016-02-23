# from led import LED

#Valid Coins
NICKEL = "nickel"
DIME = "dime"
QUARTER = "quarter"
DOLLAR = "dollar"

#Products
APPLE = "apple"
ORANGE = "orange"
BANANA = "banana"


class VendingMachine:

    def __init__(self):
        self.valid_coins = {NICKEL: .05, DIME: 0.1, QUARTER: 0.25, DOLLAR: 1.00}
        self.coins = []
        self.products = {APPLE: 0.65, ORANGE: 0.75, BANANA: 1.0}

    def input_coin(self, coin):
        if coin in self.valid_coins:
            self.add_coins(coin)

    def add_coins(self, coin):
        self.coins.append(coin)


    def get_coins_value(self):
        value = 0
        for index in range(len(self.coins)):
            coin = self.coins[index]
            cents = self.valid_coins[coin]
            value += cents
        return value

    def can_purchase(self, selected_product):
        if self.get_coins_value() >= self.products[selected_product]:
            # LED.blink(2,1)
            return True
        return False

    def get_products(self):
        return self.products

    def purchase_product(self, product):
        if product in self.products:
            self.coins = []

            return "Purchased {}".format(product)

    def get_product_price(self, product):
        return self.products[product]
