from django.db import models

# Create your models here.
class Author(models.Model): 
    name = models.CharField(
        verbose_name='Author name',
        max_length=50) 
    book_name = models.CharField(
        verbose_name='Book name',
        max_length=50,
        null=False)

    def __str__(self):
        return f'{self.name} {self.book_name}'    
          
class Genre(models.Model): 
    author = models.ForeignKey(
        'Author',
        verbose_name='Author',
        on_delete=models.PROTECT,
        related_name="genres",
        )
    # id = models.CharField(
    #     verbose_name='pk',
    #     primary_key=True,
    #     max_length=50
    # )    
    style = models.CharField(
        verbose_name='style book',
        max_length=50,
        null=True)
    description = models.TextField(
        verbose_name='book description',
        null=True,
        max_length=100,
        blank=True)      


    
    def __str__(self):
        return f'{self.author.name} {self.author.book_name} {self.style} {self.description}'





        #return f' {self.style} {self.description}'    
        