def main():
    try:
        # Ask user for the input file name
        inputfile = input("Enter the name of the file to read from: ")

        # Attempt to read the file
        try:
            with open(r'Python\WEEK 4\inputfile', 'r') as file:
                content = file.read()
                print("\nFile read successfully!")
        except FileNotFoundError:
            print(f"Error: The file '{inputfile}' was not found. Please check the filename and try again.")
            return  # Exit the program if the file is not found
        except IOError:
            print(f"Error: Could not read the file '{inputfile}'. Check if the file is accessible.")
            return

        # Modify the content (convert to uppercase)
        modified = content.upper()

        # Ask for output file name
        outputfile = input("Enter the name of the new file to write to: ")

        # Write the modified content
        try:
            with open(r'Python\WEEK 4\outputfile', 'w') as file:
                file.write(modified)
                print(f"\nModified content written to '{outputfile}' successfully.")
        except IOError:
            print(f"Error: Could not write to the file '{outputfile}'. Please check the file path and try again.")

    except Exception as e:
        print(f"An unexpected error occurred: {e}")

if __name__ == "__main__":
    main()
