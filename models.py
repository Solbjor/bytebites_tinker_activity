# These are the classes for the ByteBites
# program, the main 4 Candidate Classes comprise the core of the program, while the others are for future expansion.
# They are Customer, FoodItem, Menu, and Transaction. Customer represents the customers of ByteBites, 
# FoodItem represents the different food items available, Menu represents the menu of ByteBites, and 
# Transaction represents the transactions made by customers. The other classes such as Drinks, Desserts, 
# and Sides are for future expansion and are currently ignored in the implementation.


class Customer:
    """
    Represents a customer of ByteBites.
    Tracks customer name and purchase history for user verification.
    """
    
    def __init__(self, name):
        """
        Initialize a new Customer.
        
        Args:
            name (str): The customer's name
        """
        self.name = name
        self.purchaseHistory = []
    
    def getName(self):
        """
        Get the customer's name.
        
        Returns:
            str: The customer's name
        """
        return self.name
    
    def getPurchaseHistory(self):
        """
        Get the customer's purchase history.
        
        Returns:
            list: List of Transaction objects
        """
        return self.purchaseHistory
    
    def addPurchase(self, transaction):
        """
        Add a transaction to the customer's purchase history.
        
        Args:
            transaction (Transaction): The transaction to add
        """
        self.purchaseHistory.append(transaction)
    
    def verifyUser(self):
        """
        Verify if the customer is a real user based on purchase history.
        
        Returns:
            bool: True if customer has purchase history, False otherwise
        """
        return len(self.purchaseHistory) > 0

class FoodItem:
    """
    Represents a specific food item available for purchase.
    Tracks name, price, category, and popularity rating.
    """
    
    def __init__(self, name, price, category, popularityRating):
        """
        Initialize a new FoodItem.
        
        Args:
            name (str): The item name (e.g., "Spicy Burger")
            price (float): The item price (must be positive)
            category (str): The category (e.g., "Burgers", "Drinks")
            popularityRating (int): The popularity rating
            
        Raises:
            ValueError: If price is not positive or category is empty
        """
        if price <= 0:
            raise ValueError("Price must be positive")
        if not category or category.strip() == "":
            raise ValueError("Category cannot be empty")
        
        self.name = name
        self.price = price
        self.category = category
        self.popularityRating = popularityRating
    
    def getName(self):
        """
        Get the item name.
        
        Returns:
            str: The item name
        """
        return self.name
    
    def getPrice(self):
        """
        Get the item price.
        
        Returns:
            float: The item price
        """
        return self.price
    
    def getCategory(self):
        """
        Get the item category.
        
        Returns:
            str: The category name
        """
        return self.category
    
    def getPopularityRating(self):
        """
        Get the item's popularity rating.
        
        Returns:
            int: The popularity rating
        """
        return self.popularityRating


class Menu:
    """
    Manages the full collection of food items available at ByteBites.
    Provides functionality to add, remove, and filter items by category.
    """
    
    def __init__(self):
        self.items = []
    
    def addItem(self, foodItem):
        self.items.append(foodItem)
    
    def removeItem(self, foodItem):
        if foodItem in self.items:
            self.items.remove(foodItem)
        else:
            raise ValueError("Item not found in menu")
    
    def getAllItems(self):
        return self.items
    
    def filterByCategory(self, category):
        return [item for item in self.items if item.getCategory() == category]
    
    def sortByPrice(self, ascending=True):
        """
        Sort menu items by price.
        
        Args:
            ascending (bool): If True, sort low to high; if False, sort high to low
            
        Returns:
            list: Sorted list of FoodItem objects
        """
        return sorted(self.items, key=lambda item: item.getPrice(), reverse=not ascending)

    def sortByPopularity(self, ascending=False):
        """
        Sort menu items by popularity rating.
        
        Args:
            ascending (bool): If True, sort low to high; if False (default), sort high to low
            
        Returns:
            list: Sorted list of FoodItem objects
        """
        return sorted(self.items, key=lambda item: item.getPopularityRating(), reverse=not ascending)

    def sortByName(self):
        """
        Sort menu items alphabetically by name.
        
        Returns:
            list: Alphabetically sorted list of FoodItem objects
        """
        return sorted(self.items, key=lambda item: item.getName())



class Transaction:
    """
    Represents a single transaction/order made by a customer.
    Groups selected items and computes the total cost.
    """
    
    def __init__(self, customer):
        """
        Initialize a new Transaction for a customer.
        Automatically adds this transaction to the customer's purchase history.
        
        Args:
            customer (Customer): The customer making this transaction
        """
        self.customer = customer
        self.selectedItems = []
        # Maintain bidirectional relationship
        customer.addPurchase(self)
    
    def addItem(self, foodItem):
        """
        Add a food item to this transaction.
        
        Args:
            foodItem (FoodItem): The food item to add
        """
        self.selectedItems.append(foodItem)
    
    def removeItem(self, foodItem):
        """
        Remove a food item from this transaction.
        
        Args:
            foodItem (FoodItem): The food item to remove
            
        Raises:
            ValueError: If the item is not in the transaction
        """
        if foodItem in self.selectedItems:
            self.selectedItems.remove(foodItem)
        else:
            raise ValueError("Item not found in transaction")
    
    def getItems(self):
        """
        Get all items in this transaction.
        
        Returns:
            list: List of FoodItem objects in this transaction
        """
        return self.selectedItems
    
    def calculateTotal(self):
        """
        Calculate the total cost of all items in this transaction.
        
        Returns:
            float: The total cost (sum of all item prices)
        """
        total = 0.0
        for item in self.selectedItems:
            total += item.getPrice()
        return total
    
    def sortItemsByPrice(self, ascending=True):
        """
        Sort items in this transaction by price.
        
        Args:
            ascending (bool): If True, sort low to high; if False, sort high to low
            
        Returns:
            list: Sorted list of FoodItem objects
        """
        return sorted(self.selectedItems, key=lambda item: item.getPrice(), reverse=not ascending)

    def sortItemsByPopularity(self, ascending=False):
        """
        Sort items in this transaction by popularity rating.
        
        Args:
            ascending (bool): If True, sort low to high; if False, sort high to low
            
        Returns:
            list: Sorted list of FoodItem objects
        """
        return sorted(self.selectedItems, key=lambda item: item.getPopularityRating(), reverse=not ascending)
    
testCustomer = Customer("Alice")
purchase = Transaction(testCustomer)
burger = FoodItem("Spicy Burger", 12.99, "Burgers", 7)
soda = FoodItem("Soda", 5.99, "Drinks", 8)
menu = Menu()
menu.addItem(burger)
menu.addItem(soda)
purchase.addItem(burger)
purchase.addItem(soda)

print(f"Customer: {testCustomer.getName()}")
print(f"Items bought: {len(purchase.getItems())}")
print(f"Total Cost: ${purchase.calculateTotal()}")
print(f"Menu:")
for item in menu.getAllItems():
    print(item.getName())
print(f"Customer verified: {testCustomer.verifyUser()}")

