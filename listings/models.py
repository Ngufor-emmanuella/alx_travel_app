from django.db import models

class Listing(models.Model):
    title = models.CharField(max_length=200)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    owner = models.ForeignKey('auth.User', related_name='listings', on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

class Booking(models.Model):
    listing = models.ForeignKey(Listing, related_name='bookings', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', related_name='bookings', on_delete=models.CASCADE)
    date_booked = models.DateField()
    num_guests = models.PositiveIntegerField()

class Review(models.Model):
    listing = models.ForeignKey(Listing, related_name='reviews', on_delete=models.CASCADE)
    user = models.ForeignKey('auth.User', related_name='reviews', on_delete=models.CASCADE)
    rating = models.PositiveIntegerField(choices=[(i, str(i)) for i in range(1, 6)])  # 1 to 5
    comment = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)