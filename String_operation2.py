def convert_to_uppercase():
    print("Enter lines of text (press Enter twice to finish):")
    lines = []
    while True:
        line = input()
        if line == "":
            break
        lines.append(line.upper())
    print("\nConverted Output:")
    for l in lines:
        print(l)

convert_to_uppercase()