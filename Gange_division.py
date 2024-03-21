import random
import time

def generate_random_problem(operation):
    operand1 = random.randint(1, 100) #change
    operand2 = random.randint(0, 100) #change
    operand3 = random.randint(1, 100)

    if operation == '*':
        answer = operand1 * operand2
        return f"{operand1} * {operand2}", answer
    elif operation == '/':
        answer = round(operand1 / operand3, 2)
        return f"{operand1} / {operand3}", answer

def main():
    start_time = time.time()
    correct_attempts = 0

    print("Velkommen til matematiktræningen! Skriv 'quit' for at afslutte.")

    while True:
        operation = input("Vil du løse gange (*) eller divisions (/) opgaver? ").strip()

        if operation.lower() == 'quit':
            break

        problem_and_answer = generate_random_problem(operation)
        if problem_and_answer is None:
            print(f"Ugyldigt input '{operation}'. Prøv igen.\n")
            continue

        problem, answer = problem_and_answer
        user_input = input(f"Løs: {problem} = ")
        #user_answer = round(float(user_input), 2)

        try:
            user_answer = round(float(user_input), 2)
        except ValueError:
            while ValueError:
                print(f"Prøv igen.\n")
                user_input = input(f"Løs: {problem} = ")

                if user_input.lower() == 'quit':
                    break  # exit the loop if the user wants to quit

                try:
                    user_answer = round(float(user_input), 2)
                except ValueError:
                    print("Ugyldigt input. Prøv igen.")
                    continue

                if user_answer == answer:
                    break  # exit the loop if the answer is correct

        if user_answer == answer:
            print("Korrekt!\n")
            correct_attempts += 1

        while (user_answer != answer):
            print(f"Prøv igen.\n")
            user_input = input(f"Løs: {problem} = ")

            if user_input.lower() == 'quit':
                break  # exit the loop if the user wants to quit

            try:
                user_answer = round(float(user_input), 2)
            except ValueError:
                print("Ugyldigt input. Prøv igen.")
                continue

            if user_answer == answer:
                print("Korrekt!\n")
                correct_attempts += 1
                break  # exit the loop if the answer is correct

    end_time = time.time()
    elapsed_time = end_time - start_time
    minutes, seconds = divmod(elapsed_time, 60)
    print(f"\nDu har løst {correct_attempts} korrekte spørgsmål.")
    print(f"Det tog dig {int(minutes)} minutter og {int(seconds)} sekunder.")

if __name__ == "__main__":
    main()
