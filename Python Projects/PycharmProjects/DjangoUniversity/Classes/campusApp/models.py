from django.db import models


# Create your models here.
class UniversityCampus(models.Model): # Creates class with models imported
    Campus_Name = models.CharField(max_length=55, default="", blank=True, null=False) # Class attributes with specifications towards user input
    state = models.CharField(max_length=2, default="", blank=True, null=False)
    campusID = models.IntegerField(default="", blank=True, null=False)

    object = models.Manager()  # Creates model manager

    def __str__(self):
        return self.Campus_Name  # Returns string representation of object

    # Removes added 's' that Django adds to the model name in the brower display
    class Meta:
        verbose_name_plural = "University Campus"

