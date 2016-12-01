from rest_framework.serializers import ModelSerializer

from posts.models import Post

class PostListSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields = [
		    'title',
		    'slug',
		    'content',
		    'publish',
		]

class PostDetailSerializer(ModelSerializer):
	class Meta:
		model = Post
		fields = [
		    'id',
		    'title',
		    'slug',
		    'content',
		    'publish',
		]

"""
from posts.api.serializers import PostDetailSerializer
from posts.models import Post

data = {
	'title': 'yeah buddy',
	'content': 'new content',
	'publish': '2016-2-12',
	'slug': 'yeah-buddy',

}

obj = Post.objects.get(id=2)
new_item = PostDetailSerializer(obj, data=data)
if new_item.is_valid():
	new_item.save()
else:
	print(new_item.errors)

"""