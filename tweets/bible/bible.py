# Python program to format raw output for Bible bot

# Original:

# 13:13 But out of that camel, the divistines that are
# stayed for meats: then ye are entered in our brethren; and overthose one
# belonish thee, and was not in things that come;
# These things I do, that thou art my trust in your doubt.

# 46:4 Behold, the kingdom was committed bitterness, and shall remember
# his very priests, then the gray of God is written in the holy things
# with fast, behold, a burnt offering and all his sins he maketh strong; that
# leadeth over him.

# 49:29 For night, and easifuling, according to come, he will divide the
# people in life, beway straight with the house of the LORD, even unto the
# east of Tekitaboth.

# Cleaned:

# 13:13 But out of that camel, the divistines that are stayed for meats: then ye are entered in our brethren; and overthose one belonish thee, and was not in things that come; These things I do, that thou art my trust in your doubt.

# 46:4 Behold, the kingdom was committed bitterness, and shall remember his very priests, then the gray of God is written in the holy things with fast, behold, a burnt offering and all his sins he maketh strong; that leadeth over him.

# 49:29 For night, and easifuling, according to come, he will divide the people in life, beway straight with the house of the LORD, even unto the east of Tekitaboth.

CHARACTER_LIMIT = True # If you need to filter results by a character limit
LIMIT = 280

lines = None

with open(input("File: "), "r") as f:
    lines = f.read()
    lines = lines.splitlines()

new_lines = []
current_line = ""
new_verse = True

for line in lines:
    if line == "":
        if CHARACTER_LIMIT:
            if len(current_line) > LIMIT:
                print("Skipped a line for character limit...")
            else:
                new_lines.append(current_line)
        else:
            new_lines.append(current_line)
        current_line = ""
        new_verse = True
    else:
        if new_verse:
            current_line += line
            new_verse = False
        else:
            current_line = f"{current_line} {line}"

with open(input("Write Output: "), "w") as f:
    for line in new_lines:
        f.write(f"{line}\n")