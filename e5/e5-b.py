class Employee:
    def __init__(self, name, employee_id, department, salary):
        self.name = name
        self.employee_id = employee_id
        self.department = department
        self.salary = salary

    def display_info(self):
        print(
            f"Employee Info: {self.name}, ID: {self.employee_id}, Department: {self.department}, Salary: ${self.salary}"
        )

    def give_raise(self, amount):
        self.salary += amount
        print(
            f"{self.name} received a raise of ${amount}. New salary is ${self.salary}."
        )

    def change_department(self, new_department):
        old_department = self.department
        self.department = new_department
        print(
            f"{self.name} moved from {old_department} to {new_department} department."
        )


employee1 = Employee("Alice Johnson", 101, "Engineering", 75000)

employee1.display_info()

employee1.give_raise(5000)

employee1.change_department("Research and Development")

employee1.display_info()
