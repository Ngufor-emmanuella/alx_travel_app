from django.core.management.base import BaseCommand
from listings.models import Listing, Booking, Review
from django.contrib.auth.models import User

class Command(BaseCommand):
    help = 'Seed the database with sample listings and bookings data'

    def handle(self, *args, **kwargs):
        # Create sample users
        user1 = User.objects.create(username='user1', password='password')
        user2 = User.objects.create(username='user2', password='password')

        # Create sample listings
        listing1 = Listing.objects.create(title='Cozy Apartment', description='A lovely place', price=100.00, owner=user1)
        listing2 = Listing.objects.create(title='Luxury Villa', description='A spacious villa', price=250.00, owner=user2)

        # Create sample bookings
        Booking.objects.create(listing=listing1, user=user2, date_booked='2025-11-01', num_guests=2)
        Booking.objects.create(listing=listing2, user=user1, date_booked='2025-11-10', num_guests=4)

        # Create sample reviews
        Review.objects.create(listing=listing1, user=user2, rating=5, comment='Great experience!')
        Review.objects.create(listing=listing2, user=user1, rating=4, comment='Very nice villa.')
        
        self.stdout.write(self.style.SUCCESS('Database seeded successfully!'))