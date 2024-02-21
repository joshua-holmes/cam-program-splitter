
import re, os
from pathlib import Path


def handle_user_input() -> (str, int):
    print("Please enter program number of CAM file with extension (.MX2, .MX3, .CAM Files only):")
    input_file_name = input()
    if len(input_file_name) < 5 or input_file_name[-4:] not in [".mx2", ".mx3", ".cam"]:
        raise Exception("Only file extensions allowed are: .mx2 .mx3 .cam")
    
    print("Please enter starting number of consecutive program file names (numeric values only):")
    output_num = input()
    if not output_num.isdigit():
        raise Exception("Please only enter numeric values")

    return (input_file_name, int(output_num))


def read_file(input_file_path: str) -> str:
    with open(input_file_path, 'r') as f:
        contents = f.read()
    return contents


def paginate(file_contents: str) -> list[str]:
    input_lines = file_contents.split("\n")
    title_block = input_lines[1]
    path_type = input_lines[6]
    page_start = [
        "%",
        title_block,
        path_type,
    ]
    pages = [page_start.copy()]
    for i in range(len(input_lines)):
        # exclusions
        if not input_lines[i] or input_lines[i][0] != "N":
            continue


        #Look for a Z in the Gcode Programming
        g_code_line = re.match("N[0-9]+", input_lines[i])[0]
        if "Z" in input_lines[i]:
            print(f"A Z move was found in Gcode Line (2-AXIS ONLY!): {g_code_line}\n")
        if g_code_line == "N1":
            continue
        if len(pages[-1]) + 1 >= 504:
            pages.append(page_start.copy())
        pages[-1].append(input_lines[i])

    #I-Loop for program number & adds % to program end.
    #Also adds all stings together to form single line for Gcode.
    for i in range(len(pages)):
        pages[i].insert(3, f"(PROGRAM {i + 1} OF {len(pages)})")
        pages[i].append("%")
        pages[i] = "\n".join(pages[i])
    return pages

#SAVE Contents as each individual Program
def save(paginated_contents: list[str], output_num: int):
    for i in range(len(paginated_contents)):
        with open(f"{output_num + i}.mx2", "w") as f:
            f.write(paginated_contents[i])


def main():
    try:
        cwd = Path(__file__).parent
        os.chdir(cwd)
        (input_file_path, output_num) = handle_user_input()
        file_contents = read_file(input_file_path)
        paginated_contents = paginate(file_contents)
        save(paginated_contents, output_num)

        print("Success! Press enter to exit")
        input()
    except Exception as e:
        # print(__file__)
        # print(os.getcwd())
        print("That didn't work, reach out if you have issues!\n \n", e)
        input()


if __name__ == "__main__":
    main()