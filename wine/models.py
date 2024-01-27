from django.db import models


class MenuModel(models.Model):
    menu_name = models.CharField(max_length=30)
    price = models.IntegerField(default=12)
    text = models.TextField()
    image = models.ImageField()
    
    def __str__(self) -> str:
        return self.menu_name


# from django.db import models


# class MenuModel(models.Model):
#     menu_name = models.CharField(max_length=30)
#     image = models.ImageField()
#     price = models.IntegerField(default=12)
 
    
#     def __str__(self) -> str:
#         return self.menu_name


# class MenuText(models.Model):
#     menu = models.ForeignKey(MenuModel, null=True, on_delete=models.CASCADE)
#     text = models.TextField()
   

#     def __str__(self) -> str:
#         return self.menu.menu_name