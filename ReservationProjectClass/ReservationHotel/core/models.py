
#  مدل یک جدول دیتا بیسی هست 
# Create your models here.
from typing import Any
from django.db import models
from django.contrib.auth.models import BaseUserManager ,AbstractBaseUser , PermissionsMixin 

from django.utils.translation import gettext_lazy as _
# 'gettext' and 'gettext_lazy' are used for translating strings dynamically,
# 7 allowing multilingual support in the user's profile or other parts of the application.


# چیز های بیسک دورن کلاس یوزر منیجر را مدیرت میکنه  و ما از طریف این مدل را تغییر میدیم 


# این کلاس که ساختیم از بیس یوزر منیجر ارثبری میکنه 
class UserManager(BaseUserManager):

    # این تابع کریت یوزر که مال بیس یوزر هست را اوور رایت میکنیم 
    def create_user(self , email,password ,**argiument):

        # برسی درست بودن مقادیری ورودی را اینجا چک میکنیم ولیدیشن انجام میدیم  
        if not email:
            raise ValueError("user most have email")
        
            # اگر ایمبل وجود نداشت یک خطار را برمیگرده از تریق تابع ولیو ارور 
        user = self.model(email=self.normalize_email(email) ,**argiument)
        # self.model make one model from defulte model django 

        # این جا میشه بازم هم یک سری ولیدیشن هم انجام داد برای پسورد ها 
        # این تابع ست پسورد یک متد هست که از بیس یوزر ارثبری میکنه و تمام ولیدیشن های مربوط به پسورد را انجام میده
        user.set_password(password)          
        user.save()

        return user
    
    # عموما برای کاربر سوپر یوزر کمترین فیلدها را را تعریف میکنند  
    def create_superuser(self, email,password):
        if not email :
            raise ValueError("you Should input Email")
        user = self.create_user(email ,password)
        user.is_active = True # فعال شود کاربر
        user.is_superuser =True # سوپر یوز باشد 
        user.is_staff = True # همه دسترسی ها بهش داده شود 
        # user.set_password() عموما نمیخوایم سختگیری بشه برای سوپر یوزر پس این جا پسورد را ست نمیکنیم
        user.save()
        return user
    
    
# AbstractBaseUser is user basic model that is not completed but use for make another user model  
#  PermissionsMixin is property that we can handel permisstions  and accessible
class User(AbstractBaseUser, PermissionsMixin):

    email = models.EmailField(max_length=255 ,unique=True)  
    # in AbstractBaseUser are defulet password vaidation method that we dont need validat password
    #we don't need to make first name and last name unique because there are same person in the world
    first_name = models.CharField( max_length=255)
    last_name = models.CharField( max_length=255)
    phone_number = models.CharField( max_length=15)
    is_active= models.BooleanField(default=True)
    is_staff= models.BooleanField(default=False) # make user admin
    bearth_day =models.DateField(null=True)

    # Assign the custom UserManager to handle user-related operations using "objects"
    objects = UserManager()
    USERNAME_FIELD = "email"


# This method returns a string representation of the user object
# showing the user's first and last name when displayed in the admin panel or shell.
    def __str__(self):
        return  f"{self.first_name} {self.last_name}"

    


class Hotel(models.Model):
    name_hotel = models.CharField(max_length=255)
    address =models.CharField( max_length=150)
    description = models.CharField( max_length=500)
    total_room = models.IntegerField()
    available_room = models.IntegerField()
    create_at = models.DateField(null=True, blank=True)

    def __str__(self ) :
        return f"{self.name_hotel} |  {self.address} "
    

class Room(models.Model):
    class RoomType(models.TextChoices):
            # First value is used in the code (e.g., for logic), 
            # second value is stored in the database, 
            # and third value (optional) is displayed to the user and use from gettext_lazy.
            SINGLE = "SI", _("Single")
            DOUBLE = "DU", _("Double")
            SUITE = "SU", _("Suite")


    """
     'hotel' in this class is a ForeignKey, which creates a relationship 
      to another table (Hotel) and acts as a reference to it.
      The 'related_name' allows us to access all related 'rooms' from the 'Hotel' model.
      The 'on_delete' behavior ensures that if a related 'Hotel' is deleted, 
      the associated 'rooms' are also handled accordingly (True means CASCADE by default).
    """
    hotel = models.ForeignKey(Hotel, related_name="rooms", on_delete=models.CASCADE)
    room_number = models.IntegerField()
    type = models.CharField( max_length=2 , choices=RoomType.choices ,default=RoomType.SINGLE)
    price = models.DecimalField(max_digits=10 ,decimal_places=2) 
    is_available = models.BooleanField(default=True)

    def __str__(self):
        return f"accessible :{self.hotel.__str__()} Room Number : {self.room_number} "




class Reservation(models.Model):
    class ReservationStatus(models.TextChoices):
        PANDDING = "PA" ,_("panding")
        CANCELED = "CA" , _("canceled")
        CONFIRMED = "CO", _("confirmed")
    user =models.ForeignKey(User, related_name="user" ,on_delete=models.CASCADE  )
    room = models.ForeignKey(Room ,related_name="room", on_delete=models.CASCADE)
    check_in =models.DateField(  auto_now_add=True)
    check_out = models.DateField(null=False)
    status = models.CharField(max_length=2 , choices=ReservationStatus.choices , default=ReservationStatus.PANDDING )
    total_price =models.DecimalField( max_digits=10, decimal_places=2)

    def __str__(self):
        return f"{self.user.__str__()} user in -> room : {self.room.room_number}  in {self.room.__str__()}"
    

    




