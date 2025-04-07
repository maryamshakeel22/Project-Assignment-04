
# Problem Statement
# In this program we show an example of using dictionaries to keep track of information in a phonebook.


#function to get phonebook
def phonebook():
    phonebook ={}

    while True:
        user_input = input("Enter a name (press Enter to stop): ")
        if user_input == "":
            break
        phonebook[user_input] = input("Enter a phone number: ")
    return phonebook
    
#function to print phonebook    
def print_phonebook(phonebook):
    for key in phonebook:
        print(f"{key} => {phonebook[key]}")

#function to lookup name in phonebook
def lookup_name(phonebook):
    name = input("Enter a name to lookup: ")
    if name in phonebook:
        print(f"{name} has the phone number {phonebook[name]}")
    else:
        print(f"{name} is not in the phonebook")

def main():
    phonebook_dict = phonebook()
    print_phonebook(phonebook_dict)   
    lookup_name(phonebook_dict)     




if __name__ == "__main__":
    main()
