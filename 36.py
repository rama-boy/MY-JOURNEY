# book list program

book_list = []
while True:
    print("\n=== ENTER BOOK DATA ===")
    title = input("Book title\t: ")
    author = input("Author's name\t: ")
    
    new_book = [title,author]
    book_list.append(new_book)

    print("\n\n","="*10,"BOOK DATA","="*10)
    for index,book in enumerate(book_list):
        print(f"{index+1} | {book[0]} | {book[1]}")
        
    print("\n\n","="*20)
    isNext = input("Continue Buying?(yes/no) ")

    if isNext == "no":
        break

print("END PROGRAM")