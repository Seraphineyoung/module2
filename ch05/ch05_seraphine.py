class Customer(object):
     
#     A customer of ABC Bank with a checking account.
#     Customers have the following properties:
#     Attributes:
#     name: A string representing the customer's name.
#     balance: A float tracking the current balance of the
#     customer's account.
    
  
    def __init__(self,name,balance=0.0,overdraft = 0):
        """Return a Customer object whose name is *name* and
         starting balance is *balance*."""
        self.name = name
        self.balance = balance
        self.overdraft = overdraft
        
    def overdraft_limit(self,overdraft):
        if self.balance >= 1500:
            self.balance += overdraft
            return self.balance
        else:
            print('Your have less than 1500 in your acccount and not eligible for overdraft')
            
    
    def withdraw(self,amount):
        """Return the balance remaining 
        after withdrawing *amount*dollars."""
        
        if amount > self.balance:
            raise RuntimeError('Amount greater than available balance.')
        self.balance -= amount
        return self.balance
    
    def deposit(self,amount):
        """Return the balance remaining after depositing *amount* dollars."""
        self.balance += amount
        return self.balance

customer_1 = Customer('seraphine young', 1000.0,500)
print(customer_1.name)
#add_to_balance = (customer_1.deposit(1200))
print(customer_1.balance)
print(customer_1.withdraw(100))

print(customer_1.overdraft_limit(500))




