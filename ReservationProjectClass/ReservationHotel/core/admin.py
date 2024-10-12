from django.contrib import admin
from .models import *
from django.contrib.admin import ModelAdmin as BaseModelAdmin
from django.utils.translation import gettext_lazy as _
# with this ModelAdmin we can costomize view of model 

class UserModelAdmin(BaseModelAdmin):
    ordering = ["id"]  # order by id that django set for every user 
    list_display = ["first_name" , "last_name" , "email"]
    fieldsets= (
        (_("Login Information") , {"fields" :("email" , "password")}),
        (_("Personal information") , {"fields": ("first_name" ,"last_name" ,"phone_number" )}),
        (_("permission") , {"fields" :("is_staff" , "is_active" , "is_superuser")}),
        (_("Dates") , {"fields" :("birth_day" , "last_login")}),
    )
    
class RoomModelAdmin(BaseModelAdmin):
    ordering= ["id"]
    list_display =["hotel" , "room_number" ,"type", "is_available"]
    fieldsets = (
        (_("Room information"), {
            "fields": (
                "hotel" ,"room_number","type","price" ,"is_available"
            ),
        }),
    )
    
    
    
class ReservationModelAdmin(BaseModelAdmin):
    ordering = ["id"]
    list_display  = ["user" , "room" ,"status" , "total_price"]
    fieldsets = (
        (_("Room Information"), {
            "fields": (
                "room","status","total_price"
            ),
        }),
        (_("Person Information"), {
            "fields": (
                "user",
            ),
        }),
    )
    

class HotelModelAdmin(BaseModelAdmin):
    ordering = ["id"]
    list_display = ["name_hotel" , "address"]
    fieldsets = (
    (_("Hotel Information"), {"fields": ("name_hotel", "address")}),
    (_("Description"), {"fields": ("description", "total_room", "available_room")}),
    (_("Date"), {"fields": ("create_at",)}),
    )

    
    pass
    
 
admin.site.register(User , UserModelAdmin)
admin.site.register(Hotel ,HotelModelAdmin)
admin.site.register(Reservation, ReservationModelAdmin)
admin.site.register(Room ,RoomModelAdmin)




# Register your models here.
