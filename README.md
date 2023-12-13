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

## RUN TESTS

## AUTHORS

- Szymon Lider
- Sebastian Kutny
- Karina Lu
- Maxim Besarab
- Tomasz Lewandowski