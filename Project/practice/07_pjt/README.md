
# PJT 07

### 이번 pjt 를 통해 배운 내용

* REST API 서버를 직접 구현한다 
(REST API : REST 방법론을 따라 개발한 API)


* .env 
- 환경변수 
- 루트 디렉토리에 위치해야하며, Debug, API_KEY를 저장해둔다. 
- 텍스트 파일로 되어있으며 키-값 쌍 형태로 설정 값을 저장한다.
- .env의 API_KEY를 넘긴다 
```python 
# project/settings.py

import os
import environ

env = environ.Env(DEBUG=(bool, True))
environ.Env.read_env(
    env_file=os.path.join(BASE_DIR, '.env')
)

WEATHER_API_KEY = env('API_KEY')
```



## A. 정기예금 상품 목록 DB저장
* 요구 사항 : 정기예금 API로부터 전달 받은데이터 상품 중 목록 정보와 옵션 목록 정보를 DB에 저장한다. 

* 결과 : 10명의 사람에게 보내지 않으면 ....
  
  ```python
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
  ```
  
  * 이 문제에서 어려웠던점
    - `get`을 통해 그동안 pk(integer)로 가져왔던 것을 str 형태로 처음 가져와보는것 같았다.
  * 내가 생각하는 이 문제의 포인트
    - dictionary method를 활용하여 각각에 대하여 default값을 알맞게 설정하는 것이 포인트였다.

-----


## B. 전체 정기예금 상품 목록 출력
* 요구 사항 : 아래 URL 로 요청이 오면 DB에 저장된 정기예금 상품 목록을 반환하도록 코드를 구현한다.

* 결과 : 10명의 사람에게 보내지 않으면 ....
  
  ```python
  @api_view(["GET", "POST"])
  def deposit_products(request):
    if request.method == "GET":
      deposit_products = DepositProducts.objects.all()
      serializers = DepositProductsSerializer(deposit_products, many=True)
      return Response(serializers.data)
  ```
  
  * 이 문제에서 어려웠던점
    - `serializers`와 원하는 data에 따라 알맞은 return(여기서는 `Response`)에 함수를 적용하는 것이 까다로웠다.
  * 내가 생각하는 이 문제의 포인트
    - `GET`과 `POST`중 `GET`에 해당하는 부분을 가져와서 내가 원하는 형태로 데이터를 알맞게 변환하여 가져오는 것

-----


## C. 정기예금 상품 추가하기
* 요구 사항 : 아래 URL 로 요청이 오면 요청과 함께 전송한 데이터를 DB에 저장하도록 코드를 구현한다.

* 결과 : 10명의 사람에게 보내지 않으면 ....
  
  ```python
  @api_view(["GET", "POST"])
  def deposit_products(request):
    elif request.method == "POST":
      serializer = DepositProductsSerializer(data=request.data)
      if serializer.is_valid():
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
  ```
  
  * 이 문제에서 어려웠던점
    - `serializers`와 원하는 data에 따라 알맞은 return(여기서는 `Response`)에 함수를 적용하는 것이 까다로웠다. 또한 return값에 추가로 `status`를 추가하여 알맞은 response message를 출력하는 것을 생각해야 했다.
  * 내가 생각하는 이 문제의 포인트
    - `GET`과 `POST`중 `POST`에 해당하는 부분을 가져와서 내가 원하는 형태로 데이터를 알맞게 변환하여 가져오는 것

-----


## D. 특정 상품의 옵션 리스트 출력
* 요구 사항 : 아래 URL 로 요청이 오면 상품 코드에 따라 해당 상품의 옵션 리스트를 출력하도록 코드를 구현한다.

* 결과 : 10명의 사람에게 보내지 않으면 ....
  
  ```python
  @api_view(["GET"])
  def deposit_products_options(request, fin_prdt_cd):
    options = DepositOptions.objects.filter(fin_prdt_cd=fin_prdt_cd)
    serializer = DepositOptionsSerializer(options, many=True)
    return Response(serializer.data)
  ```
  
  * 이 문제에서 어려웠던점
    - 외래키가 아닌 `.filter()`를 사용하여 원하는 data를 가져오고 이것을 원하는 형태로 return하는 것이 까다로웠다.
  * 내가 생각하는 이 문제의 포인트
    - 외래키를 가져오는 `model_set()`형태가 아닌 `.filter()`로 가져오는 것이 중요했다.

-----

## E. 금리가 가장 높은 상품의 정보 출력
* 요구 사항 : 아래 URL 로 요청이 오면 금리가 가장 높은 상품의 상세정보와 옵션을 반환하도록 코드를 구현한다.

* 결과 : 10명의 사람에게 보내지 않으면 ....
  
  ```python
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
  ```
  
  * 이 문제에서 어려웠던점
    - 원하는 data를 가져오는데에 data전체를 가져오고 원하는 데이터(금리가 가장 높은 상품)를 추출하는 것이 아닌 data전체를 가져오는 동시에 `order_by()`를 통하여 정렬된 형태로 가져오고 index접근으로 원하는 데이터를 추출하는 것이 어려웠다.
  * 내가 생각하는 이 문제의 포인트
    - `order_by()`를 이용하여 원하는 데이터를 정렬된 형태로 가져와서 index로 쉽게 가져오는 것이 포인트였다.

-----


# 후기

* 송민정 : 오늘 프로젝트는 쉬워 보였지만 종합적으로 적용하고 활용하는 것이 어려웠다.
* 최병주 : 배운내용들을 활용하고 API를 이용하여 전반적인 backend경험을 할 수 있었다.
* 김태경 : 그동안 배운것을 이용하고 부족하거나 필요한 부분은 공식 문서를 통해 찾아보는 방법을 기를수 있었다.
