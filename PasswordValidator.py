def main():
    filename = open("password.txt")
    contents = filename.read()
    split = contents.split("\n")
    count = int(split[0])
    index = 1
    while count >= index:
        if password_check(split[index]):
            print("YES " + split[index])
        else:
            print("NO " + split[index])
        index += 1


def password_check(passwd):
    SpecialSym =['~', '!', '@', '#', '$', '%', '^', '&', '*']
    val = True
    if len(passwd) < 8:
        val = False
    if len(passwd) > 32:
        val = False
    if not any(char.isdigit() for char in passwd):
        val = False
    if not any(char.isupper() for char in passwd):
        val = False
    if not any(char.islower() for char in passwd):
        val = False
    if not any(char in SpecialSym for char in passwd):
        val = False
    if passwd[0].isdigit():
        val = False
    for char in passwd:
        if char not in SpecialSym and char.isalpha() == False and char.isdigit() == False:
            val = False
    if val:
        return val


main()
