from django.db import models

# Create your models here.


class ViewManager(models.Model):

    CHOICES = ( 
    ("Welcome_Screen", "Welcome_Screen"),
    ("About_Us", "About_Us"),
    ("Feedback", "Feedback")
) 
    banner_type = models.CharField(max_length=255, choices=CHOICES,db_column="banner_type", default="not_available")
    banner_title = models.CharField(max_length=555,db_column="banner_title", default="not_available")
    title_text = models.TextField(max_length=1025,db_column="title_text", null=False)
    feedback_by = models.CharField(max_length=255, db_column="feedback_by", default="not_available")
    added_on = models.DateTimeField(auto_now=True)
    added_by = models.CharField(max_length=255, db_column="added_by", default="GP")

    class Meta:
        db_table = "ViewManager"
        # db_table_comment = "View and manage the site contents"

    def __str__(self):
        return self.banner_type.replace("_"," ")
    
class Products_List(models.Model):
    CHOICES = ( 
    ("Capsule", "Capsule"),
    ("Injection", "Injection"),
    ("Syrup", "Syrup")
    )   
    
    product_type = models.CharField(max_length=255, choices=CHOICES,db_column="product_type", default="Capsule")
    product_name = models.CharField(max_length=255, db_column="product_name", null=False)
    product_description = models.TextField(max_length=1025,db_column="product_description", default="Not Defined")
    price = models.DecimalField(max_digits=9, decimal_places=2, default=0.00)
    added_on = models.DateTimeField(auto_now=True)
    added_by = models.CharField(max_length=255, db_column="added_by", default="GP")
    updated_by = models.CharField(max_length=255, db_column="updated_by", default="")

    class Meta:
        db_table = "Products_List"
        # db_table_comment = "Manage Product List"

    def __str__(self):
        return f"{self.product_type} -- {self.product_name}"
    

class UnauthorizedAccess_Tracker(models.Model):

    track_log = models.TextField(max_length=9999,db_column="track_log", null=True)
    ip_logged = models.TextField(max_length=1025,db_column="title_text", null=True)
    tracked_on = models.DateTimeField(auto_now=True)
    
    class Meta:
        db_table = "UnauthorizedAccess_Tracker"
        # db_table_comment = "Track and View Unauthorized Access"

    def __str__(self):
        return f"{self.tracked_on}" 