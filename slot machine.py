import random


MAX_LINES = 3
MAX_BET = 1000
MIN_BET = 1

ROWS = 3
COLS = 3

symbol_count = {
    "7": 2,
    "★": 4,
    "♥": 6,
    "☮": 8
}

symbol_value = {
    "7": 5,
    "★": 4,
    "♥": 3,
    "☮": 2
}


def check_win(columns, lines, bet, values):
    win = 0
    winning_lines = []
    for line in range(lines):
        symbol = columns[0][line]
        for col in columns:
            symbol_to_check = col[line]
            if symbol != symbol_to_check:
                break
        else:
            win += values[symbol] * bet
            winning_lines.append(line + 1)

    return win, winning_lines


def get_slot_machine_spin(rows, cols, symbols):
    all_symbols = []
    for symbol, symbol_count in symbols.items():
        for _ in range (symbol_count):
            all_symbols.append(symbol)

    columns = []
    for _ in range(cols):
        column = []
        current_symbols = all_symbols[:]
        for _ in range(rows):
            value = random.choice(current_symbols)
            current_symbols.remove(value)
            column.append(value)
        columns.append(column)
    return columns


def show_slot_machine(columns):
    for row in range(len(columns[0])):
        for i, col in enumerate(columns):
            if i != len(columns) - 1:
                print(col[row], end=" | ")
            else:
                print(col[row], end="")
        print()


def deposit():
    while True:
        amount = input("How much would you like to deposit? $")
        if amount.isdigit():
            amount = int(amount)
            if amount > 0:
                break
            else:
                print("Amount must be greater than 0.")
        else:
            print("Enter a number please.")
    return amount


def get_number_of_lines():
    while True:
        lines = input(f"Enter number of lines to bet on from 1 - {MAX_LINES}? ")
        if lines.isdigit():
            lines = int(lines)
            if 1 <= lines <= MAX_LINES:
                break
            else:
                print(f"Enter a number of lines between 1 and {MAX_LINES} please.")
        else:
            print("Enter a number please.")
    return lines


def get_bet():
    while True:
        bet = input("How much would you like to bet on each line? $")
        if bet.isdigit():
            bet = int(bet)
            if MIN_BET <= bet <= MAX_BET:
                break
            else:
                print(f"Amount must be between ${MIN_BET} and ${MAX_BET} .")
        else:
            print("Enter a number please.")
    return bet


def game_start(balance):
    lines = get_number_of_lines()
    while True:
        bet = get_bet()
        total_bet = bet * lines
        if total_bet > balance:
            print(f"You don't have enough money on your balance. Your balance is ${balance}")
        else:
            break
    print(f"You are betting ${bet} on {lines} lines. Total bet is: ${total_bet}")

    slots = get_slot_machine_spin(ROWS, COLS, symbol_count)
    show_slot_machine(slots)
    win, winning_lines = check_win(slots, lines, bet, symbol_value)
    if win != 0:
        print(f"Congratulations! You won ${win}.")
        print(f"You won on lines: ", *winning_lines)
    else:
        print("You lost.")
    return win - total_bet


def main():
    balance = deposit()
    while True:
        print(f"Your current balance: ${balance}")
        begin = input("Press enter to start the game or q to quit.")
        if begin == "q":
            break
        balance += game_start(balance)
    print(f"You left with ${balance}")

main()