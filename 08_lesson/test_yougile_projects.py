from assist_methods import ProjectApi

# Задача - создать проект  [POST] /api-v2/projects

base_url = 'https://ru.yougile.com'
api = ProjectApi(base_url)
project_id = ''

def test_positive_create_project():
    global project_id
    new_title = 'Project8'
    resp_cr = api.create_project(new_title)
    assert resp_cr.status_code == 201
    project_id = resp_cr.json()['id']
    return project_id

def test_negative_create_project():
    new_title = 888 # must be string

    resp = api.create_project(new_title)
    assert resp.status_code == 400  #не описан код
    print(resp.json())

# Задача - получить данные по ИД  [GET] /api-v2/projects/{id}

def test_positive_get_project():
    global project_id
    awr = api.get_project_by_id(project_id)
    assert awr.status_code == 200
    print(awr.json())


def test_negative_get_project():
    project_id = '785zlak358ю'              #несуществующий
    awr = api.get_project_by_id(project_id)
    assert awr.status_code == 404, awr.json()


# Задача - изменить/del проект   [PUT] /api-v2/projects/{id}

def test_positive_delete_project():
    global project_id
    response = api.delete_project(project_id)
    assert response.status_code == 200
    assert response.json()['id'] == project_id

def test_negative_delete_project():
    project_id = None
    response = api.delete_project(project_id)
    assert response.status_code == 404, response.json()