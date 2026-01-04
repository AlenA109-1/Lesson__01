from assist_methods import ProjectApi

# Задача - создать проект  [POST] /api-v2/projects

base_url = 'https://ru.yougile.com'
api = ProjectApi(base_url)


def test_positive_create_project():
    new_title = 'Project8'
    resp_cr = api.create_project(new_title)
    assert resp_cr.status_code == 201, resp_cr.status_code
    project_id = resp_cr.json()['id']
    api.change_project(project_id, deleted = True, title = new_title)

def test_negative_create_project():
    new_title = 888 # must be string

    resp = api.create_project(new_title)
    assert resp.status_code == 400, resp.status_code
    assert resp.json()['message'][0] == 'title must be a string', resp.json()


# Задача - получить данные по ИД  [GET] /api-v2/projects/{id}

def test_positive_get_project():
    title = 'Project_GET'
    resp = api.create_project(title)
    project_id = resp.json()['id']
    awr = api.get_project_by_id(project_id)
    assert awr.status_code == 200, awr.status_code
    api.change_project(project_id, deleted = True, title = title)


def test_negative_get_project():
    title = 'Project_GET'
    resp = api.create_project(title)
    project_id = resp.json()['id']

    project_id_test = '785zlak358ю'              #несуществующий ID
    awr = api.get_project_by_id(project_id_test)
    assert awr.status_code == 404, awr.status_code
    assert awr.json()['message'] == 'Проект не найден', awr.json()

    api.change_project(project_id, deleted = True, title = title)


# Задача - изменить проект   [PUT] /api-v2/projects/{id}

def test_positive_delete_project():
    title = 'Project_PUT'
    resp = api.create_project(title)
    project_id = resp.json()['id']

    new_title = 'Changed project'
    response = api.change_project(project_id, title = new_title)
    assert response.status_code == 200, response.status_code
    assert response.json()['id'] == project_id, response.json()['id']

    api.change_project(project_id, deleted=True, title = new_title)

def test_negative_change_project():
    title = 'Project_PUT'
    resp = api.create_project(title)
    project_id = resp.json()['id']

    new_title = ''
    response = api.change_project(project_id, deleted = False, title = new_title)
    assert response.status_code == 400, response.status_code                                       #в документации 404

    messages = ['title must be a string', 'title should not be empty']
    assert response.json()['message'][0] in messages, response.json()['message'][0]

    api.change_project(project_id, deleted = True, title = title)



