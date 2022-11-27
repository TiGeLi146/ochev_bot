Команда "Заказ в пути"
Проект бот для поиска формул "Формула очевидности"
Роли участников: 
  Коротков Роман - заполнение таблиц с формулами, создание презентации, тестирование бота
  Селиверстов Тимофей - написание кода, деплой на сервер, разработка логотипов
  Леушканов Арсений - продюсирование и монтаж видео, разработка логотипов
Идея проекта - бот, выдающий формулы по разным предметам. Идея пришла в ходе опроса учеников и учителей. 
Так мы поняли, что люди нуждаются в данном боте и это актуальная тема. Проблемой является то, что 
для поиска формул надо перешерстить много сайтов, или искать их в огромном конспекте (в чем мы и убедились во время заполнения таблицы). 
Наш бот позволяет тратить в разы меньше времени на поиск нужной формулы.
Получилось реализовать поиск формул через категории: предметы.
В будущем планируем реализовать сортировку по подкатегориям: например, класс и темы; возможность добавления формул в избранное; 
возможность добавления пользователем своих формул; создание пользователями публичных список формул, доступных по паролю или ссылке; работа с диплинками
Бот написан на асинхронной библиотеке aiogram с использованием базы данных SQLite. Выбран хостинг heroku