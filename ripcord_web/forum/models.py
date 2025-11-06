from django.db import models

class School (models.Model):

  name = models.CharField(max_length=100)

class User (models.Model):

  name = models.CharField(max_length=25)
  school = models.ForeignKey(School, null=True, on_delete=models.SET_NULL)
  date_joined = models.DateTimeField("date joined")

class Post (models.Model):

  user = models.ForeignKey(User, on_delete=models.CASCADE)
  title = models.CharField(max_length=50)
  text = models.CharField(max_length=1000)
  date = models.DateTimeField("date published")

class Attachment (models.Model):

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

  file_path = models.CharField(max_length=128)

class Comment (models.Model):

  user = models.ForeignKey(User, on_delete=models.CASCADE)
  post = models.ForeignKey(Post, on_delete=models.CASCADE)
  text = models.CharField(500)
  date = models.DateTimeField("date published")

