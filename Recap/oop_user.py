class User:
    # User class 

    def __init__(self, email, name, password, job_title):
        self.email = email
        self.name = name
        self.password = password
        self.job_title = job_title

    def change_password(self, new_password):
        # methods to change user password

        self.password = new_password
    def change_job(self, new_job_title):
        # methods to change job title

        self.job_title = new_job_title

    def print_user(self):
        #method to print user info
        print(f"User {self.name} currently works as {self.job_title}, contact them at {self.email}")

