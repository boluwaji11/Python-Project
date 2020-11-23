def negatives():
    # Open a file named philosophers.txt.
    infile = open(r'C:\Users\Boluwaji\Desktop\School Folder\MIS 5301 - Object Oriented Programming\Project\Step 4\negatives.txt', 'r')

    # Read the file's contents.
    file_contents = infile.read()

    # Close the file.
    infile.close()

    # Print the data that was read into memory.
    low = file_contents.split()
    print(low)

# Call the main function
negatives()
