from django.db import models

# Create your models here.
class Bookingtable(models.Model):
  
   Name = models.CharField(max_length=255)    
   No_of_guests = models.IntegerField()
   Bookingdate = models.DateField(db_index=True)

   def __str__(self):
      return self.Name


# Add code to create Menu model
class Menu(models.Model):
   
    Title = models.CharField(max_length = 255)
    Price = models.DecimalField(max_digits= 10, decimal_places= 2)
    Inventory = models.IntegerField()
    
    def __str__(self) -> str:
        return f'{self.title} : {str(self.price)}'