from django.db import models
from django.db import models


# ---------------------- CUSTOMER ----------------------
class Customer(models.Model):
    full_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.full_name


# ---------------------- STAFF ----------------------
class Staff(models.Model):
    POSITION_CHOICES = [
        ('Manager', 'Manager'),
        ('Receptionist', 'Receptionist'),
        ('Cleaner', 'Cleaner'),
    ]

    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    phone = models.CharField(max_length=15)
    position = models.CharField(max_length=20, choices=POSITION_CHOICES)
    salary = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name} ({self.position})"


# ---------------------- HOTEL ----------------------
class Hotel(models.Model):
    name = models.CharField(max_length=150)
    owner = models.ForeignKey(Staff, on_delete=models.CASCADE)  # FK 1
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    country = models.CharField(max_length=100, default="India")
    description = models.TextField()
    rating = models.FloatField(default=0)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


# ---------------------- ROOM TYPE ----------------------
class RoomType(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    base_price = models.DecimalField(max_digits=10, decimal_places=2)

    def __str__(self):
        return self.name


# ---------------------- ROOM ----------------------
class Room(models.Model):
    STATUS_CHOICES = [
        ('Available', 'Available'),
        ('Booked', 'Booked'),
        ('Maintenance', 'Maintenance'),
    ]

    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)      # FK 2
    room_type = models.ForeignKey(RoomType, on_delete=models.CASCADE)  # FK 3
    room_number = models.CharField(max_length=20)
    floor = models.IntegerField()
    capacity = models.IntegerField()
    price_per_night = models.DecimalField(max_digits=10, decimal_places=2)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='Available')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.hotel.name} - {self.room_number}"


# ---------------------- AMENITY ----------------------
class Amenity(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField(blank=True)

    def __str__(self):
        return self.name


# ---------------------- ROOM AMENITY ----------------------
class RoomAmenity(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)      # FK 4
    amenity = models.ForeignKey(Amenity, on_delete=models.CASCADE)  # FK 5

    def __str__(self):
        return f"{self.room.room_number} - {self.amenity.name}"


# ---------------------- OFFER ----------------------
class Offer(models.Model):
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)  # FK 6
    title = models.CharField(max_length=100)
    discount_percentage = models.PositiveIntegerField()
    start_date = models.DateField()
    end_date = models.DateField()
    active = models.BooleanField(default=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.title} ({self.discount_percentage}%)"


# ---------------------- BOOKING ----------------------
class Booking(models.Model):
    BOOKING_STATUS = [
        ('Pending', 'Pending'),
        ('Confirmed', 'Confirmed'),
        ('Cancelled', 'Cancelled'),
    ]

    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)  # FK 7
    room = models.ForeignKey(Room, on_delete=models.CASCADE)          # FK 8
    check_in = models.DateField()
    check_out = models.DateField()
    guests = models.PositiveIntegerField()
    total_amount = models.DecimalField(max_digits=12, decimal_places=2)
    booking_status = models.CharField(max_length=20, choices=BOOKING_STATUS, default='Pending')
    special_request = models.TextField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Booking #{self.id} - {self.customer.full_name}"


# ---------------------- PAYMENT ----------------------
class Payment(models.Model):
    PAYMENT_METHOD = [
        ('Cash', 'Cash'),
        ('UPI', 'UPI'),
        ('Card', 'Card'),
        ('NetBanking', 'Net Banking'),
    ]

    PAYMENT_STATUS = [
        ('Pending', 'Pending'),
        ('Paid', 'Paid'),
        ('Failed', 'Failed'),
    ]

    booking = models.ForeignKey(Booking, on_delete=models.CASCADE)  # FK 9
    payment_method = models.CharField(max_length=20, choices=PAYMENT_METHOD)
    payment_status = models.CharField(max_length=20, choices=PAYMENT_STATUS, default='Pending')
    amount = models.DecimalField(max_digits=12, decimal_places=2)
    transaction_id = models.CharField(max_length=100, unique=True)
    payment_date = models.DateTimeField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Payment #{self.id} - {self.payment_status}"


# ---------------------- REVIEW ----------------------
class Review(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)  # FK 10
    hotel = models.ForeignKey(Hotel, on_delete=models.CASCADE)        # FK 11
    rating = models.IntegerField()
    comment = models.TextField()
    review_date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.customer.full_name} - {self.hotel.name}"


# ---------------------- INVOICE ----------------------
class Invoice(models.Model):
    payment = models.ForeignKey(Payment, on_delete=models.CASCADE)  # FK 12
    invoice_number = models.CharField(max_length=50, unique=True)
    tax_amount = models.DecimalField(max_digits=10, decimal_places=2)
    total_with_tax = models.DecimalField(max_digits=12, decimal_places=2)
    issued_date = models.DateField(auto_now_add=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.invoice_number



