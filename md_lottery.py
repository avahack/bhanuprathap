def get_input(prompt, num_values):
    return {f"{prompt}{i+1}": int(input(f"Enter the {prompt}'s value of {i+1}: ")) for i in range(num_values)}

def calculate_output(today_input, yesterday_input, multiplier):
    return {key: (today_input[key] - yesterday_input.get(key, 0)) * multiplier for key in today_input}

def print_summary(output):
    total = sum(output.values())
    print(f"Today's summary is: {total}")
    return total

def main():
    prompts = ['A', 'B', 'C', 'D', 'E', 'F', 'G', '1', '2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12', '13', '14', '15', '16', '17', '18', '19', '20', '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31', '32', '33', '34', '35', '36', '37', '38', '39', '40', '41', '42', '43', '44', '45', '46', '47', '48', '49', '50', '51', '52', '53', '54', '55']
    multipliers = [30, 20, 10, 5, 3, 2, 1, 5, 10]
    num_values = [2, 5, 18, 18, 4, 5, 3, 6, 1]

    total_sum = 0
    for prompt, multiplier, num in zip(prompts, multipliers, num_values):
        yesterday_input = get_input(f"yesterday's {prompt}", num)
        today_input = get_input(f"today's {prompt}", num)
        output = calculate_output(today_input, yesterday_input, multiplier)
        total_sum += print_summary(output)

    cash = float(input("Enter the amount of cash: "))
    summary = total_sum - cash

    if summary == 0:
        print("Today you guys did great job! Today summary is OK.")
    elif summary > 0:
        print(f"Today total is plus {summary}")
    elif summary < 0:
        print(f"Today total is minus {summary}")
    else:
        print("You did something wrong! Please try again.\n")

    print("Hope this application made your work a bit easier. Developed by BHANU!")

if __name__ == "__main__":
    main()
