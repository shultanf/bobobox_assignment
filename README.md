# bobobox_assignment
Web-scrap code for bobobox internship take-home assignment.
This code will output a .json file (output.json) which contains the scrapped data from books.toscrape.com. A sample of the output data is provided in this repo in `sample_output/output.json`

# How to run in local
1. Open Docker Desktop in you local machine, minimize it and let it run in the background.
2. Clone this repository to your desired local directory
3. Navigate to the /bobobox_assignment directory
4. In your CLI, run `docker-compose up --build` if its your first time running this (might take a few minutes).
5. A folder should be created automatically, output result is located in `./output/output.json`
6. To close the image run `docker-compose down`, add `-v` to also delete the output folder/volume.



