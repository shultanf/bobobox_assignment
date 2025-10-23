# web_scrape
This repo contains code that will scrape html data from book.toscrape.com using scrapy in python. This code will output a .json file (output.json) which contains the scrapped data. A sample of the output data is provided in this repo in `sample_output/output.json`

# How to run in local
1. Install and open Docker Desktop in you local machine, minimize it and let it run in the background.
2. Clone this repository to your desired local directory: `git clone https://github.com/shultanf/bobobox_assignment.git`
3. Navigate to the directory: `cd bobobox_assignment`
4. Run `docker-compose up --build` if its your first time running this (might take a few minutes while dependecies install).
5. A folder should be created automatically, output result is located in `./output/output.json`
6. To close the container, run `docker-compose down`, add `-v` to also delete the volumes.



