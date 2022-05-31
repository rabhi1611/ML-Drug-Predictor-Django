import numpy as np
import pandas as pd
from .apps import *
from rest_framework.views import APIView
from rest_framework.response import Response
from django.shortcuts import render, redirect
from django.http import request, response




class Prediction(APIView):
    def post(self, request):
        #data = request.data
        age= request.GET.get('age')
        gender = request.GET.get('gender')
        bp = request.GET.get('bp')
        cholesterol = request.GET.get('cholesterol')
        salt = request.GET.get('salt')
        dtree = ApiConfig.model
        #predict using independent variables
        PredictionMade = dtree.predict([[age, gender, cholesterol, bp, salt]])
        response_dict = {"Predicted drug": PredictionMade}
        print(response_dict)
        return Response(response_dict, status=200)


def index(request):
    return render(request, 'index.html', {})

def result(request):
    age= int(request.GET.get('age'))
    gender = int(request.GET.get('gender'))
    bp = int(request.GET.get('bp'))
    cholesterol = int(request.GET.get('cholesterol'))
    salt = int(request.GET.get('salt'))
    dtree = ApiConfig.model
        #predict using independent variables
    PredictionMade = dtree.predict([[age, gender, cholesterol, bp, salt]])
    response_dict = {"Predicted_drug": PredictionMade}
    return render(request, 'result.html', response_dict)
