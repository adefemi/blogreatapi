from rest_framework.viewsets import ModelViewSet
from blogreat.utils import (Helper, get_query)
from .models import (TagModel, BlogModel, CommentModel, ImageModel, SpecialblogModel)
from .serializers import (TagSerializer, BlogSerializer, CommentSerializer, ImageSerializer, SpecialblogSerializer)
from django.db.models import (Count, Q)


class TagView(ModelViewSet):
	queryset = TagModel.objects.all()
	serializer_class = TagSerializer


class BlogView(ModelViewSet):
	queryset = BlogModel.objects.all()
	serializer_class = BlogSerializer
	lookup_field = 'slug'

	def get_queryset(self):
		if self.request.method.lower() != 'get':
			return self.queryset

		params = self.request.query_params.dict()
		keyword = params.pop('keyword', None)
		params.pop('page', None)
		results = self.queryset.filter(**params)
		if keyword:
			search_fields = ['tag__name', 'title', 'slug']
			query = get_query(keyword, search_fields)
			results = results.filter(query)

		filter_params = self.request.query_params.dict()

		# Remove search key from considerable fields
		if 'keyword' in filter_params:
			del filter_params['keyword']

		try:
			results = self.queryset.filter(**filter_params)

		except Exception as e:
			raise Exception(e)

		return results


class CommentView(ModelViewSet):
	queryset = CommentModel.objects.all()
	serializer_class = CommentSerializer

	def get_queryset(self):

		if self.request.method.lower() != 'get':
			return self.queryset

		filter_params = self.request.query_params.dict()

		try:
			results = self.queryset.filter(**filter_params)

		except Exception as e:
			raise Exception(e)

		return results


class ImageView(ModelViewSet):
	queryset = ImageModel.objects.all()
	serializer_class = ImageSerializer


class SpecialblogView(ModelViewSet):
	queryset = SpecialblogModel.objects.all()
	serializer_class = SpecialblogSerializer
	http_method_names = ['get', 'post']


class TopBlogView(ModelViewSet):
	queryset = BlogModel.objects.all()
	serializer_class = BlogSerializer
	lookup_field = 'slug'
	http_method_names = ['get']

	def get_queryset(self):

		if self.request.method.lower() != 'get':
			return self.queryset

		filter_params = self.request.query_params.dict()

		try:
			results = self.queryset.filter(**filter_params)

		except Exception as e:
			raise Exception(e)

		results = results.annotate(comments_count=Count('comments')).order_by('-comments_count')[:5]

		return results
