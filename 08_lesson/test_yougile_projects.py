from assist_methods import ProjectApi

# Задача - создать проект  [POST] /api-v2/projects

base_url = 'https://ru.yougile.com'
api = ProjectApi(base_url)
login = ''
password = ''

def test_positive_create_project():
    title = 'Project8'
    resp = api.create_project(login, password, title)
    assert resp.status_code == 201
    print(resp.json())
    project_id = str(resp.json()['id'])
    return project_id

def test_negative_create_project():
    title = 888 # must be string

    resp = api.create_project(login, password, title)
    assert resp.status_code == 401  #не описан код
    print(resp.json())

# Задача - получить данные по ИД  [GET] /api-v2/projects/{id}

def test_positive_get_project():
    project_id = test_positive_create_project()
    awr = api.get_project_by_id(project_id)
    assert awr.status_code == 200
    print(awr.json())


def test_negative_get_project():
    api.get_token(login, password)

    project_id = '785zlak358ю' #несуществующий
    awr = api.get_project_by_id(project_id)
    assert awr.status_code == 404, awr.json()                  # в документации 404, возвращается 401


# Задача - изменить/del проект   [PUT] /api-v2/projects/{id}

def test_positive_delete_project():
    project_id = test_positive_create_project()
    response = api.delete_project(project_id)
    assert response.status_code == 200
    assert response.json()['deleted'] == True

def test_negative_delete_project():
    api.get_token(login, password)

    project_id = None
    response = api.delete_project(project_id)
    assert response.status_code == 404, response.json() # в документации 404, возвращается 401