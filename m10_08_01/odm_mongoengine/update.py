from mongoengine import disconnect

from models import Post, User

if __name__ == '__main__':
    user = User.objects(pk="642b1fdea3aa6346016ffcd0")
    post = Post.objects(title='MongoEngine Documentation')

    post.update(link_url="https://docs.mongoengine.org/index.html", author=user[0].id)

    disconnect()
