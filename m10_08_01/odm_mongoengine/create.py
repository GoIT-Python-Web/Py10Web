from mongoengine import disconnect

from odm_mongoengine.models import User, TextPost, LinkPost, ImagePost

if __name__ == '__main__':
    ross = User(email='ross@example.com')
    ross.first_name = 'Ross'
    ross.last_name = 'Lawley'
    ross.save()

    john = User(email='john@example.com', first_name='John', last_name='Lawley').save()

    post1 = TextPost(title='Fun with MongoEngine', author=john)
    post1.content = 'Took a look at MongoEngine today, looks pretty cool.'
    post1.tags = ['mongodb', 'mongoengine']
    post1.save()

    post2 = LinkPost(title='MongoEngine Documentation', author=ross)
    post2.link_url = 'http://docs.mongoengine.com/'
    post2.tags = ['mongoengine']
    post2.save()

    tolya = User(email='python_guru@example.com', first_name='Anatoliy', last_name='Safonov').save()
    post3 = ImagePost(title='MongoDB picture', author=tolya)
    post3.image_path = 'https://res.cloudinary.com/hevo/image/upload/v1626694700/hevo-blog/MongoDB-sm-logo-500x400-1-1.gif'
    post3.tags = ['Senior', 'Pomidor']
    post3.save()

    disconnect()
