from BookHierarchy import Book, BookList

Hobbit = {
    'title': 'The Hobbit',
    'author': 'J.R.R. Tolkien',
    'synopsis': 'Synopsis',
    'publisher': 'George Allen & Unwin',
    'publish_date': '1937-09-21',
    'page_count': 310,
    'tags': ['Fantasy', 'Adventure']
}

Fellowship = {
    'title': 'The Fellowship of the Ring',
    'author': 'J.R.R. Tolkien',
    'synopsis': 'Synopsis',
    'publisher': 'George Allen & Unwin',
    'publish_date': '1954-07-29',
    'page_count': 423,
    'tags': ['Fantasy', 'Adventure']
}

TwoTowers = {
    'title': 'The Two Towers',
    'author': 'J.R.R. Tolkien',
    'synopsis': 'Synopsis',
    'publisher': 'George Allen & Unwin',
    'publish_date': '1954-11-11',
    'page_count': 352,
    'tags': ['Fantasy', 'Adventure']
}

ReturnOfTheKing = {
    'title': 'The Return of the King',
    'author': 'J.R.R. Tolkien',
    'synopsis': 'Synopsis',
    'publisher': 'George Allen & Unwin',
    'publish_date': '1955-10-20',
    'page_count': 416,
    'tags': ['Fantasy', 'Adventure']
}

Silmarillion = {
    'title': 'The Silmarillion',
    'author': 'J.R.R. Tolkien',
    'synopsis': 'Collection of mythopoeic tales providing extensive background to Middle-earth.',
    'publisher': 'George Allen & Unwin',
    'publish_date': '1977-10-20',
    'page_count': 365,
    'tags': ['Fantasy', 'Mythopoeia']
}

UnfinishedTales = {
    'title': 'Unfinished Tales of Númenor and Middle-earth',
    'author': 'J.R.R. Tolkien',
    'synopsis': 'Collection of narratives and incomplete stories providing further insight into Middle-earth.',
    'publisher': 'George Allen & Unwin',
    'publish_date': '1980-10-21',
    'page_count': 472,
    'tags': ['Fantasy', 'Narratives']
}

ChildrenOfHurin = {
    'title': 'The Children of Húrin',
    'author': 'J.R.R. Tolkien',
    'synopsis': 'Complete and expanded version of a tale found in "The Silmarillion," focusing on the tragic story of Túrin Turambar.',
    'publisher': 'Houghton Mifflin',
    'publish_date': '2007-11-22',
    'page_count': 320,
    'tags': ['Fantasy', 'Tragedy']
}

FallOfGondolin = {
    'title': 'The Fall of Gondolin',
    'author': 'J.R.R. Tolkien',
    'synopsis': 'Tells the story of the legendary city of Gondolin and its downfall, edited by Christopher Tolkien.',
    'publisher': 'HarperCollins',
    'publish_date': '2018-12-23',
    'page_count': 304,
    'tags': ['Fantasy', 'Legendary']
}

def add_books_to_BookList():
    BookList.add(Book(**Hobbit))
    BookList.add(Book(**Fellowship))
    BookList.add(Book(**TwoTowers))
    BookList.add(Book(**ReturnOfTheKing))
    BookList.add(Book(**Silmarillion))
    BookList.add(Book(**UnfinishedTales))
    BookList.add(Book(**ChildrenOfHurin))
    BookList.add(Book(**FallOfGondolin))