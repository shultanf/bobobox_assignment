from itemadapter import ItemAdapter
import json
import os


class BoboboxAssignmentPipeline:
    def open_spider(self, spider):
        # self.output = dict() # Main dict
        self.book_info_list = list()

        
        

        # Word-to-int map for rating value
        self.word_map = {
            'zero':0,
            'one':1,
            'two':2,
            'three':3,
            'four':4,
            'five':5
        }
    
    
    def process_item(self, item, spider):
        page = item['page'] # Define page name

        # Process if item from home page
        if page == 'homepage':
            # Clean item
            source_url = item['page_url']
            total_books_scraped_from_homepage = len(item['books']) # Count scrapy object element from scrapy Selector

            # Define dict value for "all_book_categories"
            self.all_book_categories = [category.strip() for category in item['categories']] # Remove whitespaces from each string

            # Define dict value for "metadata"
            self.metadata = { 
                "source_url":source_url,
                "total_books_scraped_from_homepage":total_books_scraped_from_homepage
            }
        
        # Process if item from historical fiction page
        elif page == 'historical_fiction':
            # Clean item
            title = item['title']
            price_gbp = float(item['price'].replace("£",""))
            rating_stars = self.word_map.get(item['rating'].split(" ")[-1].lower(), None)

            # Define dict value for "historical_fiction_books"
            book_info = {
                "title":title,
                "price_gbp":price_gbp,
                "rating_stars":rating_stars
            }

            # Append each book info
            self.book_info_list.append(book_info)
        
        return item

    def close_spider(self, spider):
        # Insert transformed value to output dict
        output_dict = {
            'metadata':self.metadata,
            'all_book_categories':self.all_book_categories,
            'historical_fiction_books':self.book_info_list
        }

        # Create dir inside container and file path for output json
        folder_path = "/app/output/"
        os.makedirs(folder_path, exist_ok=True)
        file_path = os.path.join(folder_path, "output.json")

        # Save json output to container: /app/output_data/output.json
        # Host machine will mount local "./output/output.json" to container "app/output/output.json"
        try:
            with open(file_path, "w", encoding="utf-8") as f:
                json.dump(output_dict, f, ensure_ascii=False, indent=2)
            spider.logger.debug(f"Data saved successfully to {self.file_path}")
        except Exception as e:
            spider.logger.error(f"Error when saving data: {e}")



