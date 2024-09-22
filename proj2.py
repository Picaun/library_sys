import string
class Book:
    def __init__(self, title=None, author=None, isbn=None, available_copies = 0):
        self.title = title
        self.author = author
        self.isbn = isbn
        self._available_copies = available_copies

    @property
    def available_copies(self):
        """a get method for the available_copies attribute that allows getting the number of available copies but
    restricts direct setting of this attribute."""
        return self._available_copies

    @available_copies.setter
    def available_copies(self, value):
        """a setter method for available_copies that only allows non-negative values. If a negative value is provided,
    it should raise a ValueError with an appropriate message."""
        if isinstance(value, int):
            if value >= 0:
                self._available_copies = value
            else:
                raise ValueError("The number of available copies only allows non-negative values.")
        else:
            raise ValueError("your inputs must be an integer!")

class Library:
    def __init__(self):
        self.list_book = []

    def add_book(self, title=None, author=None, isbn=None, available_copies=None):
        """adds a new book to the library"""
        book = [title, author, isbn, available_copies]
        # print(book)
        if isinstance(book[3], int):    # 防止意外输入
            if book[3] >= 0:             # book[3] = available_copies
                if book not in self.list_book:
                    self.list_book.append(book)
                    print(f"{book[3]} books: 《{book[0]}》 were successfully added")
                else:
                    # self.list_book[self.list_book.index(book)] = [title, author, isbn, available_copies]
                    self.list_book[self.list_book.index(book)][3] += book[3]
                    print(f"{book[3]} new books were added to Book 《{book[0]}》")
            else:
                raise ValueError("The number of available copies only allows non-negative values.")
        else:
            raise ValueError("your inputs must be an integer!")

    def borrow_book(self,book_id=None, copies_num = 0):
        """allows borrowing a book (decreasing its available copies) if there are copies available."""
        borrow_book = book_id
        flags = 0
        for i in self.list_book:
            if borrow_book == [i[0], i[2]]:     # 只允许通过书名和ISBN查询
                # i = [title, author, isbn, available_copies]
                # print(type(i[3]))
                if i[3] >= copies_num:
                    self.list_book[self.list_book.index(i)][3] -= copies_num  # available_copies -= copies，更新self.list_book
                    print(f"{copies_num} 《{borrow_book[0]}》 books were successfully loaned")
                else:
                    print(f"\033[34m\nWe don't have the quantity of 《{borrow_book[0]}》 you need, There are only {i[3]} copies left\033[0m")
                flags = 1
        if flags == 0:
            print(f"\033[34m\nThe library doesn't have this book:《{borrow_book[0]}》."
                  f"The following books are currently available: \n\033[0m")
            print_library_list_book(self.list_book)

    def return_book(self, book_id = None, copies = 0):
        """allows returning a book (increasing its available copies)"""

        flags = 0
        return_book = book_id

        for i in self.list_book:
            if return_book == [i[0], i[2]]:     # 只允许通过书名和ISBN查询
                self.list_book[self.list_book.index(i)][3] += copies  # available_copies -= copies 更新self.list_book
                print(f"{copies} 《{return_book[0]}》 books were successfully returned")
                flags = 1
                break
        if flags == 0:
            print(f"The library doesn't have this book:《{return_book[0]}》,"
                  f"But you could consider donating it to the library. Thank you")


    def clear_books(self, operand = 0, book_id = None):
        """
            operand = 0 ---> Clear specific books in Library
            operand = 1 ---> Clear all books in Library
        """
        flags = 0
        if operand == 0:
            for i in self.list_book:
                if book_id == [i[0], i[2]]:     # 只允许通过书名和ISBN查询
                    self.list_book.pop(self.list_book.index(i))
                    flags = 1
                    break

        elif operand == 1:
            self.list_book = []     # 清空图书馆的书籍
        else:
            print("\033[31mOperand must be 0 or 1 !\033[0m")

        if flags == 0:
            print(f"No book: title:{book_id[0]},ISBN:{book_id[1]} here!")



def print_library_list_book(list_book=None):
    """
        list_book = [[title_1, author_1, isbn_1, available_copies_1],
                    [title_2, author_2, isbn_2, available_copies_2],
                                    ...
                    [title_n, author_n, isbn_n, available_copies_n]]
    """
    if not list_book:
        print("No books are currently saved, please add books")
    else:
        print("The library has the following books available:\n")
        for i in list_book:
            print(f"title: {i[0]}, author: {i[1]}, ISBN: {i[2]}, available_copies: {i[3]}")


def in_list_library_book_id(x, list_book_id):
    flags = 0
    for y in list_book_id:
        y = eval(y)
        if x == [y[0], y[2]]:
            # print("True")
            flags = 1
    if flags:
        return True
    else:
        return False

def contains_punctuation(user_input):
    # 检查输入中是否包含标点符号
    flags = 0
    for char in user_input:
        if char in string.punctuation:
            flags = 1
    if flags == 1:
        return True
    else:
        return False

def main():
    library = Library()
    list_library_book_title = []    # 图书馆现有所有书的title

    """
    存放library里面每一本书的id："[title,author,isbn]"
    list_library_book_id = ["[title_1, author_1, isbn_1, available_copies_1]",
                            "[title_2, author_2, isbn_2, available_copies_2]",
                                                ...
                            "[title_n, author_n, isbn_n, available_copies_n]"]
    """
    list_library_book_id = []

    while True:
        # 记录图书馆所有书的title
        # print( library.list_book)
        for book in library.list_book:
            list_library_book_title.append(book[0])
        # print(list_library_book_title)

        # 交互部分
        operand = input("Select the action you need:"+'\n'+
                            "1: Add books"+'\n'+
                            "2: Modify the number of books remaining"+'\n'+
                            "3: Borrow books"+'\n'+
                            "4: Return books"+'\n'+
                            "5: Clear books (specific book or all)"+'\n'+
                            "6: View existing books in the library"+'\n'+
                            "0: Shutdown system"+'\n'+
                            "Select a number to perform the corresponding operation:\n")
        if not operand.isdigit():
            print("\033[31m\nPlease enter Arabic numerals and no other characters !\n\033[0m")
            continue
        else:
            operand = int(operand)
            i = 0


            # ============================================Add books=====================================================

            while operand == 1:
                flag_1 = 0    # 有输入错误时置1，无错时置0
                print("\033[34m\nPlease double check that the input is correct !\n\033[0m")
                title = input("Enter a book title:\n")
                author = input("Enter a book author:\n")
                isbn = input("Enter a book ISBN:\n")
                available_copies = input("Enter number of available copies:\n")
                if not available_copies.isdigit():
                    print("\033[31m\nThe number of available copies must be Arabic numerals and no other characters !\n\033[0m")
                    continue
                else:
                    available_copies = int(available_copies)

                if contains_punctuation(title):
                    print("\033[31m\nThe input cannot contain a string !\n\033[0m")
                    continue
                if contains_punctuation(author):
                    print("\033[31m\nThe input cannot contain a string !\n\033[0m")
                    continue
                if  contains_punctuation(isbn):
                    print("\033[31m\nThe input cannot contain a string !\n\033[0m")
                    continue
                if title == '' :
                    print("\033[31m\nThe input cannot be empty !\n\033[0m")
                    continue
                if author == '' :
                    print("\033[31m\nThe input cannot be empty !\n\033[0m")
                    continue
                if  isbn == '':
                    print("\033[31m\nThe input cannot be empty !\n\033[0m")
                    continue

                key = f"['{title}','{author}','{isbn}']"

                #  输入异常规避
                # print(list_library_book_id)
                for n in list_library_book_id:
                    # ISBN重复的情况下，title, author必须相同，否则一定是输入错误
                    if eval(n)[2] == isbn and len(list({eval(n)[0], eval(n)[1]} & {title, author})) <= 1:
                        print("\033[31m\nPlease double check that the input is correct !"
                              " one of the title, author, ISBNs might be typed incorrectly! Please re-enter!\n\033[0m")
                        flag_1 = 1
                        continue

                # 添加书籍部分 ===================================================================================
                if flag_1 == 0:
                    # 生成可能的多个Book的实例，并将其添加到library.list_book[]
                    i += 1
                    if key not in list_library_book_id:
                        # 存入图书馆
                        book = Book(title, author, isbn, available_copies)
                        exec(f'book_{i} = book')  # 一定不能写exec(f 'book_{i} = {book}')，这样操作是把book实例的地址返给book_i
                        exec(f'library.add_book(book_{i}.title, book_{i}.author, book_{i}.isbn, book_{i}.available_copies)')
                        # print(library.list_book)

                        list_library_book_id.append(key)
                    else:
                        # 添加输入的重复书籍
                        for m in library.list_book:
                            if title in m:
                                library.list_book[library.list_book.index(m)][3] += available_copies
                                print(f"{available_copies} books：《{m[0]}》 were successfully added\n")

                                # print(f"{library.list_book}")
                            else:
                                print("?????1") # 尚不清楚什么情况会导向这里
                                pass
                else:
                    print(f"\033[31m\nFailed to add book:title: {title},author:{author},ISBN:{isbn}\n\033[0m")
                    pass


                # 衔接部分 ==============================================================================================
                check = input("\033[34m\nEnter 1 to continue adding books "
                              "or input any other characters to perform other operations\n\033[0m")

                if check == '1':
                    # print("1")
                    continue
                else:
                    # print("2")
                    break

            # ============================================Add books=====================================================


            # ==================================Modify the number of books remaining====================================

            while operand == 2:
                flag_2 = 0   #  功能完成进入衔接环节置1，默认置0
                if len(library.list_book) == 0:
                    print("\033[31m\nThere are no available books ! Please use the Add Book function : 1\n\033[0m")
                    break
                else:
                    # print(list_library_book_title)
                    print(f"The title of all the books in the library are as follows:\n"+" ".join(list_library_book_title))
                    edit_book_title = input("Enter a book title in library:\n")
                    edit_book_copies = input("Enter the number of copies you want to change:\n")
                    # 修改title对于的available_copies值
                    if not edit_book_copies.isdigit():
                        print("\033[31m\nPlease enter Arabic numerals and no other characters !\n\033[0m")
                        continue
                    else:
                        edit_book_copies = int(edit_book_copies)
                        for i in library.list_book:
                            if edit_book_title in i:
                                library.list_book[library.list_book.index(i)][3] = edit_book_copies
                                print(f"The available copies of book 《{edit_book_title}》 has been successfully modified to {edit_book_copies}\n")
                                print_library_list_book(library.list_book)
                                flag_2 = 1
                                break
                        if flag_2 == 0:
                            print(f"\033[31m\nThe title of the books are not in the library, Please try again!\n\033[0m")
                            continue

                if flag_2 == 1:
                    check = input("\033[34m\nEnter 2 to continue Modify the number of books remaining "
                                  "or input any other characters to perform other operations\n\033[0m")
                    if check == '2':
                        # print("1")
                        continue
                    else:
                        # print("2")
                        break

            # ==================================Modify the number of books remaining====================================


            # ============================================Borrow books==================================================

            while operand == 3:
                flag_3 = 0   #  功能完成进入衔接环节置1，默认置0

                if len(library.list_book) == 0:     # 要现有书才能借书
                    print("\033[31m\nThere are no available books ! Please use the Add Book function: 1\n\033[0m")
                    break
                else:
                    print_library_list_book(library.list_book)
                    try:
                        book_title,book_isbn = input("\nEnter the title and ISBN of the book you want to borrow: "
                                                     "(Such as: \033[34m title ISBN \033[0m,title and ISBN are separated by a space)\n").split()
                    except ValueError:
                        print("\033[31m\nPlease enter a valid value !\n\033[0m")
                        continue
                    book_id = [book_title,book_isbn]
                    # print(book_id)

                    if not in_list_library_book_id(book_id, list_library_book_id):
                        print("\033[31m\nThe book you are looking for could not be found, please make sure you enter it correctly\n\033[0m")
                        continue
                    else:
                        copies_num = input("\nEnter the number of copies you want to borrow:"
                                           "(Only Arabic digits can be entered)\n")
                        if not copies_num.isdigit():
                            print("\033[31m\nPlease enter Arabic numerals and no other characters !\n\033[0m")
                            continue
                        else:
                            copies_num = int(copies_num)
                            library.borrow_book(book_id, copies_num)
                            print_library_list_book(library.list_book)
                            flag_3  = 1

                if flag_3 == 1:
                    check = input("\033[34m\nEnter 3 to continue Borrow books "
                                  "or input any other characters to perform other operations\n\033[0m")
                    if check == '3':
                        # print("1")
                        continue
                    else:
                        # print("2")
                        break



            # ============================================Borrow books==================================================


            # ============================================Return books==================================================

            while operand == 4:
                flag_4 = 0  # 功能完成进入衔接环节置1，默认置0

                if len(library.list_book) == 0:  # 要现有书才能借书
                    print("\033[31m\nThere are no available books ! Please use the Add Book function: 1\n\033[0m")
                    break
                else:
                    print_library_list_book(library.list_book)
                    try:
                        book_title, book_isbn = input("\nEnter the title and ISBN of the book you want to return: "
                                                      "(Such as: \033[34m title ISBN \033[0m,title and ISBN are separated by a space)\n").split()
                    except ValueError:
                        print("\033[31m\nPlease enter a valid value !\n\033[0m")
                        continue
                    book_id = [book_title, book_isbn]


                    copies_num = input("\nEnter the number of copies you want to return:"
                                       "(Only Arabic digits can be entered)\n")
                    if not copies_num.isdigit():
                        print("\033[31m\nPlease enter Arabic numerals and no other characters !\n\033[0m")
                        continue
                    else:
                        copies_num = int(copies_num)
                        library.return_book(book_id, copies_num)
                        print_library_list_book(library.list_book)
                        flag_4 = 1

                if flag_4 == 1:
                    check = input("\033[34m\nEnter 4 to continue Borrow books "
                                  "or input any other characters to perform other operations\n\033[0m")
                    if check == '4':
                        # print("1")
                        continue
                    else:
                        # print("2")
                        break

            # ============================================Return books==================================================


            # ============================================Clear books===================================================

            while operand == 5:
                flag_5 = 0  # 功能完成进入衔接环节置1，默认置0
                flag_5_1 = 0    # 1:已完成清除图书馆所有书籍的功能
                if len(library.list_book) == 0:  # 要有书才能清除书
                    print("\033[31m\nThere are no available books ! Please use the Add Book function: 1\n\033[0m")
                    break
                else:
                    clear_operand = input("There are two patterns here:\n"
                                          "0 ---> Clear specific books in Library\n"
                                          "1 ---> Clear all books in Library\n")
                    """
                        clear_operand = 0 ---> Clear specific books in Library
                        clear_operand = 1 ---> Clear all books in Library
                    """
                    if not clear_operand.isdigit():
                        print("\033[31m\nPlease enter Arabic numerals and no other characters !\n\033[0m")
                        continue
                    else:
                        clear_operand = int(clear_operand)
                        if clear_operand == 1:
                            library.clear_books(clear_operand)
                            flag_5_1 = 1
                        elif clear_operand == 0:
                            print_library_list_book(library.list_book)
                            try:
                                book_title, book_isbn = input(
                                    "\nEnter the title and ISBN of the book you want to return: "
                                    "(Such as: \033[34m title ISBN \033[0m,title and ISBN are separated by a space)\n").split()
                            except ValueError:
                                print("\033[31m\nPlease enter a valid value !\n\033[0m")
                                continue
                            book_id = [book_title, book_isbn]
                            library.clear_books(clear_operand,book_id)
                            flag_5 = 1   # 功能完成进入衔接环节置1，默认置0
                        else:
                            print("\033[31m\nYou can only type 0 or 1 !\n\033[0m")
                            continue
                        print_library_list_book(library.list_book)

                if flag_5 == 1 or flag_5_1 == 1:
                    check = input("\033[34m\nEnter 5 to continue Clear books "
                                  "or input any other characters to perform other operations\n\033[0m")
                    if check == '5':
                        # print("1")
                        continue
                    else:
                        # print("2")
                        break


            # ============================================Clear books===================================================


            # ================================View existing books in the library========================================

            while operand == 6:
                flag_6 = 0
                if len(library.list_book) == 0:
                    print("\033[31m\nThere are no available books ! Please use the Add Book function: 1\n\033[0m")
                    break
                else:
                    print_library_list_book(library.list_book)
                    flag_6 = 1

                if flag_6 == 1:
                    check = input("\033[34m\nEnter 6 to continue Borrow books "
                                  "or input any other characters to perform other operations\n\033[0m")
                    if check == '6':
                        # print("1")
                        continue
                    else:
                        # print("2")
                        break

            # ================================View existing books in the library========================================


            # ==========================================Shutdown system=================================================

            if operand == 0:
                sec_operand = input("\033[34mIs the exit really confirmed? Confirm: 1 Cancel: 0\033[0m\n")
                if sec_operand == '1':
                    break
                elif sec_operand == '0':
                    continue
                else:
                    print("\033[31m\nInput error, can only enter 1 or 0\n\033[0m")
                    continue

            # ==========================================Shutdown system=================================================


def text_class():
    # 只是测试一下book类的available_copies属性修改，和图书管理系统无关
    a = Book('a1','aa','111',5)
    b = Book('b1','ba','222',5)
    c = Library()
    print(f"a图书剩余个数：{a.available_copies}\nb图书剩余个数：{b.available_copies}")
    available_copies_a = input(f"修改a图书剩余个数为:")
    available_copies_b = input(f"修改b图书剩余个数为:")
    a.available_copies = int(available_copies_a)
    b.available_copies = int(available_copies_b)
    print(f"更改后：\na图书剩余个数：{a.available_copies}\nb图书剩余个数：{b.available_copies}")
    print('#'*50)

    # 添加书籍
    print('-' * 30 + "添加书" + '-' * 30)
    c.add_book(a.title, a.author, a.isbn, a.available_copies)
    c.add_book(a.title, a.author, a.isbn, a.available_copies)  # test
    c.add_book(b.title, b.author, b.isbn, b.available_copies)
    print(f"目前图书馆有这些书:{c.list_book}")
    print('-' * 30 + "添加书" + '-' * 30 + '\n')

    # 借书
    print('-' * 30 + "借书" + '-' * 30)
    c.borrow_book(['title_test','isbn_test'], 10)
    c.borrow_book([a.title,a.isbn], 5)
    print(f"目前图书馆有书：{c.list_book}")
    print('-' * 30 + "借书" + '-' * 30 + '\n')

    # 还书
    c.return_book(a.title,10)
    print('-' * 30 + "还书" + '-' * 30)
    print(f"目前图书馆有书：{c.list_book}")
    print('-' * 30 + "还书" + '-' * 30 + '\n')






if __name__ == "__main__":
    # text_class()
    main()









