import requests

# Задача - создать проект
# шаг 1 - авторизоваться,
# чтобы авторизоваться, нужно знать ИД компании
# шаг 2 - создать проект, обязательный заголовок title


class ProjectApi:

    def __init__(self, base_url):
        self.base_url = base_url
        self.token = ""

    def create_project(self, title):
        token = self.token
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }

        resp = requests.post(self.base_url + '/api-v2/projects', headers = headers, json={'title': title})
        return resp

    def get_project_by_id(self, project_id):
        token = self.token
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }
        awr = requests.get(f'{self.base_url}/api-v2/projects/{project_id}', headers=headers)
        return awr

    def delete_project(self, project_id):
        token = self.token
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }

        response = requests.put(f'{self.base_url}/api-v2/projects/{project_id}', headers=headers)
        return response






