# Presta-Forfiter
## Internet shop project

## CONTENTS

- [USED SOFTWARE](#technologies)
- [RUN SCRAPER](#run-scraper)
- [RUN SHOP](#run-shop)
- [RUN TESTS](#run-tests)
- [AUTHORS](#authors)

## SOFTWARE

1. Prestashop v1.7.8
2. MariaDB
3. Docker
4. Python
5. Scrapy
6. Selenium

## RUN SCRAPER
Run commands in order in directory of ForfitScraper:

```
scrapy crawl category -O ../scrapped_data/categories.json
```
```
scrapy crawl alco -O ../scrapped_data/products.json
```
```
scrapy crawl detail -O ../scrapped_data/details.json
```
```
python download_photos.py
```

Commands are also in run.ps1 Windows Powershell file.

## RUN SHOP
To ensure all components running smoothly, first run chmod in the main directory.
```
sudo chmod -R 777 shop-src
```

Next, initialize the Docker container. Navigate to shop-config directory and run:
```
docker compose up
```

After booting the container, you can access the shop website at:
```
http://localhost:8080/
```

To make changes to the website, navigate to the admin panel and log in using the correct credentials.
```
http://localhost:8080/admin4577/
```

## RUN TESTS
1. Install Python on your machine.
2. Move to the selenium_tests directory.
   ```
   cd selenium_tests
   ```
4. Install chromedriver, virtual environment and sellenium
   ```
   pip install selenium
   python3 -m venv venv
   venv\Scripts\activate
   ```
5. Run tests.
   ```
   python main.py
   ```
   

## AUTHORS

- Szymon Lider
- Sebastian Kutny
- Karina Lu
- Maxim Besarab
- Tomasz Lewandowski
