import random
import sys

pass_dict = ['abcdefghijklmnopqrstuvwxyz','ABCDEFGHIJKLMNOPQRSTUVWXYZ','1234567890',"~!@#$%^&*()_-+={}[]:;<>,.?"]

#pass_len = int(input("Enter the length of the password: "))

#pass_data = "abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890[];',./!@#$%^&*()_+:<>?"

def getPassLen():
    pass_len = int(input("Enter the length of the password: "))
    
    return pass_len

def getPassDict():
    print("*"*20)
    print("Choose which dictionary to use:")
    print("1. lower case letters only (i.e. abcd...)")
    print("2. upper case letters only (i.e. ABCD...)")
    print("3. numbers only (i.e. 1234...)")
    print("4. symbols only (i.e. !@#$...)")
    print("5. letters only (i.e. abcd...ABCD...)")
    print("6. Alphnumeric (i.e. abcd...ABCD...1234...)")
    print("7. Complex (i.e. all dictionaries)")
    dict_choice = int(input("Enter the the dictionary choice: "))

    if dict_choice < 5 and dict_choice > 0:
        return pass_dict[dict_choice - 1]
    elif dict_choice == 5:
        return "".join(pass_dict[:2])
    elif dict_choice == 6:
        return "".join(pass_dict[:3])
    elif dict_choice == 7:
        return "".join(pass_dict)
    else:
        print("Please enter a valid entry")
        print("Exiting")
        sys.exit()

#password = "".join(random.sample(pass_data, pass_len))

#print(password)

if __name__=='__main__':
    pass_len = getPassLen()
    pass_data = getPassDict()
    print("".join(random.sample(pass_data, pass_len)))
