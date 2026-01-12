from sqlalchemy import create_engine #для создания соединений с БД
from sqlalchemy import text #для передачи запроса sql

db_connection_string = 'postgresql://postgres:123@localhost:5432/TestQA'

db = create_engine(db_connection_string) #создаст соединение с БД

def test_create_subject():
    with db.connect() as connection:  # вместо создания и закрытия соединения, типа фикстуры
        transaction = connection.begin()
        req_for_create = text('insert into subject (subject_title) values (:new_subject)')
        connection.execute(req_for_create, {"new_subject": 'Test subject'})      #создание нового предмета

        req_for_assert = text('select subject_title from subject where subject_title = :new_subject')
        result = connection.execute(req_for_assert, {"new_subject": 'Test subject'})

        # все найденные названия, где строки — это словари
        subjects = [row['subject_title'] for row in result.mappings()]

        assert 'Test subject' in subjects, "Ошибка, новый предмет не найден"

        # удаление по названию
        req_for_delete = text('delete from subject where subject_title = :new_subject')
        connection.execute(req_for_delete, {"new_subject": 'Test subject'})

        transaction.commit()


def test_update_subject():
    with db.connect() as connection:
        transaction = connection.begin()

        req_for_create = text('insert into subject (subject_title) values (:new_subject)')
        connection.execute(req_for_create, {"new_subject": 'Test subject'})  # создание нового предмета

        # изменение название на новое
        req_for_update = text('update subject set subject_title = :new_title where subject_title = :old_title')
        connection.execute(req_for_update, {"old_title": 'Test subject', "new_title": 'Test subject updated'})

        req_for_assert = text('select subject_title from subject where subject_title = :new_subject')
        result = connection.execute(req_for_assert, {"new_subject": 'Test subject updated'})

        # все найденные названия, где строки — это словари
        subjects_updated = [row['subject_title'] for row in result.mappings()]

        assert 'Test subject updated' in subjects_updated, "Ошибка, название не найдено"

        # удаление по названию
        req_for_delete = text('delete from subject where subject_title = :new_subject')
        connection.execute(req_for_delete, {"new_subject": 'Test subject updated'})

        transaction.commit()


def test_delete_tags():
    with db.connect() as connection:
        transaction = connection.begin()

        # post_id и tag - оба обязательные, не должны повторяться, ключи
        # максимальный post_id
        req_max_id = connection.execute(text('select max(post_id) from tags'))
        max_post_id = req_max_id.scalar() # получит первую строку
        if max_post_id is None:
            max_post_id = 0
        new_post_id = max_post_id + 1 # value 1

        new_tag = 'test tag' # value 2

        # тег не повторяется
        req_uniq_tag = connection.execute(text('select 1 from tags where tag = :tag'), {"tag": new_tag}).first()
       #возвращает строку с 1 для каждой найденной записи, если есть хотя бы одна, результат будет содержать хотя бы одну строку

        if req_uniq_tag is None:
        # новaя запись
            req_for_create = text('insert into tags (post_id, tag) VALUES (:post_id, :tag)')
            connection.execute(req_for_create, {"post_id": new_post_id, "tag": new_tag})

        else:
            print("Ошибка, повторяющееся значение уникального поля")

        req_for_delete = text('delete from tags where post_id = :new_post_id')
        result_del = connection.execute(req_for_delete, {"new_post_id": new_post_id})

        rows_deleted = result_del.rowcount #кол-во измененных строк

        # Проверка, что удалена одна строка
        assert rows_deleted == 1, "Ошибка, удалено больше одной строки"

        # Проверка, что тег отсутствует в таблице
        req_uniq_tag = connection.execute(text('select 1 from tags where tag = :tag'), {"tag": new_tag}).first()
        assert req_uniq_tag is None, "Ошибка, строка не удалена"

        transaction.commit()





