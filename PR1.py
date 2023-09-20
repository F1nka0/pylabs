from datetime import datetime
from typing import List
import math
class Employee:
    
    def __init__(self, name: str):
        self.name = name
    def __str__(self) -> str:
        return self.name

class Company:
    def __init__(self, name: str, address: str, *employees):
        self.name = name
        self.address = address
        self.employees = employees
        
    def prrr(self) -> str:
        print(self.name)
        print(self.address)
        print(self.employees)
        for a in self.employees:
            print(a)




company = Company("qwe","ул. строителей, дом 1", Employee("bob"),Employee("bill"))
company.prrr()




from math import sin, log, sqrt
from typing import List

def f(x: float) -> float:
    
    result: float = (1.0/3.0)*(math.sqrt(math.fabs(math.sin(x))))*math.pow(math.pow(math.e,0.12*x),(1.0/3.0))
    return result

[print(f(x/10)) for x in range(1, 7)]



results_by_for: List[float] = []
for x in range(1, 7):
    results_by_for.append(f(x/10))
    
results_by_while: List[float] = []
current_x: float = 0.10
while current_x <= 0.6:
    results_by_while.append(f(current_x))
    current_x += 0.1
    
print(results_by_while)
print(results_by_for)
print(f(0.5))