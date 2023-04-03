from mongoengine import disconnect

from models import Post, User

if __name__ == '__main__':
    post = Post.objects(title="Fun with MongoEngine")
    post.delete()

    disconnect()
