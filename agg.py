import os
import re

def main():
    with open("AGG.md", "w") as out:
        if os.path.exists("SUMMARY.md"):
            out.write("Contents:\n")
            summary = open("SUMMARY.md")
            lines = summary.readlines()

            to_process = []

            for line in lines:
                if line.lstrip().startswith("*"):
                    match = re.search(r"\((\S+)\)", line)
                    if not match:
                        continue
                    path = match.group(1)
                    tokens = path.split("/")
                    index = -1

                    elem_id = tokens[index][0:-3]

                    while elem_id == "README":
                        index -= 1
                        try:
                            elem_id = tokens[index]
                        except:
                            elem_id = "main"
                            break
                    
                    out.write(line.replace(path, f'#{elem_id}'))
                    to_process.append([path, elem_id, (len(line) - len(line.lstrip())) >> 1])

            for [path, elem_id, spaces] in to_process:

                print(f'Processing {path}')
                module = open(path, "r", encoding="utf-8")
                lines = module.readlines()

                lines = ["#" * spaces + line if line.startswith("#") else line for line in lines]

                out.write(lines[0] + f'<a name="{elem_id}"></a>')

                for line in lines[1:]:
                    out.write(line)

                out.write("\n")
        else:
            print("CAN NO FIND SUMMARY.md")

if __name__ == "__main__":
    main()