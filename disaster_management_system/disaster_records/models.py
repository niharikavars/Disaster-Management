from django.db import models

# Create your models here.
class DisasterRecords(models.Model):
    Name = models.CharField(max_length=200,unique=True)
    Date = models.DateField()
    State = models.CharField(max_length=200)
    Type = models.CharField(max_length=200)
    District = models.CharField(max_length=200)
    Month = models.CharField(max_length=100)
    Year = models.IntegerField()
    Source = models.CharField(max_length=200)



class EmergencyContactInfo(models.Model):
    District = models.ForeignKey(DisasterRecords,default=1,on_delete=models.SET_DEFAULT)
    Service = models.CharField(max_length=300,blank=True)
    STD_Code = models.CharField(max_length=200)
    Contact_no = models.CharField(max_length=200)
    Web_page_address = models.CharField(max_length=300)

class Relief_fund(models.Model):
    State = models.ForeignKey(DisasterRecords,default=1,on_delete=models.SET_DEFAULT)
    Name = models.CharField(max_length=200,null=True)
    OfficialSite_link = models.CharField(max_length=300,null=True)

class AffectedData(models.Model):
    District = models.ForeignKey(DisasterRecords,on_delete=models.CASCADE)
    Year = models.IntegerField()
    No_of_deaths = models.IntegerField()
    Fields_crops_damage = models.CharField(max_length=250)
    Property_damage = models.CharField(max_length=250)
    People_affected = models.CharField(max_length=250)
    Families_affected = models.CharField(max_length=250)
    Animals_affected = models.CharField(max_length=250)
