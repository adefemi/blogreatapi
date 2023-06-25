from django.contrib import admin
from .models import (TagModel, BlogModel, CommentModel, ImageModel, SpecialblogModel)


admin.site.register(
	(TagModel, BlogModel, CommentModel, ImageModel, SpecialblogModel)
)
