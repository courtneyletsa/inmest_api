from django.shortcuts import render
from django.http import JsonResponse, HttpResponse
from django.views import View

from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
from main.models import *
from main.serializers import *
import datetime

# Create your views here.


def say_hello(req):
    return HttpResponse("<h1>Hello Fleur</h1>")

# function: UserProfile name: your name, email: your email, phone number: your phone number  
# view function returns a JsonResponse 
# register the view function on a path called profile

def user_profile(req):

    return JsonResponse(
        {
       "name": "Courtney" ,
       "email": "courtney.letsa@meltwater.org",
       "Phone_number": "0208047508"
    }
    )
    

# write a view function called filter_queries
# the view function should receive query_id through the url
# return a JsonResponse data with the following data id, title, description, status
#and submitted_by
#the id should be the id received through the url

def filter_queries(req,id):
    return JsonResponse(
        {
            "id": id,
            "title": "Wedding Dress",
            "description": "Lorem ipsum dolor sit amet, consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. Ut enim ad minim veniam",
            "status": "in progress",
            "submitted_by": "Courtney"
        }
    )
     
class QueryView(View):
    queries = [
        {
                "id":1, "title": "Adama declined Val shot"
            },
        {
                "id":1, "title": "Adama declined Val shot"
            }
        ]
    
    def get(self, req):

        return JsonResponse({"result": self.queries})
    
    def post(self,req):
        return JsonResponse({"status": "ok"})
    

@api_view(['GET']) 
def fetch_class_schedule(request):
    
    print("Usermaking", request.user)
    # 1. Retrive from database all class schedule
    queryset = ClassSchedule.objects.all()
    
    # 2. Return queryset results as response
    # 2b. transform or serialize the queryset result to json and send as response
    
    serializer = ClassScheduleSerializer(queryset, many=True)
    
    #3. Respond to the request
    return Response({"data": serializer.data}, status.HTTP_200_OK)

@api_view(['POST'])
def create_class_schedule(request):
    # receiving data from front-end
    title = request.data.get("title")
    description = request.data.get("description")
    start_date_and_time = request.data.get("start_date_and_time")
    end_date_and_time = request.data.get("end_date_and_time")
    cohort_id = request.data.get("cohort_id")
    venue = request.data.get("venue")
    facilitator_id = request.data.get("facilitator_id")
    is_repeated = request.data.get("is_repeated")
    repeat_frequency = request.data.get("repeat_frequency")
    course_id = request.data.get("course_id")
    meeting_type = request.data.get("meeting_type")
    
    print(title)
    
    if not title:
        return Response({"message":"My friend, send me title"}, status.HTTP_400_BAD_REQUEST)
    
    cohort = None
    facilitator = None
    course = None
    
    # validating the existence of records
    
    try:
        cohort = Cohort.objects.get(id=cohort_id)
    except Cohort.DoesNotExist:
        return Response({'message': 'Massa, this cohort does not exist'}, status.HTTP_400_BAD_REQUEST)
    try:
        facilitator = IMUser.objects.get(id=facilitator_id)
    except IMUser.DoesNotExist:
        return Response({'message': 'Massa, this facilitator does not exist'}, status.HTTP_400_BAD_REQUEST)
    try:
        course = Course.objects.get(id=course_id)
    except Course.DoesNotExist:
        return Response({'message': 'Massa, this course does not exist'}, status.HTTP_400_BAD_REQUEST)
    
    
    
    class_schedule = ClassSchedule.objects.create(
        title = title,
        description = description,
        venue = venue,
        is_repeated = is_repeated,
        repeat_frequency = repeat_frequency,
        facilitator = facilitator,
        cohort = cohort,
        course = course,
        organizer = facilitator,
        start_date_and_time = datetime.datetime.now(),
        end_date_and_time = datetime.datetime.now()
    )
    class_schedule.save()
    
    serializers = ClassScheduleSerializer(class_schedule, many=False)
    return Response({'message': 'Schedule sucessfully created', 'data': serializers.data}, status.HTTP_201_CREATED)