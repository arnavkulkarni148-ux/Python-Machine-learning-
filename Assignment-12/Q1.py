#  Checking the character is vowel or not
def Check_vowel(ch):
    vowel_check = False
    vowels =["a","e","i","o","u","A","E","I","O","U"]
    for i in vowels:
        if i == ch:
            vowel_check = True
    return vowel_check

def main():

    print("Enter a Character")
    char = input()
    if Check_vowel(char) == True:
        print("You Enter a vowel..")
    else:
        print("You Enter a consonent..")

if __name__ == "__main__":
    main()