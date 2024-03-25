# ORM
* Object-Relational-Mapping
* 객체 지향 프로그래밍 언어를 사용하여 호환되지 않는 유형의 시스템 간에 데이터를 변환하는 기술
* ORM의 역할
    * 사용하는 언어가 다르기 때문에 소통 불가 -> ORM이 중간에서 이를 해석

        ![django_orm_role](../image/django_orm_role.png)


# QuerySet API
* ORM에서 데이터를 검색, 필터링, 정렬 및 그룹화 하는데 사용하는 도구
    * API를 사용하여 SQL이 아닌 Python 코드로 데이터를 처리

        ![django_orm_queryset_API](../image/django_orm_queryset_API.png)
        
        * 다중데이터의 경우 'QuerySet', 단일데이터의 경우 'instance'로 반환

* QuerySet API 구문
    * `Article.objects.all()`
        * `Article` : model class
        * `objects` : manager
        * `all()` : Queryset API
* QuerySet API 구문 동작 예시

    ![django_orm_query_API](../image/django_orm_query_API.png)

* Query
    * 데이터베이스에 특정한 데이터를 보여 달라는 요청
    * "쿼리문을 작성한다" : 원하는 데이터를 얻기 위해 데이터베이스에 요청을 보낼 코드를 작성한다.
    * python으로 작성한 코드가 ORM에 의해 SQL로 변환되어 데이터베이스에 전달되며, 데이터베이스의 응답 데이터를 ORM이 QuerySet이라는 자료 형태로 변환하여 우리에게 전달
* QuerySet
    * 데이터베이스에게서 전달 받은 객체 목록(데이터 모음)
        * 순회가 가능한 데이터로써 1개 이상의 데이터를 불러와 사용할 수 있다.
    * Django ORM을 통해 만들어진 자료형
    * 단, 데이터베이스가 단일한 객체를 반환 할 때는 QuerySet이 아닌 모델(Class)의 인스턴스로 반환됨
    * QuerySet API는 python의 모델 클래스와 인스턴스를 활용해 DB에 데이터를 저장, 조회, 수정, 삭제 하는 것


# QuerySet API 실습
* 외부 라이브러리 설치 및 설정
```
$ pip install ipython
$ pip install django-extensions
```
```python
# settings.py
INSTALLED_APPS = [
    'articles',
    'django_extensions',
    ...,
]
```
```
$ pip freeze > requirements.txt
```
* Django shell
    * Django 환경 안에서 실행되는 python shell
    * 입력하는 QuerySet API 구문이 Django 프로젝트에 영향을 미침
    * Django shell 실행
        ```
        $ python manage.py shell_plus
        ```
## Create

## Read

## Update

## Delete