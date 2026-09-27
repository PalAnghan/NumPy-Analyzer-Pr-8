import numpy as np


def create_array_menu():

    while True:

        print("\nSelect the type of array to create:")
        print("1. 1D Array")
        print("2. 2D Array")
        print("3. 3D Array")
        print("4. Go Back")

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:

                try:
                    elements = input(
                        "Enter the elements separated by space: "
                    )

                    elements = list(map(int, elements.split()))

                    if len(elements) == 0:
                        print("Please enter at least one element.")
                        continue

                    array = np.array(elements)

                    print("\nArray created successfully:")
                    print(array)

                    return array

                except ValueError:
                    print(
                        "Invalid input. Please enter numbers only."
                    )

            elif choice == 2:

                try:
                    rows = int(input("Enter the number of rows: "))
                    columns = int(input("Enter the number of columns: "))

                    if rows <= 0 or columns <= 0:
                        print(
                            "Rows and columns must be greater than 0."
                        )
                        continue

                    total_elements = rows * columns

                    elements = input(
                        f"Enter {total_elements} elements "
                        "separated by space: "
                    )

                    elements = list(map(int, elements.split()))

                    if len(elements) != total_elements:
                        print(
                            f"Please enter exactly "
                            f"{total_elements} elements."
                        )
                        continue

                    array = np.array(elements).reshape(rows, columns)

                    print("\nArray created successfully:")
                    print(array)

                    return array

                except ValueError:
                    print(
                        "Invalid input. Please enter valid numbers."
                    )

            elif choice == 3:

                try:
                    layers = int(input("Enter the number of layers: "))
                    rows = int(input("Enter the number of rows: "))
                    columns = int(input("Enter the number of columns: "))

                    if layers <= 0 or rows <= 0 or columns <= 0:
                        print(
                            "Layers, rows, and columns "
                            "must be greater than 0."
                        )
                        continue

                    total_elements = layers * rows * columns

                    elements = input(
                        f"Enter {total_elements} elements "
                        "separated by space: "
                    )

                    elements = list(map(int, elements.split()))

                    if len(elements) != total_elements:
                        print(
                            f"Please enter exactly "
                            f"{total_elements} elements."
                        )
                        continue

                    array = np.array(elements).reshape(
                        layers,
                        rows,
                        columns
                    )

                    print("\nArray created successfully:")
                    print(array)

                    return array

                except ValueError:
                    print(
                        "Invalid input. Please enter valid numbers."
                    )
            elif choice == 4:
                return None

            else:
                print("Invalid choice. Please enter 1, 2, 3, or 4.")

        except ValueError:
            print("Invalid input. Please enter a number.")