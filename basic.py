# Create a class called Cat Owner


class CatOwner:
    def __init__(self, name, address, phone):
        self.name = name
        self.address = address
        self.phone = phone


# Create a class called Cat


class Cat:
    def __init__(self, name, breed, owner):
        self.name = name
        self.breed = breed
        self.owner = owner

    def meow(self):
        print("meouw meouw")


owner1 = CatOwner("John", "123 Main St", "123-456-7890")
owner2 = CatOwner("Jane", "456 Main St", "123-456-7890")
cat1 = Cat("Tom", "Persian", owner1)
cat2 = Cat("Jerry", "Siamese", owner2)

print(cat1.owner.name)
print(cat2.owner.address)
