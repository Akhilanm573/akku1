class WasteTracker:
    def __init__(self):
        self.waste_log = {}

    def add_waste(self, waste_type, amount):
        if waste_type in self.waste_log:
            self.waste_log[waste_type] += amount
        else:
            self.waste_log[waste_type] = amount
        print(f"Added {amount} units of {waste_type}.")

    def total_waste(self):
        total = sum(self.waste_log.values())
        print(f"Total waste: {total} units.")
        return total

    def display_waste_log(self):
        print("Waste Log:")
        for waste_type, amount in self.waste_log.items():
            print(f"{waste_type}: {amount} units")

def main():
    tracker = WasteTracker()
    
    while True:
        print("\n1. Add waste")
        print("2. View total waste")
        print("3. Display waste log")
        print("4. Exit")
        
        choice = input("Choose an option: ")
        
        if choice == '1':
            waste_type = input("Enter waste type: ")
            amount = float(input("Enter amount (in units): "))
            tracker.add_waste(waste_type, amount)
        elif choice == '2':
            tracker.total_waste()
        elif choice == '3':
            tracker.display_waste_log()
        elif choice == '4':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
