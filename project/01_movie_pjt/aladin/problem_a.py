import json
from pprint import pprint



def book_info(book):
    book_info = {}
    book_info['id'] = book["id"] # int
    book_info['name'] = book["title"]
    book_info['author'] = book["author"]
    book_info['priceSales'] = book["priceSales"] # int
    book_info['description'] = book["description"]
    book_info['cover'] = book["book"]
    book_info['categoryId'] = book["categoryId"] # list 나머지는 str
    # 여기에 코드를 작성합니다.



# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    book_json = open('data/book.json', encoding='utf-8')
    book = json.load(book_json)

    pprint(book_info(book))
