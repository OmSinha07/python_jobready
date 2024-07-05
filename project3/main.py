class library:
    def display (self,listofBooks):
        self.Books= listofBooks
    def displayAvailableBooks(self):
        print("Books present in this library are : ")
        for book in self.books:
            print(book)
