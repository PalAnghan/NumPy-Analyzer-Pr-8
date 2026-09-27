import numpy as np


def combine_split_menu():
    while True:
        print("\nChoose an option:")
        print("1. Combine Arrays")
        print("2. Split Array")
        print("3. Go Back")

        # Error handling for menu choice
        try:
            choice = int(input("Enter your choice: "))
        except ValueError:
            print("Invalid input. Please enter a number.")
            continue

        # 1. Combine Arrays
        if choice == 1:
            try:
                print("\nCombine Arrays")

                array1 = np.array([
                    [10, 20, 30],
                    [40, 50, 60]
                ])

                elements = input(
                    "Enter 6 elements of another array to combine "
                    "(6 elements separated by space): "
                ).split()

                # Convert input into integers
                array2 = np.array(elements, dtype=int).reshape(2, 3)

               
                result = np.vstack((array1, array2))

                print("\nFirst Array:")
                print(array1)

                print("\nSecond Array:")
                print(array2)

                print("\nCombined Array:")
                print(result)

            except ValueError:
                print(
                    "Invalid input. Please enter exactly 6 integer values."
                )

        # 2. Split Array
        elif choice == 2:
            try:
                print("\nSplit Array")

                array = np.array([
                    10, 20, 30, 40, 50, 60
                ])

                print("\nOriginal Array:")
                print(array)

                parts = int(
                    input("Enter the number of parts to split the array: ")
                )

                # Check whether array can be divided equally
                if len(array) % parts != 0:
                    print(
                        "Error: Array cannot be divided equally "
                        "into this number of parts."
                    )
                else:
                    result = np.array_split(array, parts)

                    print("\nSplit Arrays:")

                    for i, part in enumerate(result, start=1):
                        print(f"Part {i}:")
                        print(part)

            except ValueError:
                print(
                    "Invalid input. Please enter a valid positive integer."
                )

            except ZeroDivisionError:
                print("Number of parts cannot be zero.")

        # 3. Go Back
        elif choice == 3:
            break

        else:
            print("Invalid choice. Please enter a number between 1 and 3.")


#combine_split_menu()