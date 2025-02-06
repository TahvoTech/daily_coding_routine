import os  # Import the os module to interact with the operating system

# List of topics for which we want to create Python files
topics = [
    "data_processing",
    "visualization",
    "file_operations",
    "string_utils"
]

# Get the directory of the current script file
output_dir = os.path.dirname(__file__)

# Loop through each topic in the topics list
for topic in topics:
    # Create a filename by replacing spaces and removing parentheses
    filename = f"{topic}.py"
    # Create the full file path by joining the directory and filename
    filepath = os.path.join(output_dir, filename)
    
    # Open the file in write mode
    with open(filepath, 'w') as f:
        # Write a comment at the top of the file with the module name
        f.write(f"# {topic.capitalize()} module\n\n")
        # Write a placeholder main function
        f.write("def main():\n")
        f.write("    pass\n\n")
        # Write the standard boilerplate to call the main function
        f.write("if __name__ == '__main__':\n")
        f.write("    main()\n")

# Print a success message with the output directory
print(f"Python files created successfully in {output_dir}.")
