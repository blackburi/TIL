from django.http import JsonResponse
from rest_framework.decorators import api_view
import random
import pandas as pd
import numpy as np
import csv

array_length = 1000
random_range = 5000

@api_view(['GET'])
def bubble_sort(request):
    li = []
    for i in range(array_length):
        li.append(random.choice(range(1, random_range)))
    for i in range(len(li) - 1, 0, -1):
        for j in range(i):
            if li[j] < li[j + 1]:
                li[j], li[j + 1] = li[j + 1], li[j]
    context = {
      'top': li[0]
    }
    return JsonResponse(context)

@api_view(['GET'])
def normal_sort(request):
    li = []
    for i in range(array_length):
        li.append(random.choice(range(1, random_range)))
    li.sort(reverse=True)
    context = {
        'top': li[0]
    }
    return JsonResponse(context)

from queue import PriorityQueue

@api_view(['GET'])
def priority_queue(request):
    pq = PriorityQueue()
    for i in range(array_length):
        pq.put(-random.choice(range(1, random_range)))
    context = {
        'top': -pq.get()
    }
    return JsonResponse(context)

@api_view(['GET'])
def csv_to_df(request):
    df = pd.read_csv('./data/test_data.CSV',encoding='cp949',usecols=['나이'])
    data = df.to_dict('records')
    
    return JsonResponse({'data' : data})


@api_view(['GET'])
def dropna(request):
    df = pd.read_csv('./data/test_data_has_null.CSV',encoding='cp949',usecols=['나이'])
    df_new = df.dropna(axis=0)
    data = df_new.to_dict('records')


    return JsonResponse({'data' : data})

@api_view(['GET'])
def age_nearest(request):
    df = pd.read_csv('./data/test_data_has_null.CSV',encoding='cp949',usecols=['나이'])
    df_new = df.dropna(axis=0)
    df_nearest = df_new.iloc[(df_new['나이']-df_new['나이'].mean()).abs().argsort()[:10]]
    data = df_nearest.to_dict('records')
    return JsonResponse({'data' : data})

@api_view(['GET'])
def average_test(request):
    df = pd.read_csv('./data/test_data_has_null.CSV',encoding='cp949',usecols=['나이'])
    df.dropna(subset=['나이'], inplace=True)
    mean = df['나이'].mean()
    df = df.sort_values(by='나이', key=lambda x: abs(x - mean)).head(10)
    data = df.to_dict('records')
    return JsonResponse({'data': data})