from django.db import models
from django.urls import reverse
from django.contrib.auth.models import User
from ckeditor_uploader.fields import RichTextUploadingField
from read_statistics.models import ReadNumExpandMethod

# 博客分类模型
class BlogType(models.Model):
	type_name = models.CharField(max_length=15)

	def __str__(self):
		return self.type_name

# 博客模型
class Blog(models.Model, ReadNumExpandMethod):
	title = models.CharField(max_length=50)
	blog_type = models.ForeignKey(BlogType, on_delete=models.CASCADE)
	content = RichTextUploadingField()
	author = models.ForeignKey(User, on_delete=models.CASCADE)
	
	created_time = models.DateTimeField(auto_now_add=True)
	last_update_time = models.DateTimeField(auto_now_add=True)
	
	def get_url(self):
		return reverse('blog_detail', kwargs={'blog_pk': self.pk})

	def __str__(self):
		return "<Blog: %s>" % self.title

	class Meta:
		ordering = ['-created_time']