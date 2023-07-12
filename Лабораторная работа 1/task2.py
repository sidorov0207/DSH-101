# TODO Найдите количество книг, которое можно разместить на дискете

symbol_size = 4
stroka_size = symbol_size * 25
page_size = stroka_size * 50
book_size = page_size * 100
book_size_kb = book_size / 1024

disk_size_kb = 1.44 * 1024

books = disk_size_kb // book_size_kb

print(f"Количество книг, помещающихся на дискету: {books:.0f}")
