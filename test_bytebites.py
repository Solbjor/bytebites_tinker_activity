"""
Pytest test suite for ByteBites application
Run with: pytest test_bytebites.py -v
"""

import pytest
from models import Customer, FoodItem, Menu, Transaction


# ==========================
# Fixtures (Test Data Setup)
# ==========================

@pytest.fixture
def sample_food_items():
    """Create a set of sample food items for testing"""
    return {
        'burger': FoodItem("Spicy Burger", 12.99, "Burgers", 7),
        'soda': FoodItem("Soda", 5.99, "Drinks", 8),
        'fries': FoodItem("French Fries", 3.99, "Sides", 9),
        'ice_cream': FoodItem("Ice Cream", 4.50, "Desserts", 10),
        'cheese_burger': FoodItem("Cheese Burger", 15.99, "Burgers", 8),
        'cola': FoodItem("Cola", 2.99, "Drinks", 7),
        'cake': FoodItem("Chocolate Cake", 6.99, "Desserts", 6)
    }


@pytest.fixture
def populated_menu(sample_food_items):
    """Create a menu populated with sample items"""
    menu = Menu()
    for item in sample_food_items.values():
        menu.addItem(item)
    return menu


@pytest.fixture
def customer():
    """Create a test customer"""
    return Customer("Alice")


@pytest.fixture
def customer_with_transaction(customer, sample_food_items):
    """Create a customer with a transaction"""
    transaction = Transaction(customer)
    transaction.addItem(sample_food_items['burger'])
    transaction.addItem(sample_food_items['soda'])
    return customer, transaction


# ==========================
# Customer Tests
# ==========================

class TestCustomer:
    
    def test_customer_creation(self):
        """Test that a customer can be created with a name"""
        customer = Customer("Alice")
        assert customer.getName() == "Alice"
        assert len(customer.getPurchaseHistory()) == 0
    
    def test_customer_verify_user_no_purchases(self, customer):
        """Test that a new customer without purchases is not verified"""
        assert customer.verifyUser() == False
    
    def test_customer_verify_user_with_purchases(self, customer_with_transaction):
        """Test that a customer with purchases is verified"""
        customer, _ = customer_with_transaction
        assert customer.verifyUser() == True
    
    def test_customer_purchase_history(self, customer_with_transaction):
        """Test that purchase history is tracked correctly"""
        customer, transaction = customer_with_transaction
        assert len(customer.getPurchaseHistory()) == 1
        assert customer.getPurchaseHistory()[0] == transaction


# ==========================
# FoodItem Tests
# ==========================

class TestFoodItem:
    
    def test_food_item_creation(self):
        """Test that a food item can be created with valid data"""
        item = FoodItem("Burger", 10.99, "Burgers", 8)
        assert item.getName() == "Burger"
        assert item.getPrice() == 10.99
        assert item.getCategory() == "Burgers"
        assert item.getPopularityRating() == 8
    
    def test_food_item_invalid_price(self):
        """Test that negative price raises ValueError"""
        with pytest.raises(ValueError, match="Price must be positive"):
            FoodItem("Burger", -5.0, "Burgers", 8)
    
    def test_food_item_zero_price(self):
        """Test that zero price raises ValueError"""
        with pytest.raises(ValueError, match="Price must be positive"):
            FoodItem("Burger", 0, "Burgers", 8)
    
    def test_food_item_empty_category(self):
        """Test that empty category raises ValueError"""
        with pytest.raises(ValueError, match="Category cannot be empty"):
            FoodItem("Burger", 10.99, "", 8)


# ==========================
# Menu Tests
# ==========================

class TestMenu:
    
    def test_menu_creation(self):
        """Test that a menu can be created empty"""
        menu = Menu()
        assert len(menu.getAllItems()) == 0
    
    def test_menu_add_item(self, sample_food_items):
        """Test adding items to menu"""
        menu = Menu()
        menu.addItem(sample_food_items['burger'])
        assert len(menu.getAllItems()) == 1
        assert menu.getAllItems()[0] == sample_food_items['burger']
    
    def test_menu_remove_item(self, populated_menu, sample_food_items):
        """Test removing an item from menu"""
        initial_count = len(populated_menu.getAllItems())
        populated_menu.removeItem(sample_food_items['cola'])
        assert len(populated_menu.getAllItems()) == initial_count - 1
        assert sample_food_items['cola'] not in populated_menu.getAllItems()
    
    def test_menu_remove_nonexistent_item(self, populated_menu):
        """Test that removing nonexistent item raises ValueError"""
        fake_item = FoodItem("Fake Item", 1.0, "Test", 1)
        with pytest.raises(ValueError, match="Item not found in menu"):
            populated_menu.removeItem(fake_item)
    
    def test_menu_filter_by_category(self, populated_menu):
        """Test filtering menu by category"""
        burgers = populated_menu.filterByCategory("Burgers")
        assert len(burgers) == 2
        for item in burgers:
            assert item.getCategory() == "Burgers"
        
        desserts = populated_menu.filterByCategory("Desserts")
        assert len(desserts) == 2
        for item in desserts:
            assert item.getCategory() == "Desserts"
    
    def test_menu_sort_by_price_ascending(self, populated_menu):
        """Test sorting menu by price (low to high)"""
        sorted_items = populated_menu.sortByPrice(ascending=True)
        prices = [item.getPrice() for item in sorted_items]
        assert prices == sorted(prices)
        assert sorted_items[0].getPrice() == 2.99  # Cola is cheapest
    
    def test_menu_sort_by_price_descending(self, populated_menu):
        """Test sorting menu by price (high to low)"""
        sorted_items = populated_menu.sortByPrice(ascending=False)
        prices = [item.getPrice() for item in sorted_items]
        assert prices == sorted(prices, reverse=True)
        assert sorted_items[0].getPrice() == 15.99  # Cheese Burger is most expensive
    
    def test_menu_sort_by_popularity(self, populated_menu):
        """Test sorting menu by popularity (high to low by default)"""
        sorted_items = populated_menu.sortByPopularity(ascending=False)
        ratings = [item.getPopularityRating() for item in sorted_items]
        assert ratings == sorted(ratings, reverse=True)
        assert sorted_items[0].getPopularityRating() == 10  # Ice Cream is most popular
    
    def test_menu_sort_by_name(self, populated_menu):
        """Test sorting menu alphabetically by name"""
        sorted_items = populated_menu.sortByName()
        names = [item.getName() for item in sorted_items]
        assert names == sorted(names)


# ==========================
# Transaction Tests
# ==========================

class TestTransaction:
    
    def test_transaction_creation(self, customer):
        """Test that a transaction can be created"""
        transaction = Transaction(customer)
        assert len(transaction.getItems()) == 0
        assert transaction.customer == customer
    
    def test_transaction_auto_adds_to_customer(self, customer):
        """Test that creating a transaction automatically adds it to customer history"""
        transaction = Transaction(customer)
        assert len(customer.getPurchaseHistory()) == 1
        assert customer.getPurchaseHistory()[0] == transaction
    
    def test_transaction_add_item(self, customer, sample_food_items):
        """Test adding items to a transaction"""
        transaction = Transaction(customer)
        transaction.addItem(sample_food_items['burger'])
        transaction.addItem(sample_food_items['soda'])
        assert len(transaction.getItems()) == 2
    
    def test_transaction_remove_item(self, customer_with_transaction, sample_food_items):
        """Test removing an item from transaction"""
        _, transaction = customer_with_transaction
        initial_count = len(transaction.getItems())
        transaction.removeItem(sample_food_items['burger'])
        assert len(transaction.getItems()) == initial_count - 1
    
    def test_transaction_remove_nonexistent_item(self, customer):
        """Test that removing nonexistent item raises ValueError"""
        transaction = Transaction(customer)
        fake_item = FoodItem("Fake", 1.0, "Test", 1)
        with pytest.raises(ValueError, match="Item not found in transaction"):
            transaction.removeItem(fake_item)
    
    def test_transaction_calculate_total(self, customer, sample_food_items):
        """Test calculating total cost of transaction"""
        transaction = Transaction(customer)
        transaction.addItem(sample_food_items['burger'])   # 12.99
        transaction.addItem(sample_food_items['soda'])     # 5.99
        transaction.addItem(sample_food_items['fries'])    # 3.99
        expected_total = 12.99 + 5.99 + 3.99
        assert transaction.calculateTotal() == pytest.approx(expected_total, rel=1e-2)
    
    def test_transaction_sort_by_price(self, customer, sample_food_items):
        """Test sorting transaction items by price"""
        transaction = Transaction(customer)
        transaction.addItem(sample_food_items['burger'])
        transaction.addItem(sample_food_items['fries'])
        transaction.addItem(sample_food_items['soda'])
        
        sorted_items = transaction.sortItemsByPrice(ascending=True)
        prices = [item.getPrice() for item in sorted_items]
        assert prices == sorted(prices)
    
    def test_transaction_sort_by_popularity(self, customer, sample_food_items):
        """Test sorting transaction items by popularity"""
        transaction = Transaction(customer)
        transaction.addItem(sample_food_items['burger'])
        transaction.addItem(sample_food_items['ice_cream'])
        transaction.addItem(sample_food_items['fries'])
        
        sorted_items = transaction.sortItemsByPopularity(ascending=False)
        ratings = [item.getPopularityRating() for item in sorted_items]
        assert ratings == sorted(ratings, reverse=True)


# ==========================
# Integration Tests
# ==========================

class TestIntegration:
    
    def test_complete_order_flow(self, populated_menu):
        """Test a complete order flow from menu browsing to purchase"""
        # Customer browses menu
        customer = Customer("Bob")
        assert customer.verifyUser() == False  # New customer
        
        # Customer filters by category
        burgers = populated_menu.filterByCategory("Burgers")
        assert len(burgers) > 0
        
        # Customer creates transaction
        transaction = Transaction(customer)
        
        # Customer adds items
        for burger in burgers[:1]:  # Add first burger
            transaction.addItem(burger)
        
        # Calculate total
        total = transaction.calculateTotal()
        assert total > 0
        
        # Customer is now verified
        assert customer.verifyUser() == True
        assert len(customer.getPurchaseHistory()) == 1
    
    def test_multiple_transactions_per_customer(self, sample_food_items):
        """Test that a customer can have multiple transactions"""
        customer = Customer("Charlie")
        
        # First transaction
        trans1 = Transaction(customer)
        trans1.addItem(sample_food_items['burger'])
        
        # Second transaction
        trans2 = Transaction(customer)
        trans2.addItem(sample_food_items['soda'])
        trans2.addItem(sample_food_items['fries'])
        
        assert len(customer.getPurchaseHistory()) == 2
        assert trans1 in customer.getPurchaseHistory()
        assert trans2 in customer.getPurchaseHistory()


if __name__ == "__main__":
    # Allow running with: python test_bytebites.py
    pytest.main([__file__, "-v"])