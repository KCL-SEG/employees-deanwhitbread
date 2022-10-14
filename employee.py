"""Employee pay calculator."""

class Employee:
    def __init__(self, name, contract, commission=None):
        self.name = name
        self.contract = contract
        if (commission == None):
            self.commission = NoCommission()
        else:
            self.commission = commission

    def get_pay(self):
        return self.contract.get_pay() + self.commission.get_commission()

    def get_commission(self):
        return self.commission.get_commission()

    def __str__(self):
        return f'{self.name} works on a {self.contract.__str__()}{self.commission.__str__()} Their total pay is {self.get_pay()}.'

'''Contract Class'''
class Contract:
    def __init__(self, wage, monthly_hours=1):
        self.wage = wage
        self.monthly_hours = monthly_hours

    def get_pay(self):
        return self.wage

    def get_monthly_hours(self):
        return self.monthly_hours

class MonthlyContract(Contract):
    def __init__(self, wage):
        super().__init__(wage)

    def __str__(self):
        return f'monthly salary of {super().get_pay()}'

class HourlyContract(Contract):
    def __init__(self, wage, monthly_hours):
        super().__init__(wage, monthly_hours)

    def get_pay(self):
        return self.get_wage() * super().get_monthly_hours()

    def get_wage(self):
        return super().get_pay()

    def get_hours(self):
        return super().get_monthly_hours()

    def __str__(self):
        return f'contract of {self.get_hours()} hours at {self.get_wage()}/hour'

''' Commission class '''

class Commission:
    def __init__(self, commission_rate=0):
        self.commission_rate = commission_rate

    def get_commission(self):
        return self.commission_rate

class NoCommission(Commission):
    def __init__(self):
        super().__init__()

    def __str__(self):
        return f'.'

class BonusCommission(Commission):
    def __init__(self, commission_rate):
        super().__init__(commission_rate)

    def __str__(self):
        return f' and receives a bonus commission of {super().get_commission()}.'

class ContractCommission(Commission):
    def __init__(self, commission_rate, commission_num):
        super().__init__(commission_rate)
        self.commission_num = commission_num

    def get_commission(self):
        return super().get_commission() * self.commission_num

    def get_rate(self):
        return super().get_commission()

    def __str__(self):
        return f' and receives a commission for {self.commission_num} contract(s) at {self.get_rate()}/contract.'


# Billie works on a monthly salary of 4000.  Their total pay is 4000.
billie = Employee('Billie', MonthlyContract(4000))

# Charlie works on a contract of 100 hours at 25/hour.  Their total pay is 2500.
charlie = Employee('Charlie', HourlyContract(25,100))

# Renee works on a monthly salary of 3000 and receives a commission for 4 contract(s) at 200/contract.  Their total pay is 3800.
renee = Employee('Renee', MonthlyContract(3000), ContractCommission(200,4))

# Jan works on a contract of 150 hours at 25/hour and receives a commission for 3 contract(s) at 220/contract.  Their total pay is 4410.
jan = Employee('Jan', HourlyContract(25, 150), ContractCommission(220, 3))

# Robbie works on a monthly salary of 2000 and receives a bonus commission of 1500.  Their total pay is 3500.
robbie = Employee('Robbie', MonthlyContract(2000), BonusCommission(1500))

# Ariel works on a contract of 120 hours at 30/hour and receives a bonus commission of 600.  Their total pay is 4200.
ariel = Employee('Ariel', HourlyContract(30, 120), BonusCommission(600))
