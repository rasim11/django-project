from django.db import models

# Create your models here.
class Search(models.Model):
    search = models.CharField(max_length=100)
    create = models.DateTimeField(auto_now=True)

    def __str__(self):
        return '{}'.format(self.search) #show the value instead of objects amount

    class Meta:
        verbose_name_plural='Searches'  #usually django add's s in the end of each tables name. But if it do the same with table Search it will not be coorect. Due to this
                            # we use Meta.