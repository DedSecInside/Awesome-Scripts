from django.db import models

# Create your models here.

class post(models.Model):
    article_id = models.IntegerField(primary_key=True)
    article_name = models.CharField(max_length=200, null=False)
    date = models.DateTimeField()
    article_category = models.CharField(max_length=400)
    category_id = models.IntegerField()
    article_content = models.TextField(null=False)
    image = models.ImageField()
    


    def __repr__(self):
        return self.article_name


class category(models.Model):

    category_id = models.IntegerField(null=False, primary_key=True)
    category_name = models.CharField(max_length=400, null=False)
    category_type = models.CharField(max_length=400, null=False)
    type_id = models.IntegerField(null=False)


    def __repr__(self):
        return self.category_name