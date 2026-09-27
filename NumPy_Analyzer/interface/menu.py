from utilities.create_numpy_array import create_array_menu
from utilities.mathematical_operations import mathematical_operations_menu
from utilities.combine_split import combine_split_menu
from utilities.search_sort_filter import search_sort_filter
from utilities.data_analytics import data_analytics_menu
from utilities.indexing_slicing import indexing_slicing_menu


def main_menu():

    print("Welcome to the NumPy Analyzer!")

    while True:
        
        
        print("=" * 30)
        print("Choose an option:")

        print("1. Choose a Numpy Array")
        print("2. Perform Mathematical Operations")
        print("3. Combine or Split Arrays")
        print("4. Search, Sort, or Filter Arrays")
        print("5. Compute Aggregates and Statistics")
        print("6. Exit")

        try:

            choice = int(input("Enter your choice: "))

            match choice:

                case 1:
                    array = create_array_menu()

                    if array is not None:
                        indexing_slicing_menu(array)

                case 2:
                    mathematical_operations_menu()

                case 3:
                    combine_split_menu()

                case 4:
                    search_sort_filter()

                case 5:
                    data_analytics_menu()

                case 6:
                    print("Thank you for using NumPy Analyzer! Goodbye!")
                    break
                case _:
                    print("Invalid choice. Please try again.")
                    
        except ValueError:
            print("Invalid input. Please enter a number between 1 and 6.")
