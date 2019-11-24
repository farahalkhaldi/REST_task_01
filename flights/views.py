from .models import Flight, Booking
from .serializers import FlightSerializer, BookingSerializer

from rest_framework.generics import ListAPIView
from datetime import datetime

class FlightsList(ListAPIView):
	queryset = Flight.objects.all()
	serializer_class = FlightSerializer


class BookingsList(ListAPIView):
	queryset = Booking.objects.filter(date__gte=datetime.today())
	serializer_class = BookingSerializer