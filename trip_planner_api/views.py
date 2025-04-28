from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action
from .models import TravelPlan
from .serializers import TravelPlanSerializer
import openai
from django.conf import settings
import os
from dotenv import load_dotenv

load_dotenv()

class TravelPlanViewSet(viewsets.ModelViewSet):
    queryset = TravelPlan.objects.all()
    serializer_class = TravelPlanSerializer

    @action(detail=False, methods=['post'])
    def generate_plan(self, request):
        destination = request.data.get('destination')
        start_date = request.data.get('start_date')
        end_date = request.data.get('end_date')
        budget = request.data.get('budget')
        preferences = request.data.get('preferences')

        # Set OpenAI API key
        openai.api_key = os.getenv('OPENAI_API_KEY')

        # Build prompt
        prompt = f"""
        Please generate a detailed travel itinerary for the following trip:
        Destination: {destination}
        Start Date: {start_date}
        End Date: {end_date}
        Budget: {budget}
        Preferences: {preferences}

        Please provide:
        1. Daily itinerary
        2. Recommended attractions
        3. Dining suggestions
        4. Transportation advice
        5. Budget allocation
        """

        try:
            # Call OpenAI API
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[
                    {"role": "system", "content": "You are a professional travel planner."},
                    {"role": "user", "content": prompt}
                ]
            )

            # Create new travel plan
            travel_plan = TravelPlan.objects.create(
                destination=destination,
                start_date=start_date,
                end_date=end_date,
                budget=budget,
                preferences=preferences,
                plan_details=response.choices[0].message.content
            )

            return Response({
                'status': 'success',
                'plan': TravelPlanSerializer(travel_plan).data
            })

        except Exception as e:
            return Response({
                'status': 'error',
                'message': str(e)
            }, status=500)
