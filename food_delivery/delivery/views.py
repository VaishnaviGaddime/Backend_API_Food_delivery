# delivery/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from .models import Pricing

class CalculatePrice(APIView):
    def post(self, request):
        zone = request.data.get('zone')
        organization_id = request.data.get('organization_id')
        total_distance = request.data.get('total_distance')
        item_type = request.data.get('item_type')
        
        try:
            pricing = Pricing.objects.get(organization_id=organization_id, zone=zone)
            base_price = pricing.fix_price
            if total_distance > pricing.base_distance_in_km:
                extra_distance = total_distance - pricing.base_distance_in_km
                per_km_price = pricing.km_price
                total_price = base_price + extra_distance * per_km_price
            else:
                total_price = base_price
            return Response({'total_price': total_price}, status=status.HTTP_200_OK)
        except Pricing.DoesNotExist:
            return Response({'error': 'Pricing not found for the specified organization and zone'}, status=status.HTTP_404_NOT_FOUND)
