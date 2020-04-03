class ShoppingList:
    def __init__(self, **items):
        self.items = items

    def __len__(self):
        total_items = 0
        for _ in self.items:
            total_items += 1

        return total_items

    # Return string
    def __str__(self):
        return 'List contains items: ' + ', '.join(self.items.keys())


wills_items = ShoppingList(Apple=4, Pear=23, Pie=4)
breakpoint()
print(len(wills_items))
breakpoint()
print(str(wills_items))
