'''
Создайте класс Library, представляющий библиотеку.
Класс должен иметь атрибуты books (список книг) и members (список членов библиотеки).
Реализуйте методы add_book(book) для добавления книги в библиотеку,
remove_book(book) для удаления книги из библиотеки,
add_member(member) для добавления нового члена библиотеки и
remove_member(member) для удаления члена библиотеки.
Также реализуйте метод checkout_book(book, member) для выдачи книги члену библиотеки и
return_book(book, member) для возврата книги в библиотеку.
'''


class Library:
    def __init__(self, books: list[str], members: list[str]):
        self.books = books
        self.members = list(set(members))
        self.member_books_dict = {}

    def add_book(self, book: str):
        self.books.append(book)

    def remove_book(self, book: str):
        if book in self.books:
            self.books.remove(book)
            return
        print(f'Книги "{book}" нет в библиотеке')

    def add_member(self, member: str):
        if member not in self.members:
            self.members.append(member)
            return
        print(f'Участник "{member}" уже есть в библиотеке')

    def remove_member(self, member: str):
        if member in self.members:
            self.members.remove(member)
            return
        print(f'Участника "{member}" нет в библиотеке')

    def checkout_book(self, book: str, member: str):
        if member not in self.members:
            print(f'Учатник {member} не является членом библиотеки')
            return

        if member not in self.member_books_dict:
            self.member_books_dict[member] = [book]
        else:
            self.member_books_dict[member].append(book)
        self.remove_book(book)

    def return_book(self, book: str, member: str):
        if member not in self.member_books_dict or \
                book not in self.member_books_dict[member]:
            print(f'Участник {member} не брал книгу {book}')
            return
        self.member_books_dict[member].remove(book)
        self.add_book(book)

    def __str__(self):
        return f'books: {self.books}; members: {self.members}\n{self.member_books_dict}'


a = Library(books=['a', 'b', 'c'], members=[])
a.add_member('Bob')
a.add_member('John')
print(a)
a.checkout_book(book='c', member='Bob')
a.checkout_book(book='a', member='Bob')
a.checkout_book(book='b', member='John')
print(a)
a.return_book(book='a', member='Bob')
print(a)
