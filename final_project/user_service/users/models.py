from django.db import models

class User(models.Model):    
    email = models.CharField(max_length=255, unique=True)
    username = models.CharField(max_length=255)
    password = models.CharField(max_length=255)
    
    full_name = models.CharField(max_length=255)
    address = models.CharField(max_length=255)
    sdt = models.CharField(max_length=255)

    def __str__(self):
        return '%s %s %s %s %s %s' % (self.email, self.username, self.password, 
                                      self.full_name, self.address, self.sdt)
