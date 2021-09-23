from scraping.parsers import *
import os, sys
from scraping.models import City, Vacancy, Language, Error

proj = os.path.dirname(os.path.abspath('manage.py'))
sys.path.append(proj)
os.environ["DJANGO_SETTINGS_MODULE"] = "scraping_service.settings"


import django
django.setup()
from django.db import DatabaseError
parsers = (
            (work, 'https://www.work.ua/ru/jobs-kyiv-python/'),
            (dou, 'https://jobs.dou.ua/vacancies/?city=%D0%9A%D0%B8%D1%97%D0%B2&category=Python'),
            (rabota, 'https://rabota.ua/zapros/python/%D0%BA%D0%B8%D0%B5%D0%B2'),
            (djinni, 'https://djinni.co/jobs/keyword-python/kyiv')
           )

jobs, errors = [], []

for func, url in parsers:
    j, e = func(url)
    jobs += j
    errors += e

for job in jobs:
    v = Vacancy(**job)
    try:
        v.save()
    except DatabaseError:
        pass
if errors:
    er = Error(data=errors).save()



# h = open('work.txt', 'w', encoding='utf-8')
# h.write(str(jobs))
# h.close()