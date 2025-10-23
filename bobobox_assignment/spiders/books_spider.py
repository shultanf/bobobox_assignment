import scrapy

class bookSpider(scrapy.Spider):
    name = "books" # Spider name

    # Start function
    def start_requests(self):
        urls = [
        "https://books.toscrape.com",
        "https://books.toscrape.com/catalogue/category/books/historical-fiction_4/index.html"
        ]
        yield scrapy.Request(url=urls[0], callback=self.parse)
        yield scrapy.Request(url=urls[1], callback=self.parse_hist_fiction)

    # Callback func for homepage
    def parse(self, response):
        books = response.css("article.product_pod::attr(class)").getall()
            
        xpath_category = '//*[@id="default"]/div/div/div/aside/div[2]/ul/li/ul/li/a'
        categories = response.xpath(f"{xpath_category}/text()").getall()
        
        if books or categories:
            yield {
                'page':'homepage',
                'page_url':response.url,
                'books':books,
                'categories':categories
            }
        else:
            self.logger.error(f"Element not found. Page: {response.url}")

    # Callback func for historical fiction page
    def parse_hist_fiction(self, response): 
        books = response.css("article.product_pod")
        if books:
            for index, book in enumerate(books):
                title = book.css("h3 a::attr(title)").get()
                price = book.css("p.price_color::text").get()
                rating = book.css("p.star-rating").attrib['class']
                
                yield {
                    'page':'historical_fiction',
                    'page_url':response.url,
                    'title':title,
                    'rating':rating,
                    'price':price
                }
        else:
            self.logger.error(f"Element not found. Page: {response.url}")
        # Loop next page until next_page == None
        next_page = response.css("li.next a::attr(href)").get()
        if next_page:
            yield response.follow(next_page, callback=self.parse_hist_fiction) # response.follow doesnt need to use urljoin()
