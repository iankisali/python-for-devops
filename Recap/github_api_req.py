import requests

response = requests.get("https://gitlab.com/api/v4/users/iankisali/projects")

print(response.json()[0])

projects = response.json()

for project in projects:
    print(f"Project name: {project['name']} \nProject url: {project['web_url']} \n")