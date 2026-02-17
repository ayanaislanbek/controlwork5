# 1. Запуск проекта
1.1.```bash git clone https://github.com/ayanaislanbek/controlwork5.git ```

2. Настройка окружения
2.1 Обновляем облако:
```bash sudo apt update ```

2.2 Создание виртуальной вселенной:
 ```bash python3 -m venv venv ```

2.3 Активация виртуальной вселенной:
 ```bash source venv/bin/activate ```

2.4 Установка библиоток:
 ```bash pip install -r requirements.txt ```

3. Путь к интерпретатору,
 если вс код не видит Django
3.1 нажимаем на shift+ctrl+p
3.2 Введите Python: Select Interpreter.
3.3 Введите путь к интерпретатору:
home --> project --> venv --> bin --> python

4. Настройка базы данных
4.1 Миграции
  ```bash python manage.py migrate ```

4.2 создаем супер пользователя чтобы подключить базу данных
```bash python manage.py createsuperuser ``` 


5. Запуск
```bash python manage.py runserver ```

После запуска проект будет доступен по адресу:
http://127.0.0.1:8000/

Чтобы получить документ в нашу ссылку добавляем /swagger/
можно ещё: /swagger/redoc/
/swagger.json/ 



