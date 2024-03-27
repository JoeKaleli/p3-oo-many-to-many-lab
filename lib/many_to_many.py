class Book:
    _all_books = []

    def __init__(self, title):
        self.title = title
        self._all_books.append(self)

    @classmethod
    def all_books(cls):
        return cls._all_books


class Author:
    _all_authors = []

    def __init__(self, name):
        self.name = name
        self._all_contracts = []
        self._all_authors.append(self)

    @classmethod
    def all_authors(cls):
        return cls._all_authors

    def contracts(self):
        return self._all_contracts

    def books(self):
        return [contract.book for contract in self._all_contracts]

    def sign_contract(self, book, date, royalties):
        if not isinstance(book, Book):
            raise Exception("Book must be an instance of the Book class")
        if not isinstance(date, str):
            raise Exception("Date must be a string")
        if not isinstance(royalties, int) or royalties < 0:
            raise Exception("Royalties must be a non-negative integer")

        contract = Contract(self, book, date, royalties)
        self._all_contracts.append(contract)
        return contract

    def total_royalties(self):
        return sum(contract.royalties for contract in self._all_contracts)


class Contract:
    _all_contracts = []

    def __init__(self, author, book, date, royalties):
        self.author = author
        self.book = book
        self.date = date
        self.royalties = royalties
        self._all_contracts.append(self)

    @classmethod
    def contracts_by_date(cls, date):
        return [contract for contract in cls._all_contracts if contract.date == date]
