# -*- coding: utf-8 -*-
"""
Created on Tue May 21 14:38:25 2024

@author: WEIUGR
"""

"""
Created on Tue May 21 04:12:34 2024

Author: Hirak
"""

from pathlib import Path
from tkinter import filedialog, Tk
import re

def replace_commas_with_points(input_file):
    try:
        with open(input_file, 'r') as infile:
            data = infile.read()
            modified_data = data.replace(',', '.')

        output_file = Path(input_file).stem + '_replaced.txt'
        with open(output_file, 'w') as outfile:
            outfile.write(modified_data)
        
        print(f"Commas replaced with points successfully. Output saved as '{output_file}'")
        return output_file
    except FileNotFoundError:
        print(f"File not found: {input_file}")
    except IOError as e:
        print(f"An I/O error occurred: {e}")
        return None

def save_lines_between(file_path, target_line):
    try:
        with open(file_path, 'r') as file:
            lines = file.readlines()

        copying = False
        output_lines = []
        occurrence_count = 0
        saved_files = []

        for line in lines:
            if target_line in line:
                if copying:
                    output_lines.reverse()
                    sanitized_target_line = re.sub(r'\s+', '_', target_line.strip())
                    #save_file_name = f"output_{sanitized_target_line}_{occurrence_count + 1}.txt"
                    save_file_name = f"sample_{occurrence_count + 1}.txt"
                    with open(save_file_name, 'w') as save_file:
                        save_file.writelines(output_lines)
                    saved_files.append(save_file_name)
                    print(f"Lines between occurrences saved to {save_file_name} in reverse order")
                    occurrence_count += 1

                copying = True
                output_lines = [line]
            elif copying:
                output_lines.append(line)

        if occurrence_count == 0 and not output_lines:
            print(f"Target line not found: {target_line}")
        else:
            output_lines.reverse()
            #save_file_name = f"{Path(file_path).stem}_inverted.txt"
            save_file_name = f"{'sample_0'}.txt"
            with open(save_file_name, 'w') as save_file:
                save_file.writelines(output_lines)
            saved_files.append(save_file_name)
            print(f"Lines between occurrences saved to {save_file_name} in reverse order")

        return saved_files

    except FileNotFoundError:
        print(f"File not found: {file_path}")
    except IOError as e:
        print(f"An I/O error occurred: {e}")
        return []

def read_generated_files(file_list):
    for file_name in file_list:
        try:
            with open(file_name, 'r') as file:
                print(f"Contents of {file_name}:")
                print(file.read())
                print("---")
        except FileNotFoundError:
            print(f"File not found: {file_name}")
        except IOError as e:
            print(f"An error occurred while reading {file_name}: {e}")

def main():
    # Initialize Tkinter root and hide the main window
    root = Tk()
    root.withdraw()

    # Select input files
    file_paths = filedialog.askopenfilenames(filetypes=[("Text files", "*.txt")])

    # Close the Tkinter root window
    root.destroy()

    if file_paths:
        for file_path in file_paths:
            # Step 1: Replace commas with points
            replaced_file = replace_commas_with_points(file_path)
            
            if replaced_file:
                # Step 2: Save lines between occurrences of the target line in reverse order
                target_line = 'MTtodo por defecto'  # Replace with the line you want to check
                generated_files = save_lines_between(replaced_file, target_line)

                # Step 3: Read and print the contents of the generated files
                read_generated_files(generated_files)
    else:
        print("No files selected.")

if __name__ == "__main__":
    main()
