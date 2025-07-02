def show_menu():
    print("\nChoose an option:")
    print("1. Read file")
    print("2. Write to file")
    print("3. Count characters")
    print("4. Search for a word")
    print("5. Replace word")
    print("6. Exit")

filename=input("enter filename with (.txt):")

def read_file():
    try:
        with open(filename,"r") as f:
            print(f.read())
    except FileNotFoundError:
        print("file not found error")

def write_file():
    text=input("enter text to write")
    with open(filename,"a") as f:
        f.write(text)
        print("new text is appended")
# with open(filename,"r") as m:
#         print(m.read())

def count_char():
    with open(filename,"r") as f:
        c=f.read()
        print("No.of character=",len(c))

def word_search():
    word=input("enter any word to search:")
    with open(filename,"r") as f:
        c=f.read()
        if word in c:
            print("word is present")
        else:
            print("word is not present")

def replace_word():
    old = input("enter old word:")
    new=input("enter new word to replace:")
    with open(filename,"r") as f:
       c=f.read()
       if old in c:
            c=c.replace(old,new)
            print("new string=",c)

while True:
    show_menu()
    choice=int(input("enter your choice:"))
    if choice==1:
        read_file()
    elif choice == 2:
        write_file()
    elif choice == 3:
        count_char()
    elif choice == 4:
        word_search()
    elif choice == 5:
        replace_word()
    elif choice == 6:
        print("Goodbye!")
        break
    else:
        print("Invalid choice.")



