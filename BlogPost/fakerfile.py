from faker import Faker
from myapp.models import Post
from django.contrib.auth.models import User
import numpy as np

fake = Faker()
Faker.seed(313)

possible_tags = ['tag1', 'tag2', 'tag3', 'tag4', 'tag5', 'tag6', 'tag7', 'tag8', 'tag9', 'tag10']
possible_status = ['published', 'draft']

author = User.objects.get(username='harsh')

for i in range(100):
    title = 'Post Title '+str(i)
    tags = np.random.choice(possible_tags, 3)
    status = np.random.choice(possible_status)
    new_post = Post(title=title, author=author, body=fake.paragraph(nb_sentences=20), status=status)
    new_post.save()
    new_post.tags.add(*tags)