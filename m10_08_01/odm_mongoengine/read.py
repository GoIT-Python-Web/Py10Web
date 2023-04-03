from mongoengine import disconnect

from models import Post, User

if __name__ == '__main__':

    posts = Post.objects()
    for post in posts:
        print(post.to_mongo().to_dict())

    users = User.objects()
    for user in users:
        print(user.to_mongo().to_dict())

    disconnect()
