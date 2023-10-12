import random

def main():
    
    slotmachine = SlotMachine()
    slotmachine.use_slot_machine()
    

    
class SlotMachine:
    def __init__(self, balance=0, bet=0) -> None:
        # User values
        self._balance = balance # The user balance
        self._bet = bet # The users current bet
        
        # Bet values
        self._max_lines = 3
        self._max_bet = 100
        self._min_bet = 1

        # Slotmachine values
        self._rows = 3
        self._cols = 3
        self._symbol_count  = {
            "A": 2,
            "B": 4,
            "C": 6,
            "D": 8,
        }
        
        self._symbol_values = {
            "A": 5,
            "B": 4,
            "C": 3,
            "D": 2,
        }

                
    def __str__(self) -> str:
        """What is this?"""
        return "It's a goddamn slotmachine."
    
    def use_slot_machine(self):
        self.user_deposit()
        while True:
            print(f"\nCurrent balance is: ${self._balance}")    
            spin = input("Press enter to spin (q to quit)")
            if spin == "q":
                break
            else:
                
                lines = self.get_number_of_lines()
                while True:
                    bet = self.get_bet()
                    total_bet = bet * lines

                    if total_bet > self._balance:
                        print(f"You do not have enough funds to bet that amount. Your current balance is {self._balance}.")
                    else:
                        self._balance = self._balance - total_bet
                        print(self._balance)
                        break
                    
                print(f"You are betting {bet} on {lines} lines. Your total bet is equal to ${total_bet}")
                
                columns = self.get_slot_machine_spin()
                
                # Print the slot 
                self.print_slot_machine(columns)
                
                # Call the winnings function
                winnings, winning_lines = self.check_winnings(columns, lines)
                print(f"You won ${winnings}.")
                if len(winning_lines) > 0:
                    print(f"You won on lines:", *winning_lines,)
                    
                self._balance = self._balance + winnings
            
        
        print(f"\nYou left with ${self._balance}")
    
    def get_number_of_lines(self):
        """Prompt the user for the amount of lines they would like to play"""
        while True:
            lines = input(f"Enter the number of lines to bet on (1-{str(self._max_lines)})")
            if lines.isdigit():
                lines = int(lines)
                if 1 <= lines <= self._max_lines:
                    break
                else:
                    print("Amount of lines must be between 1 and 3\n")
            else:
                print("Please enter a valid number of lines\n")
        return lines
    
    def get_bet(self):
        while True:
            amount = input("What would you like to bet on each line? $ ")
            if amount.isdigit():
                amount = int(amount)
                if self._min_bet <= amount <= self._max_bet:
                    self._bet = amount
                    return self._bet
                else:
                    print(f"Amount must be between {self._min_bet} and {self._max_bet}")
            else:
                print("Please enter a number.")

    def user_deposit(self) -> None:
        while True:
            amount = input("What would you like to deposit? $ ")
            if amount.isdigit():
                amount = int(amount)
                if amount > 0:
                    self.deposit(amount)  # Call the deposit method here
                    break
                else:
                    print("Amount must be greater than 0")
            else:
                print("Please enter a number.")
                
    def deposit(self, amount: int) -> int:
        if amount > 0:
            self._balance += amount
            return amount
        else:
            raise ValueError("Amount must be greater than 0")

    def get_slot_machine_spin(self):
        all_symbols = []
        for symbol, symbol_count in self._symbol_count.items():
            for _ in range(symbol_count):
                all_symbols.append(symbol)
        
        columns = []
        for _ in range(self._cols):
            column = []
            current_symbols = all_symbols[:]
            for _ in range(self._rows):
                value = random.choice(current_symbols)
                current_symbols.remove(value)
                column.append(value)
                
            columns.append(column)
        
        return columns
    
    def print_slot_machine(self, columns):
        for row in range(len(columns[0])):
            for i, column in enumerate(columns):
                if i != len(columns) - 1:
                    print(column[row], end=" ❘ ")    
                else:
                    print(column[row])
        
    def check_winnings(self, columns, lines):
        winnings = 0
        winning_lines = []
        for line in range(lines):
            symbol = columns[0][line]
            for column in columns:
                symbol_to_check = column[line]
                if symbol != symbol_to_check:
                    break
            else:
                winnings += self._symbol_values[symbol] * self._bet
                winning_lines.append(line + 1)
                
        return winnings, winning_lines
                
                
            


if __name__ == "__main__":
    main()
    