from django.shortcuts import render
from django.http import JsonResponse
from django.http import HttpResponse
import sqlite3
from .models import Projects
from .models import User


try:
    db = sqlite3.connect('db.sqlite3')
    cursor = db.cursor()
    print("Подключен к SQLite")

    # sqlite_insert_query = """INSERT INTO sqlitedb_developers
    #                       (id, name, email, joining_date, salary)
    #                       VALUES
    #                       (1, 'Oleg', 'oleg04@gmail.com', '2020-11-29', 8100);"""
    # count = cursor.execute(sqlite_insert_query)
    # db.commit()
    # print("Запись успешно вставлена ​​в таблицу sqlitedb_developers ", cursor.rowcount)
    cursor.close()

except sqlite3.Error as error:
    print("Ошибка при работе с SQLite", error)

def Projects_Data(request):
    
    data = Projects.project_desc
    return JsonResponse(data, safe=False)



def User_Data(request):
    get_id = request.GET.get('user_id')
    if not get_id:
        return print("не передано Id")
    select_query = """SELECT first_name FROM app_user WHERE user_id = ?"""
    insert_query = """INSERT INTO app_user
                          (user_id, first_name)
                          VALUES
                          (?, ?);"""
    cursor.execute(select_query, (get_id,))
    result = cursor.fetchone()
    if not result:
        cursor.execute(insert_query, (get_id, "заглушка"))
        db.commit()
    cursor.execute(select_query,(get_id,))
    result = cursor.fetchone()
    db.close()
    return JsonResponse(result, safe= False)

def Hello(request):
    return HttpResponse('Hello')