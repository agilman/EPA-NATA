from django.shortcuts import render

from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt

from nataMaps.models import *
from nataMaps.serializers import *
# Create your views here.


def index(request):
    return render(request,"index.html")


@csrf_exempt
def countyDiesel(request,countyId=None,stateId=None):
    if request.method=="GET":
        tracts = Tract.objects.filter(stateFP=stateId).filter(countyFP=countyId)
        tractsSerialized = DieselSerializer(tracts,many=True)

        return JsonResponse(tractsSerialized.data, safe=False)

@csrf_exempt
def stateCounties(request, stateId=None):
    if request.method=="GET":
        counties = Tract.objects.filter(stateFP=stateId).values('countyFP','countyName').distinct()
        countiesSerialized = CountiesSerializer(counties,many=True)
                              
        return JsonResponse(countiesSerialized.data,safe=False)

@csrf_exempt
def states(request):
    if request.method=="GET":
        states = Tract.objects.values('stateFP','stateName').distinct()
        statesSerialized = StatesSerializer(states,many=True)

        return JsonResponse(statesSerialized.data,safe=False)
