#  Checking the character is vowel or not
def main():
    vowels =["a","e","i","o","u","A","E","I","O","U"]

    print("Enter a Character")
    char = input()
    check_vowel = False

    for i in vowels:
        if i == char:
            check_vowel = True
    if check_vowel == True:
        print("You Enter a vowel..")
    else:
        print("You Enter a consonent..")

if __name__ == "__main__":
    main()