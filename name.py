def copy_times(name, number):
    if number <= 0:
        print("You entered a non-positive number.")
        answer = input("Do you want to try again? [Y/n]")
        if answer.lower() == "y":
            return True
        else:
            return False
    else:
        for i in range(number):
            print(f"{i}:Hello dear {name}. the square of {i} is {square(i)}")

def square(x):
    return x * x

def main():
    name = input("Enter your name: ")
    while True:
        try:
            number = int(input("How many times do you want to print? "))
            if not copy_times(name, number):
                break
        except ValueError:
            print("Please enter a valid integer.")

if __name__ == "__main__":
    main()
