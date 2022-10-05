from django.db import models

#EACH POST IS ASSOCIATED WITH A USER SO WE IMPORT THE USER MODEL,
from django.contrib.auth.models import User

#FOR TIME STAMP
from django.utils import timezone

# Create your models here.
#creating a blog 


#EACH POST IN A CATEGORY

class Category(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name





class Post(models.Model):

    #creating a custom manager 
    # to modify objects.all()
    # now the manager objects.all only return the all published Post

    class PostObjects(models.Manager):

        def get_queryset(self):
            return super().get_queryset().filter(status='published')# works likedefault filter for .all() there for we don't have to filter in view
    
    # creating choices field ((value,label))
    options = (('published','Published'),
                ('draft','Draft'))
    category = models.ForeignKey(Category,on_delete=models.PROTECT,default=1)
    #models.PROTECT protects the post when deleting category ie if there is post associated with a category then 
    #if we try to delete that category cannot delete the category
    title = models.CharField(max_length=100)
    excerpt = models.TextField(null = True)
    content = models.TextField()
    #SlugField
    slug = models.SlugField(max_length=300, unique_for_date='published')#unique_for_date='published' django will not allow entry of 2 records with same pub_date and slug
    published = models.DateTimeField(default=timezone.now)
                                                                       
    author = models.ForeignKey(User,on_delete=models.CASCADE,related_name='blog_posts')

    status = models.CharField(max_length = 10,choices=options,default='published')

    objects = models.Manager() #default manager

    postobjects = PostObjects() #custom manager that returns only published 


    class Meta:
        # return objects in the order recently published
        ordering = ('-published',)
    def __str__(self):
        return self.title