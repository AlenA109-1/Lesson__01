
**<ins>Python, homework #10 Documentation with Allure</ins>**


**1. Как запустить тесты для формирования отчета:**
* Для запуска теста и сохранения результата в папку lesson10-results выполните в терминале команду: 
```
pytest --alluredir lesson10-results
``` 

**2. Как просмотреть сформированный отчет:**
* Для формирования и просмотра отчета локально выполните в терминале команду:
```
allure serve lesson10-results
```
* Для формирования отчета и HTML-версии выполните в терминале команду:
```
allure generate lesson10-results -o lesson10_report
```



[!Внимание: указанные команды применимы для OS Windows/Linux]