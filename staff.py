class Staff:
    def __init__(self, name, department, wage):
        if not name:
            raise ValueError("Missing name")
        if department not in ["Finance", "Sales", "Management", "IT"]:
            raise ValueError("Invalid department")
        
        self.name = name
        self.department = department
        self.wage = wage
    
    def __str__(self):
        return f"{self.name} from {self.department}, wage {self.wage}"
    
def main():
    staff = get_staff()
    print(staff)

def get_staff():
    name = input("Name: ")
    department = input("Department: ")
    wage = float(input("Wage: "))

    return Staff(name, department, wage)

    
#if __name__ == "__main__":
main()