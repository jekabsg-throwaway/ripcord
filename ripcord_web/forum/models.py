from django.db import models
from django.conf import settings

class School (models.Model):
  def __str__(self): return self.name

  name = models.CharField(max_length=100)

class User (models.Model):
  def __str__(self): return self.name

  # link to Django user to inherit auth features
  auth_user = models.OneToOneField(
    settings.AUTH_USER_MODEL,
    null=True,
    blank=True,
    on_delete=models.SET_NULL,
    related_name='forum_user'
  )

  name = models.CharField(max_length=25)
  school = models.ForeignKey(School, null=True, on_delete=models.SET_NULL)
  date_joined = models.DateTimeField("date joined")

class Post (models.Model):
  def __str__(self): return self.title

  user = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=50)
  text = models.CharField(max_length=1000)
  date = models.DateTimeField("date published")

class Attachment (models.Model):
  def __str__(self): return self.original_file_name

  post = models.ForeignKey(Post, on_delete=models.CASCADE)

  class FileType(models.TextChoices):
    IMAGE_JPG = "JPG",
    IMAGE_PNG = "PNG",
    IMAGE_OTHER = "IMG",
    VIDEO_MP4 = "MP4",
    VIDEO_MKV = "MKV",
    VIDEO_OTHER = "VIDEO",
    DOCUMENT_PDF = "PDF",
    DOCUMENT_DOCX = "DOCX",
    DOCUMENT_ODT = "ODT",
    OTHER = "OTHER"
  file_type = models.CharField(
    max_length = 5,
    choices = FileType,
    default = FileType.OTHER
  )

  original_file_name = models.CharField(max_length=128)
  file_path = models.CharField(max_length=128)

class Comment (models.Model):
  def __str__(self): return self.text

  user = models.ForeignKey(User, on_delete=models.CASCADE)
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  text = models.CharField("comment text", max_length=500)
  date = models.DateTimeField("date published")

