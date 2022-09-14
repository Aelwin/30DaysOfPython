class PersonAccount:

    def __init__(self, first_name, last_name) -> None:
        self.first_name = first_name
        self.last_name = last_name
        self.incomes = []
        self.expenses = []

    def total_income(self) :
        return sum([key for income in self.incomes for key in income])
    
    def total_expense(self) :
         return sum([key for income in self.expenses for key in income])

    def account_info(self) :
        return f"{self.first_name} {self.last_name} has {self.incomes} incomes and {self.expenses} expenses"

    def add_income(self, income) :
        self.incomes.append(income)

    def add_expense(self, expense) :
        self.expenses.append(expense)

    def account_balance(self) :
        return self.total_income() - self.total_expense()

juan = PersonAccount("Juan", "López")
juan.add_income({10: "premio"})
juan.add_income({32: "sueldo"})
juan.add_expense({18: "comida"})
print(juan.account_info())
print("Total de ingresos:", juan.total_income())
print(f"Total de gastos: {juan.total_expense()}")
print(f"Diferencia = {juan.account_balance()}")