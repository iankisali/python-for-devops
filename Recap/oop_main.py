from oop_user import User
from oop_post import Post

#creating object from class
user_1 = User("neek@email", "neek", "pwd", "devops")
user_1.print_user()

user_1.change_job("cloud eng")
user_1.print_user()

user_2 = User("vee@gmail", "vee", "pws3", "it")
user_2.print_user()

user_2.change_job("Nurse")
user_2.print_user()

new_post = Post("Secret mission", user_1.name)
new_post.post_info()