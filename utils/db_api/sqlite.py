import datetime
import logging
import random
import sqlite3
import time

# Путь к БД
path_to_db = "data/botBD.sqlite"


def logger(statement):
    logging.basicConfig(
        level=logging.INFO,
        filename="logs.log",
        format=f"[Executing] [%(asctime)s] | [%(filename)s LINE:%(lineno)d] | {statement}",
        datefmt="%d-%b-%y %H:%M:%S"
    )
    logging.info(statement)


def handle_silently(function):
    def wrapped(*args, **kwargs):
        result = None
        try:
            result = function(*args, **kwargs)
        except Exception as e:
            logger("{}({}, {}) failed with exception {}".format(
                function.__name__, repr(args[1]), repr(kwargs), repr(e)))
        return result

    return wrapped


####################################################################################################
###################################### ФОРМАТИРОВАНИЕ ЗАПРОСА ######################################
# Форматирование запроса с аргументами
def update_format_with_args(sql, parameters: dict):
    values = ", ".join([
        f"{item} = ?" for item in parameters
    ])
    sql = sql.replace("XXX", values)
    return sql, tuple(parameters.values())


# Форматирование запроса без аргументов
def get_format_args(sql, parameters: dict):
    sql += " AND ".join([
        f"{item} = ?" for item in parameters
    ])
    return sql, tuple(parameters.values())


####################################################################################################
########################################### ЗАПРОСЫ К БД ###########################################
# Добавление пользователя
def add_userx(user_id, list_of_formulas_id):
    with sqlite3.connect(path_to_db) as db:
        db.execute("INSERT INTO storage_users "
                   "(user_id, list_of_formulas_id) "
                   "VALUES (?, ?)",
                   [user_id, list_of_formulas_id])
        db.commit()


# Изменение пользователя
def update_userx(user_id, **kwargs):
    with sqlite3.connect(path_to_db) as db:
        sql = f"UPDATE storage_users SET XXX WHERE user_id = {user_id}"
        sql, parameters = update_format_with_args(sql, kwargs)
        db.execute(sql, parameters)
        db.commit()


# Удаление пользователя
def delete_userx(**kwargs):
    with sqlite3.connect(path_to_db) as db:
        sql = "DELETE FROM storage_users WHERE "
        sql, parameters = get_format_args(sql, kwargs)
        db.execute(sql, parameters)
        db.commit()


# Получение пользователя
def get_userx(**kwargs):
    with sqlite3.connect(path_to_db) as db:
        sql = "SELECT * FROM storage_users WHERE "
        sql, parameters = get_format_args(sql, kwargs)
        get_response = db.execute(sql, parameters)
        get_response = get_response.fetchone()
    return get_response


# Получение пользователей
def get_usersx(**kwargs):
    with sqlite3.connect(path_to_db) as db:
        sql = "SELECT * FROM storage_users WHERE "
        sql, parameters = get_format_args(sql, kwargs)
        get_response = db.execute(sql, parameters)
        get_response = get_response.fetchall()
    return get_response


# Получение всех пользователей
def get_all_usersx():
    with sqlite3.connect(path_to_db) as db:
        get_response = db.execute("SELECT * FROM storage_users")
        get_response = get_response.fetchall()
    return get_response


# Добавление категории в БД
def add_categoryx(category_id, category_name):
    with sqlite3.connect(path_to_db) as db:
        db.execute("INSERT INTO storage_category "
                   "(category_id, category_name) "
                   "VALUES (?, ?)",
                   [category_id, category_name])
        db.commit()


# Изменение категории
def update_categoryx(category_id, **kwargs):
    with sqlite3.connect(path_to_db) as db:
        sql = f"UPDATE storage_category SET XXX WHERE category_id = {category_id}"
        sql, parameters = update_format_with_args(sql, kwargs)
        db.execute(sql, parameters)
        db.commit()


# Получение категории
def get_categoryx(what_select, **kwargs):
    with sqlite3.connect(path_to_db) as db:
        sql = f"SELECT {what_select} FROM storage_category WHERE "
        sql, parameters = get_format_args(sql, kwargs)
        get_response = db.execute(sql, parameters)
        get_response = get_response.fetchone()
    return get_response


# Получение категорий
def get_categoriesx(what_select, **kwargs):
    with sqlite3.connect(path_to_db) as db:
        sql = f"SELECT {what_select} FROM storage_category WHERE "
        sql, parameters = get_format_args(sql, kwargs)
        get_response = db.execute(sql, parameters)
        get_response = get_response.fetchall()
    return get_response


# Получение всех категорий
def get_all_categoriesx():
    with sqlite3.connect(path_to_db) as db:
        sql = "SELECT * FROM storage_category"
        get_response = db.execute(sql)
        get_response = get_response.fetchall()
    return get_response


# Очистка категорий
def clear_categoryx():
    with sqlite3.connect(path_to_db) as db:
        sql = "DELETE FROM storage_category"
        db.execute(sql)
        db.commit()


# Удаление категорий
def remove_categoryx(**kwargs):
    with sqlite3.connect(path_to_db) as db:
        sql = "DELETE FROM storage_category WHERE "
        sql, parameters = get_format_args(sql, kwargs)
        db.execute(sql, parameters)
        db.commit()


# Добавление формулы в БД
def add_positionx(position_id, position_name, position_price, category_id):
    with sqlite3.connect(path_to_db) as db:
        db.execute("INSERT INTO storage_position "
                   "(position_id, position_name, position_price, category_id) "
                   "VALUES (?, ?, ?, ?)",
                   [position_id, position_name, position_price, category_id])
        db.commit()


# Изменение формулы
def update_positionx(position_id, **kwargs):
    with sqlite3.connect(path_to_db) as db:
        sql = f"UPDATE storage_position SET XXX WHERE position_id = {position_id}"
        sql, parameters = update_format_with_args(sql, kwargs)
        db.execute(sql, parameters)
        db.commit()


# Получение формулы
def get_positionx(what_select, **kwargs):
    with sqlite3.connect(path_to_db) as db:
        sql = f"SELECT {what_select} FROM storage_position WHERE "
        sql, parameters = get_format_args(sql, kwargs)
        get_response = db.execute(sql, parameters)
        get_response = get_response.fetchone()
    return get_response


# Получение формул
def get_formulasx(what_select, **kwargs):
    with sqlite3.connect(path_to_db) as db:
        sql = f"SELECT {what_select} FROM storage_position WHERE "
        sql, parameters = get_format_args(sql, kwargs)
        get_response = db.execute(sql, parameters)
        get_response = get_response.fetchall()
    return get_response


# Получение всех формул
def get_all_positionsx():
    with sqlite3.connect(path_to_db) as db:
        sql = "SELECT * FROM storage_position"
        get_response = db.execute(sql)
        get_response = get_response.fetchall()
    return get_response


# Удаление формул
def remove_positionx(**kwargs):
    with sqlite3.connect(path_to_db) as db:
        sql = "DELETE FROM storage_position WHERE "
        sql, parameters = get_format_args(sql, kwargs)
        db.execute(sql, parameters)
        db.commit()


# Очистка категорий
def clear_positionx():
    with sqlite3.connect(path_to_db) as db:
        sql = "DELETE FROM storage_position"
        db.execute(sql)
        db.commit()


# Создание всех таблиц для БД
def create_bdx():
    with sqlite3.connect(path_to_db) as db:
        # Создание БД с хранением данных пользователей
        check_sql = db.execute("PRAGMA table_info(storage_users)")
        check_sql = check_sql.fetchall()
        check_create_users = [c for c in check_sql]
        if len(check_create_users) == 3:
            print("DB was found(1/3)")
        else:
            db.execute("CREATE TABLE storage_users("
                       "increment INTEGER PRIMARY KEY AUTOINCREMENT, "
                       "user_id INTEGER, list_of_formulas_id INTEGER)")
            print("DB was not found(1/3) | Creating...")

        # Создание БД с хранением категорий
        check_sql = db.execute("PRAGMA table_info(storage_category)")
        check_sql = check_sql.fetchall()
        check_create_category = [c for c in check_sql]
        if len(check_create_category) == 3:
            print("DB was found(2/3)")
        else:
            db.execute("CREATE TABLE storage_category("
                       "increment INTEGER PRIMARY KEY AUTOINCREMENT,"
                       "category_id INTEGER, category_name TEXT)")
            print("DB was not found(2/3) | Creating...")

        # Создание БД с хранением позиций
        check_sql = db.execute("PRAGMA table_info(storage_position)")
        check_sql = check_sql.fetchall()
        check_create_position = [c for c in check_sql]
        if len(check_create_position) == 5:
            print("DB was found(3/3)")
        else:
            db.execute("CREATE TABLE storage_position("
                       "increment INTEGER PRIMARY KEY AUTOINCREMENT,"
                       "position_id INTEGER, position_name TEXT, "
                       "position_price INTEGER,"
                       "category_id INTEGER)")
            print("DB was not found(3/3) | Creating...")

        db.commit()
