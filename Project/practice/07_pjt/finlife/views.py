from django.shortcuts import render
from rest_framework import status
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from django.http import JsonResponse
from django.conf import settings
from .models import DepositOptions, DepositProducts
from .serializers import DepositOptionsSerializer, DepositProductsSerializer
# Create your views here.

API_KEY = settings.DEPOSIT_API_KEY

# A : 정기예금 상품 목록과 옵션목록 DB에 저장
@api_view(["GET"])
def save_deposit_products(request):
    # API로 전체 데이터 다 가져온거고 
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()
    # is_valid -> serializer 로 데이터 저장 
    for li in response.get('result').get('baseList'):
        fin_prdt_cd = li.get('fin_prdt_cd', "없음")
        kor_co_nm = li.get('kor_co_nm', "없음")
        fin_prdt_nm = li.get('fin_prdt_nm', "없음")
        etc_note = li.get('etc_note', "없음")
        join_deny = li.get('join_deny')
        join_member = li.get('join_member', "없음")
        join_way = li.get('join_way', "없음")
        spcl_cnd = li.get('spcl_cnd', "없음")

        save_data = {
            'fin_prdt_cd': fin_prdt_cd,
            'kor_co_nm': kor_co_nm,
            'fin_prdt_nm': fin_prdt_nm,
            'etc_note': etc_note,
            'join_deny': join_deny,
            'join_member': join_member,
            'join_way': join_way,
            'spcl_cnd': spcl_cnd,
        }
        
        serializer = DepositProductsSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            
    for ol in response.get('result').get('optionList'):
        fin_prdt_cd = ol.get('fin_prdt_cd', "없음")
        product = DepositProducts.objects.get(fin_prdt_cd = fin_prdt_cd)
        intr_rate_type_nm = ol.get('intr_rate_type_nm', "없음")
        intr_rate = ol.get('intr_rate', -1)
        intr_rate2 = ol.get('intr_rate2', -1)
        save_trm = ol.get('save_trm', -1)
        
        save_data = {
            'fin_prdt_cd': fin_prdt_cd,
            'intr_rate_type_nm': intr_rate_type_nm,
            'intr_rate': intr_rate,
            'intr_rate2': intr_rate2,
            'save_trm': save_trm,
        }
        
        serializer = DepositOptionsSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save(product = product)
    # 데이터 삽입 실패시 적절한 실패 안내 문구를 작성해야한다. 
    return JsonResponse({"message" : "okay"})

#  GET : 전체 정기예금 상품 목록 반환, POST 상품 데이터 저장
@api_view(["GET", "POST"])
def deposit_products(request):
    # B
    if request.method == "GET":
        deposit_products = DepositProducts.objects.all()
        serializers = DepositProductsSerializer(deposit_products, many=True)
        return Response(serializers.data)
    # C
    elif request.method == "POST":
        serializer = DepositProductsSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 특정 상품의 옵션 리스트 반환
# D
@api_view(["GET"])
def deposit_products_options(request, fin_prdt_cd):
    options = DepositOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
    serializer = DepositOptionsSerializer(options, many=True)
    return Response(serializer.data)


# 가입 기간에 상관없이 금리가 가장 높은 상품과 해당 상품의 옵션 리스트 출력 
@api_view(["GET"])
def top_rate(request):
    options = DepositOptions.objects.order_by("-intr_rate2")
    option = options[0]
    product = option.product
    context = {
        'deposit_product' : DepositProductsSerializer(product).data,
        'options' : DepositOptionsSerializer(option).data,
    }
    return Response(context)