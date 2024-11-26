import os

def create_file():
    """
    Create a new text file.

    This function prompts the user to enter a filename, and then creates a new
    text file with the specified name in the current working directory.
    """
    filename = input("Enter a filename: ")
    with open(filename, "w") as file:
        print(f"Created a new file: {filename}")

def open_file():
    """
    Open an existing text file.

    This function prompts the user to enter a filename, and then opens the
    specified text file in the current working directory. The content of the
    file is then displayed.
    """
    filename = input("Enter a filename: ")
    if os.path.isfile(filename):
        with open(filename, "r") as file:
            content = file.read()
            print(f"Opening file: {filename}")
            print(content)
    else:
        print(f"File not found: {filename}")
def edit_file():
    """
    Edit the content of a text file.

    This function prompts the user to enter a filename, and then opens the
    specified text file in the current working directory. The user can then
    modify the content of the file, and the changes are saved.
    """
    filename = input("Enter a filename: ")
    if os.path.isfile(filename):
        with open(filename, "r") as file:
            content = file.read()
        new_content = input("Enter the new content: ")
        with open(filename, "w") as file:
            file.write(new_content)
        print(f"Saved changes to file: {filename}")
    else:
        print(f"File not found: {filename}")
def main():
    """
    Main function of the BASICS text editor application.

    This function displays a menu of options for the user to choose from, and
    then calls the appropriate function based on the user's selection.
    """
    print("Welcome to BASICS Text Editor!")
    while True:
        print("\nChoose an option:")
        print("1. Create a new file")
        print("2. Open an existing file")
        print("3. Edit a file")
        print("4. Exit")
        choice = input("Enter your choice (1-4): ")
        if choice == "1":
            create_file()
        elif choice == "2":
            open_file()
        elif choice == "3":
            edit_file()
        elif choice == "4":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")
if _name_ == "_main_":
    main()