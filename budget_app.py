class Category:
    def __init__(self, name):
        self.name = name
        self.ledger = []

    def __str__(self):
        title = f'{self.name:*^30}\n'
        items = ''
        for item in self.ledger:
            description = f"{item['description'][:23].ljust(23)}"
            amount = f"{item['amount']:>7.2f}"
            items += f'{description}{amount}\n'
        total = f'Total: {self.get_balance()}'
        return title + items + total

    def deposit(self, amount, description = ''):
        self.ledger.append({'amount': amount, 'description': description})

    def withdraw(self, amount, description = ''):
        if self.check_funds(amount):
            self.ledger.append({'amount': -amount, 'description': description})
            return True
        return False

    def get_balance(self):
        return sum(item['amount'] for item in self.ledger)

    def transfer(self, amount, category):
        if self.check_funds(amount):
            self.withdraw(amount, f'Transfer to {category.name}')
            category.deposit(amount, f'Transfer from {self.name}')
            return True
        return False

    def check_funds(self, amount):
        if amount > self.get_balance():
            return False
        else:
            return True

def create_spend_chart(categories):
    withdrawls = []
    for category in categories:
        total = sum(abs(item['amount']) for item in category.ledger if item['amount'] < 0)
        withdrawls.append(total)

    total_withdrawls = sum(withdrawls)
    percentage = [(w / total_withdrawls) * 100 if total_withdrawls != 0 else 0 for w in withdrawls]
    percentage = [(p // 10 * 10) for p in percentage]

    chart = 'Percentage spent by category\n'
    for i in range(100, -10, -10):
        chart += f'{i:3}| '
        for p in percentage:
            chart += 'o  ' if p >= i else '   '
        chart += '\n'
    
    chart += '    ' + '-' * (len(categories) * 3 + 1) + '\n'

    max_lenght = max(len(category.name) for category in categories)
    for i in range(max_lenght):
        chart += '     '
        for category in categories:
            if i < len(category.name):
                chart += category.name[i] + '  '
            else:
                chart += '   '
        if i < max_lenght - 1:
            chart += '\n'

    return chart

food = Category('Food')
food.deposit(1000, 'deposit')
food.withdraw(10.15, 'groceries')
food.withdraw(15.89, 'restaurant and more food for dessert')
clothing = Category('Clothing')
food.transfer(50, clothing)
print(food)

print(create_spend_chart([food, clothing]))