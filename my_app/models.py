from django.db import models

# Create your models here.


class Customer(models.Model):
    title = models.CharField(max_length=5)
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    # null=True or default=True
    email_address = models.EmailField(null=True)    # after you've done your first migragtion and you want to add a new field you also need to add a default value
    description = models.TextField()
    customer_since = models.DateTimeField()



    def __str__(self):
        return f"{self.first_name} {self.last_name}"
