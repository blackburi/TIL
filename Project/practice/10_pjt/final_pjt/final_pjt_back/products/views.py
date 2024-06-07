from django.shortcuts import render
from rest_framework import status
from rest_framework import viewsets
from rest_framework.decorators import api_view
from rest_framework.response import Response
import requests
from django.http import JsonResponse
from django.conf import settings
from .models import DepositOptions, DepositProducts
from .serializers import DepositOptionsSerializer, DepositProductsSerializer
from django.views import View
from products.recommendation_model import load_trained_model
import numpy as np

# Create your views here.
API_KEY = settings.DEPOSIT_API_KEY
EXCHANGE_RATE_API_KEY = settings.EXCHANGE_RATE_API_KEY

# 정기예금 상품 목록과 옵션목록 DB에 저장
@api_view(["GET"])
def save_deposit_products(request):
    # 예금 데이터
    url = f'http://finlife.fss.or.kr/finlifeapi/depositProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()
    # is_valid -> serializer 로 데이터 저장 
    for li in response.get('result').get('baseList'):
        # 금융 상품 코드
        fin_prdt_cd = li.get('fin_prdt_cd', "없음")
        # 금융 회사 명
        kor_co_nm = li.get('kor_co_nm', "없음")
        # 금융 상품 명
        fin_prdt_nm = li.get('fin_prdt_nm', "없음")
        # 기타 유의 사항
        etc_note = li.get('etc_note', "없음")
        # 가입 제한
        join_deny = li.get('join_deny')
        # 가입 대상
        join_member = li.get('join_member', "없음")
        # 가입 방법
        join_way = li.get('join_way', "없음")
        # 우대 조건
        spcl_cnd = li.get('spcl_cnd', "없음")
        # 만기후 이자율
        mtrt_int = li.get('mtrt_int', "없음")
        # 예금
        DSname = '예금'

        save_data = {
            'fin_prdt_cd': fin_prdt_cd,
            'kor_co_nm': kor_co_nm,
            'fin_prdt_nm': fin_prdt_nm,
            'etc_note': etc_note,
            'join_deny': join_deny,
            'join_member': join_member,
            'join_way': join_way,
            'spcl_cnd': spcl_cnd,
            'mtrt_int': mtrt_int,
            'DSname' : DSname,
        }
        
        serializer = DepositProductsSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            
    for ol in response.get('result').get('optionList'):
        fin_prdt_cd = ol.get('fin_prdt_cd', "없음")
        product = DepositProducts.objects.get(fin_prdt_cd = fin_prdt_cd)
        intr_rate_type_nm = ol.get('intr_rate_type_nm', "없음")
        intr_rate = ol['intr_rate']
        if intr_rate==None:
            intr_rate = -1
        intr_rate2 = ol['intr_rate2']
        if intr_rate2==None:
            intr_rate2 = -1
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


# 적금 상품 목록과 옵션목록 DB에 저장
@api_view(["GET"])
def save_saving_products(request):
    # 적금 데이터
    url = f'http://finlife.fss.or.kr/finlifeapi/savingProductsSearch.json?auth={API_KEY}&topFinGrpNo=020000&pageNo=1'
    response = requests.get(url).json()
    # is_valid -> serializer 로 데이터 저장 
    for li in response.get('result').get('baseList'):
        # 금융 상품 코드
        fin_prdt_cd = li.get('fin_prdt_cd', "없음")
        # 금융 회사 명
        kor_co_nm = li.get('kor_co_nm', "없음")
        # 금융 상품 명
        fin_prdt_nm = li.get('fin_prdt_nm', "없음")
        # 기타 유의 사항
        etc_note = li.get('etc_note', "없음")
        # 가입 제한
        join_deny = li.get('join_deny')
        # 가입 대상
        join_member = li.get('join_member', "없음")
        # 가입 방법
        join_way = li.get('join_way', "없음")
        # 우대 조건
        spcl_cnd = li.get('spcl_cnd', "없음")
        # 만기후 이자율
        mtrt_int = li.get('mtrt_int', "없음")
        # 예금 or 적금
        DSname = '적금'

        save_data = {
            'fin_prdt_cd': fin_prdt_cd,
            'kor_co_nm': kor_co_nm,
            'fin_prdt_nm': fin_prdt_nm,
            'etc_note': etc_note,
            'join_deny': join_deny,
            'join_member': join_member,
            'join_way': join_way,
            'spcl_cnd': spcl_cnd,
            'mtrt_int': mtrt_int,
            'DSname' : DSname,
        }
        
        serializer = DepositProductsSerializer(data=save_data)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            
    for ol in response.get('result').get('optionList'):
        # print(ol)
        fin_prdt_cd = ol.get('fin_prdt_cd', "없음")
        product = DepositProducts.objects.get(fin_prdt_cd = fin_prdt_cd)
        intr_rate_type_nm = ol.get('intr_rate_type_nm', "없음")
        intr_rate = ol['intr_rate']
        if intr_rate==None:
            intr_rate = -1
        intr_rate2 = ol['intr_rate2']
        if intr_rate2==None:
            intr_rate2 = -1
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

class DepositProductsViewSet(viewsets.ModelViewSet):
    queryset = DepositProducts.objects.all()
    serializer_class  = DepositProductsSerializer


def get_exchange_rate(request):
    url ='https://www.koreaexim.go.kr/site/program/financial/exchangeJSON'
    params = {
        'authkey': EXCHANGE_RATE_API_KEY,
        'searchdate': '20240517',
        'data':'AP01'
    }
    response = requests.get(url,params=params)
    try:
        data = response.json()
    except ValueError:
        return JsonResponse({'error': 'Invalid JSON response'}, status=500)
    return JsonResponse(data, safe=False)

# 특정 상품의 옵션 리스트 반환
@api_view(["GET"])
def deposit_products_options(request, fin_prdt_cd):
    options = DepositOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
    serializer = DepositOptionsSerializer(options, many=True)
    return Response(serializer.data)

# 유저가 가입한 상품 조회
@api_view(["GET"])
def user_join_options(request):
    join_products = request.user.join_products.all()
    serializer = DepositOptionsSerializer(join_products,many=True)
    return Response(serializer.data)

# 특정 조건의 옵션 리스트 반환
@api_view(["GET"])
def want_options(request, save_trm) :
    options = DepositOptions.objects.filter(save_trm=save_trm)
    for option in options :
        products = DepositProducts.objects.filter(fin_prdt_cd=option.fin_prdt_cd)
    serializer = DepositProductsSerializer(products, many=True)
    return Response(serializer.data)

# 사용자가 가입한 상품 기반 AI 상품 추천
@api_view(["GET"])
def recommend_products(request, user_id):
    model, user_id_map, product_id_map = load_trained_model()
    
    if user_id not in user_id_map:
        return JsonResponse({'error': 'User not found'}, status=404)

    user_idx = user_id_map[user_id]
    product_indices = list(product_id_map.values())
    
    # 모델 출력
    user_array = np.array([user_idx] * len(product_indices))
    product_array = np.array(product_indices)
    
    predictions = model.predict([user_array, product_array]).flatten()
    
    product_recommendations = sorted(zip(product_id_map.keys(), predictions), key=lambda x: x[1], reverse=True)
    
    # Top 4 추천 출력
    top_recommendations = [product_id for product_id, _ in product_recommendations[:4]]
    
    return JsonResponse({'recommendations': top_recommendations})