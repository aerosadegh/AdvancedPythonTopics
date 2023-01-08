# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# In representations


class AsDictionaryMixin:
    def to_dict(self, extra=[]):
        return {
            prop: self._represent(value)
            for prop, value in self.__dict__.items()
            if not self._is_internal(prop) or prop in extra
        }

    def _represent(self, value):
        if isinstance(value, object):
            if hasattr(value, "to_dict"):
                return value.to_dict()
            else:
                return str(value)
        else:
            return value

    def _is_internal(self, prop):
        return prop.startswith("_")


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# In contacts


class Address(AsDictionaryMixin):
    def __init__(self, street, city, state, zipcode, street2=""):
        self.street = street
        self.street2 = street2
        self.city = city
        self.state = state
        self.zipcode = zipcode

    def __str__(self):
        lines = [self.street]
        if self.street2:
            lines.append(self.street2)
        lines.append(f"{self.city}, {self.state} {self.zipcode}")
        return "\n".join(lines)


class AddressBook:
    def __init__(self):
        self._employee_addresses = {
            1: Address("121 Admin Rd.", "Concord", "NH", "03301"),
            2: Address("67 Paperwork Ave", "Manchester", "NH", "03101"),
            3: Address("15 Rose St", "Concord", "NH", "03301", "Apt. B-1"),
            4: Address("39 Sole St.", "Concord", "NH", "03301"),
            5: Address("99 Mountain Rd.", "Concord", "NH", "03301"),
        }

    def get_employee_address(self, employee_id):
        address = self._employee_addresses.get(employee_id)
        if not address:
            raise ValueError(employee_id)
        return address


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# In hr


class PayrollPolicy:
    def __init__(self):
        self.hours_worked = 0

    def track_work(self, hours):
        self.hours_worked += hours


class SalaryPolicy(PayrollPolicy):
    def __init__(self, weekly_salary):
        super().__init__()
        self.weekly_salary = weekly_salary

    def calculate_payroll(self):
        return self.weekly_salary


class HourlyPolicy(PayrollPolicy):
    def __init__(self, hour_rate):
        super().__init__()
        self.hour_rate = hour_rate

    def calculate_payroll(self):
        return self.hours_worked * self.hour_rate


class CommissionPolicy(SalaryPolicy):
    def __init__(self, weekly_salary, commission_per_sale):
        super().__init__(weekly_salary)
        self.commission_per_sale = commission_per_sale

    @property
    def commission(self):
        sales = self.hours_worked / 5
        return sales * self.commission_per_sale

    def calculate_payroll(self):
        fixed = super().calculate_payroll()
        return fixed + self.commission


class PayrollSystem:
    def __init__(self):
        self._employee_policies = {
            1: SalaryPolicy(3000),
            2: SalaryPolicy(1500),
            3: CommissionPolicy(1000, 100),
            4: HourlyPolicy(15),
            5: HourlyPolicy(9),
        }

    def get_policy(self, employee_id):
        policy = self._employee_policies.get(employee_id)
        if not policy:
            return ValueError(employee_id)
        return policy

    def calculate_payroll(self, employees):
        print("Calculating Payroll")
        print("===================")
        for employee in employees:
            print(f"Payroll for: {employee.id} - {employee.name}")
            print(f"- Check amount: {employee.calculate_payroll()}")
            if employee.address:
                print("- Sent to:")
                print(employee.address)
            print("")


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# In productivity


class ProductivitySystem:
    def __init__(self):
        self._roles = {
            "manager": ManagerRole,
            "secretary": SecretaryRole,
            "sales": SalesRole,
            "factory": FactoryRole,
        }

    def get_role(self, role_id):
        role_type = self._roles.get(role_id)
        if not role_type:
            raise ValueError("role_id")
        return role_type()

    def track(self, employees, hours):
        print("Tracking Employee Productivity")
        print("==============================")
        for employee in employees:
            employee.work(hours)
        print("")


class ManagerRole:
    def perform_duties(self, hours):
        return f"expends {hours} hours."


class SecretaryRole:
    def perform_duties(self, hours):
        return f"does paperwork for {hours} hours."


class SalesRole:
    def perform_duties(self, hours):
        return f"expends {hours} hours on the phone."


class FactoryRole:
    def perform_duties(self, hours):
        return f"manufactures gadgets for {hours} hours."


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# In employees


class Employee(AsDictionaryMixin):
    def __init__(self, id, name, address, role, payroll):
        self.id = id
        self.name = name
        self.address = address
        self._role = role
        self._payroll = payroll

    def work(self, hours):
        duties = self._role.perform_duties(hours)
        print(f"Employee {self.id} - {self.name}:")
        print(f"- {duties}")
        print("")
        self._payroll.track_work(hours)

    def calculate_payroll(self):
        return self._payroll.calculate_payroll()


class EmployeeDatabase:
    def __init__(self):
        self._employees = [
            {"id": 1, "name": "Mary Poppins", "role": "manager"},
            {"id": 2, "name": "John Smith", "role": "secretary"},
            {"id": 3, "name": "Kevin Bacon", "role": "sales"},
            {"id": 4, "name": "Jane Doe", "role": "factory"},
            {"id": 5, "name": "Robin Williams", "role": "secretary"},
        ]
        self.productivity = ProductivitySystem()
        self.payroll = PayrollSystem()
        self.employee_addresses = AddressBook()

    @property
    def employees(self):
        return [self._create_employee(**data) for data in self._employees]

    def _create_employee(self, id, name, role):
        address = self.employee_addresses.get_employee_address(id)
        employee_role = self.productivity.get_role(role)
        payroll_policy = self.payroll.get_policy(id)
        return Employee(id, name, address, employee_role, payroll_policy)


# %%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%
# In program
if __name__ == "__main__":

    import json

    def print_dict(d):
        print(json.dumps(d, indent=2))

    payrole_system = PayrollSystem()
    for employee in EmployeeDatabase().employees:
        print_dict(employee.to_dict())
        # print(employee.calculate_payroll())

    # Print payroll need to consider .work method!
    # print(payrole_system.calculate_payroll(EmployeeDatabase().employees))
    # Hourly payroll -> 0!

    print()
    print()
    print()
    # expends 40 Hour!
    for employee in EmployeeDatabase().employees:
        employee.work(40)
        print("payroll: ", employee.calculate_payroll())
        print_dict(employee.to_dict())
