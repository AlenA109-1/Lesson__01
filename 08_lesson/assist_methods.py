import requests

# Задача - создать проект
# шаг 1 - авторизоваться,
# чтобы авторизоваться, нужно знать ИД компании
# шаг 2 - создать проект, обязательный заголовок title


class ProjectApi:

    def __init__(self, base_url):
        self.base_url = base_url
        self.token = None


    def get_token(self, login, password, company_id = "faa40989-411b-4bf1-845c-0056fe04c62e"):
        payload = {"login": login, "password": password, "companyId": company_id}
        headers = {"Content-Type": "application/json"}

        response = requests.post(self.base_url + '/api-v2/auth/keys', json=payload, headers=headers)
        self.token = response.json()["key"]
        return self.token

    def create_project(self, login, password, title):
        token = self.get_token(login, password)
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }
        resp = requests.post(self.base_url + '/api-v2/projects', headers = headers, json={'project_name': title})
        return resp

    def get_project_by_id(self, login, password, project_id):
        token = self.get_token(login, password)
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }
        awr = requests.get(f'{self.base_url}/api-v2/projects/{project_id}', headers=headers)
        return awr

    def delete_project(self, login, password, project_id):
        token = self.get_token(login, password)
        headers = {
            "Content-Type": "application/json",
            "Authorization": f"Bearer {token}"
        }

        response = requests.put(f'{self.base_url}/api-v2/projects/{project_id}', headers=headers)
        return response






