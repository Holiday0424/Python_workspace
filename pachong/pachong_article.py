import requests
from lxml import etree
import csv

url = 'http://search.dangdang.com/?key=Python&act=input'

headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/120.0.0.0 Safari/537.36',
    'Referer': 'http://search.dangdang.com/',
}


def safe_get(lst, default=''):
    """安全获取列表第一个元素"""
    return lst[0].strip() if lst else default


def parse_html(html):
    selector = etree.HTML(html)
    book_list = selector.xpath('//ul[@class="bigimg"]/li')  # 更健壮的选择方式
    for book in book_list:
        title = safe_get(book.xpath('.//a/@title'))
        link = safe_get(book.xpath('.//a/@href'))
        price = safe_get(book.xpath('.//span[@class="search_now_price"]/text()'))
        author = safe_get(book.xpath('.//p[@class="search_book_author"]/span[1]/a/@title'))
        publish_date = safe_get(book.xpath('.//p[@class="search_book_author"]/span[2]/text()')).replace('/', '').strip()
        publisher = safe_get(book.xpath('.//p[@class="search_book_author"]/span[3]/a/@title'))

        yield {
            '书名': title,
            '链接': link,
            '价格': price,
            '作者': author,
            '出版日期': publish_date,
            '出版社': publisher
        }


def save_data():
    with open('dangdang_books.csv', 'w', newline='', encoding='utf-8-sig') as f:
        writer = csv.DictWriter(f, fieldnames=['书名', '链接', '价格', '作者', '出版日期', '出版社'])
        writer.writeheader()
        response = requests.get(url, headers=headers)
        response.encoding = 'gbk'  # 当当网常用 gbk 编码！
        for item in parse_html(response.text):
            if item['书名']:  # 只保存有效数据
                writer.writerow(item)


if __name__ == '__main__':
    save_data()