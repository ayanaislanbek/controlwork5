1. Запуск проекта
1.1. git clone https://github.com/ayanaislanbek/controlwork5.git

2. Настройка окружения
2.1 Обновляем облако:
sudo apt update 

2.2 Создание виртуальной вселенной:
python3 -m venv venv

2.3 Активация виртуальной вселенной:
source venv/bin/activate

2.4 Установка библиоток:
pip install -r requirements.txt

3. Путь к интерпретатору,
 если вс код не видит Django
3.1 нажимаем на shift+ctrl+p
3.2 Введите Python: Select Interpreter.
3.3 Введите путь к интерпретатору:
home --> project --> venv --> bin --> python

4. Настройка базы данных
4.1 python manage.py migrate

4.2 создаем супер пользователя чтобы подключить базу данных
python manage.py createsuperuser 


5. Запуск
python manage.py runserver

После запуска проект будет доступен по адресу:
http://127.0.0.1:8000/

Чтобы получить документ в нашу ссылку добавляем /swagger/
можно ещё: /swagger/redoc/
/swagger.json/ 



