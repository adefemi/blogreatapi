from rest_framework import serializers
from .models import (TagModel, BlogModel, CommentModel, ImageModel, SpecialblogModel)


class TagSerializer(serializers.ModelSerializer):
	class Meta:
		model = TagModel
		fields = '__all__'


class BlogSerializer(serializers.ModelSerializer):
	tag = TagSerializer(read_only=True)
	tag_id = serializers.IntegerField(write_only=True)
	class Meta:
		model = BlogModel
		fields = '__all__'


class CommentSerializer(serializers.ModelSerializer):
	blog = BlogSerializer(read_only=True)
	blog_id = serializers.IntegerField(write_only=True)
	class Meta:
		model = CommentModel
		fields = '__all__'


class ImageSerializer(serializers.ModelSerializer):
	class Meta:
		model = ImageModel
		fields = '__all__'


class SpecialblogSerializer(serializers.ModelSerializer):
	blog = BlogSerializer(read_only=True)
	blog_id = serializers.IntegerField(write_only=True)
	class Meta:
		model = SpecialblogModel
		fields = '__all__'
