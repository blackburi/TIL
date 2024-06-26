Markdown & CLI & Git 에 대하여

# Markdown
* 일반 text로 문서를 작성하는 간단한 방법이다.
* 주로 개발자들이 text와 code를 작성해 문서화 하기 위해서 사용한다.
* 작성된 markdown문서는 다른 프로그램에 의해 변환되어 출력된다.

## Heading
* 문서의 단계별 제목으로 사용
* #의 개수에 따라 제목의 수준을 구별
    * #의 개수가 많아질수록 제목의 크기가 작아진다.
    * #은 최대 6개까지 사용 가능하다.

## List
* 순서가 없는 list
    * list1 (*, +, - 를 사용하면 bullet point로 나오게 된다.)
        * 내부 list로 나온다.
            * 또 내부 list
* 순서가 있는 list
    1. number.space 를 하면 순서가 있는 list가 된다.
    2. 두 번째 순서 list
        1. 내부 list 2-1
            1. 내부 리스트 2-1-1
* 순서가 있는 list와 순서가 없는 list 같이 사용 가능하다.
    1. 순서가 있는 list
        * 내부에 순서가 없는 list
    * 순서가 없는 list
        1. 내부에 순서가 있는 list
* 들여쓰기
    * 줄을 바꾼후(enter) space key 4번 또는 tab key 한번 눌러주면 된다.

## code block
* code를 보낼때 text형식이 아닌 code형식 그대로 보여주는 것이 가능하게 만들어주는 기능이다.
* Tab key 바로 위 key를 사용한다.
* code가 여러 줄일 경우 (앞뒤로 3번씩 사용)
```python
@app.route('/lotto')
def make_lotto():
    numbers = range(1,46)
    #sample 비복원 랜덤 추출
    #random.sample(후보, 갯수)
    lotto = random.sample(numbers, 6)
    return lotto
```
* code가 한 줄일 경우 (앞뒤로 1번씩 사용)
    * 반드시 한 줄을 띄어 쓰기 해야 한다.

`lotto = random.sample(number,6)`

## Link & image
* link는 `[text](address)` 형식으로 입력한다.
    [구글 바로가기](https://google.com)
* image는 `![text](location)` 형식으로 입력한다.
    * local image 넣어보기
    ![마스터이](./image/masterlee.jpg)
        * markdown file을 옮길 경우 local image 또한 같이 옮겨야 한다.
        * location은 `git init`으로 지정된 현재 위치로부터 상대 경로를 입력한다. (상대 경로는 뒤에서 다룬다.)
    * internet image 넣어보기
    ![마스터이](https://ddragon.leagueoflegends.com/cdn/img/champion/splash/MasterYi_89.jpg)


## text 관련 문법
* 글자 굵게 만들기
    * 앞뒤로 **를 붙여준다.
    * 이렇게 **굵게** 만들 수 있다.
* 글자 기울이기
    * text 앞뒤로 * 하나를 붙여준다.
    * 이렇게 *기울일* 수 있다.
* 글자 취소선 긋기
    * 글자 앞뒤로 ~~ 를 붙여준다.
    * 이렇게 ~~취소선~~을 그을 수 있다.

## 구분선
* -(hypen, dash, 빼기)를 3개 이상 사용하면 된다.
---

## 인용문 작성하기
* `>`를 이용하여 인용문 형태로 만들 수 있다.
* `>>`와 같이 여러번 사용하면 인용문 내부에 인용문을 만들 수 있다.

> 인용문 만들기
>> 내부 인용문 만들기

>인용문 만들기1
>인용문 만들기2

* 인용문 구분을 가능하게 할 수 있다.

## table 작성
* `\` 또는 원화 key를 shift와 함께 누르면 `|`가 작성된다.
* `|`를 제일 앞과 뒤, 구분을 해야 하는 곳에 넣어 작성한다.
* 첫 줄과 두번째 줄 사이에는 `|---|---|`를 삽입해야 한다.

|이름|나이|
|---|---|
|김XX|27살|
|임XX|27살|
|김XX|28살|
* `:`를 이용하여 정렬할 수 있다.
    * |---:| 우측정렬
    * |:---| 좌측정렬
    * |:---:| 가운데정렬



# CLI
* = command Line Interface
* 명령어를 통해 사용자와 컴퓨터가 상호 작용하는 방식

> ## vs GUI
> GUI = Graphic User Interface
> 그래픽을 통해 사용자와 컴퓨터가 상호 작용하는 방식

* CLI를 사용해야 하는 이유
    * GUI는 CLI에 비해 사용하기 쉽지만 단계가 많고 성능을 상대적으로 더 많이 소모
    * 수많은 server/개발system이 CLI를 통한 조작 환경을 제공한다.

## CLI에서 .(점)의 역할
* .은 현재 directory(위치)를 의미
    * CLI에서는 현재 위치를 아는 것이 매우 중요하다.
* ..은 현재 directory에서의 상위 directory(부모 folder)를 의미한다.
* CLI에서 ~는 home directory를 의미한다.
    * window에서 home directory는 'C드라이브/User/사용자로그온 ID'가 기본 설정이다
    * window 초기 설치하는 경우 home directory는 `C:/User/admin`이 된다.

## CLI 기초 문법
* touch
    * file 생성
* mkdir
    * new directory 생성
* ls
    * 현재 작업 중인 directory 내부의 folder/file을 보여준다.
    * `/`가 있다면 folder임을 나타낸다.
    * `ls -a`를 입력하면 숨겨진 모든 folder/file을 보여준다.
* cd
    * 현재 작업중인 directory를 변경한다. (위치 이동)
    * 한 번에 여러개를 넘어갈 순 없다. 반드시 순차적으로 넘어가야 한다.
* start
    * folder/file 열기
* code
    * vscode로 열기 : `code(file name)`
    * python으로 열기 : `python(file name)`
* rm
    * delete file (-r을 사용하여 directory 삭제)
        * `rm`을 사용하면 directory 안에 다른 file들이 있을 경우가 있어서 바로 삭제가 불가능
        * `rm -r`을 사용하면 전부 삭제 가능

## 절대 경로
* Root directory부터 목적 지점까지 거치는 모든 경로를 전부 작성한 것이다.
* 기준점은 없지만 모든 경로가 표시된다.
> window의 root directory는 C:/ (C드라이브)이다.
> window 바탕화면의 절대 경로는 `C:/Users/admin/Desktop`이다.
> 이때 admin은 C드라이브 안에 있는 사용자 ID가 된다.

## 상대 경로
* 현재 작업하고 있는 directory를 기준으로 계산된 상대적인 위치를 말한다.
* 모든 경로가 표시되지 않지만 현재 위치를 기준으로 상대적인 위치가 표시된다.
* 절대 경로가 너무 길어지는 경우 상대 경로를 사용한다.
> 만약 현재 작업하고 있는 directory가 `C:/Users`일 때 window 바탕 화면으로의 상대 경로는 `admin/Desktop` 이다.

# Git
* 분산 version 관리 system
    * version 관리 : 변화를 기록하고 관리하는 것
        * ex) google docs
    * 각 version은 이전 version으로부터 변경 사항을 기록하고 있다.
    * 하나의 변경 사항을 commit이라고 한다.
    * 변경된 과정과 최종 파일만이 저장되면서 용량을 줄일 수 있다.
    > 기존의 파일 저장 방식
    > file1 = A
    > file2 = A+B
    > file3 = A+B+C
    > 최종file = A+B+C+D
    > => A가 4변, B가 3번, C가 2번, D가 1번 저장된다.
    
    > Git의 파일 저장 방식
    > file = A
    > commit1 = B
    > commit2 = C
    > commit3 = D
    > => A,B,C,D가 각각 1번씩만 저장되고 최종 file은 A+B+C+D로 보여진다.
* 중앙 vs 분산
    * 중앙 집중식 : version은 main server에 저장되고 main server에서 file을 가져와 edit후 다시 main server에 upload
        * 보안이 필요한 곳이라면 중앙 집중식이 용이하다.
        * main server에 error가 있다면 전부 이용이 불가하다. 따라서 backup file, main server에 대한 정책이 중요하다.
    * 분산식 : version을 여러 개의 복제된 저장소에 저장 및 관리 (version 정보를 모든 곳에서 가지고 있으며 관리한다.) -> Git이 대표적이다.
        * 동일한 정보를 여러 곳에서 가지고 있기 때문에 한 곳에 error가 발생하면 다른 곳에서 가져와 금방 살릴 수 있다.
        * main server에 의존하지 않고도 동시에 다양한 작업을 수행할 수 있다.
            * 개발자들 간의 작업 충돌을 줄여주고 개발 생산성을 향상할 수 있다.
        * main server의 장애나 손실에 대비하여 backup과 복구가 용이하다.
        * internet이 연결되지 않은 환경에서도 작업을 계속 할 수 있다.
            * 변경 이력과 code를 local 저장소에 기록하고, 나중에 main server와 동기화 한다.

## Git의 역할
* code의 version(history)를 관리
    * 개발되어 온 과정 파악
* 이전 version과의 변경 사항 비교
* code의 '변경 이력'을 기록하고 협업을 원활하게 하는 도구 이다.
* git은 system이고 github, gitlab 등은 system을 이용하는 업체들이다.
    * git이라는 동일한 system을 사용하기 때문에 github에서 사용한 것을 gitlab에 저장이 가능하다.
    * gitlab은 삼성 SDS에서 관리하는 server이기 때문에 기본적으로 private으로 되어 있지만 github의 경우 기본적으로 public으로 설정되어 있기 때문에 노출이 된다. 이것을 private으로 설정하여 사용하면 개인적으로 사용이 가능하다.

## Git의 3가지 영역
1. WD(=Working Directory) : 현재 작업
    * 실제 작업 중인 file들이 위치하는 영역
2. SA(=Staging Area) : 선별하는 곳
    * WD에서 변경된 file 또는 생성된 file 중에서 version 관리에 포함시킬 file들을 선택적으로 추가하거나 제외할 수 있는 중간 선별 공간
3. Respository : 저장소
    * version 이력과 file들이 영구적으로 저장되는 영역
    * 모든 version과 변경 이력이 기록된다.
    * commit = version의 변경 사항
        * 변경된 file들을 저장하는 행위이다.
        * 마치 사진을 찍듯이 기록한다 하여 'snapshot'이라고도 한다.

![git_basic](../image/basic_coding/basic_coding_git_basic.png)

## Git의 동작
* `git init`
    * (master)가 뜬다.
    * local 저장소 설정(초기화)
    * 내가 version 관리를 하고자 하는 곳에 git init을 해야 한다.
        * 최초 1회만 하면 된다.
        * 이 영역을 git으로 관리한다고 선언하는 것
    * git init 주의사항
        * git local 저장소 내에 또다른 git local 저장소를 만들지 말것
            * 즉 이미 git local 저장소인 directory 내부 하단에서 git init 명령어를 다시 입력하지 말것
        * git 저장소 안에 git 저장소가 있을 경우 가장 바깥 쪽의 git 저장소가 안쪽의 git 저장소의 변경 사항을 추적할 수 없기 때문이다.
            * project 단위가 너무 클 경우에 사용한다.
                * 나눠서 관리하거나 수정하기 편함
            * 가장 바깥 범위의 git 저장소에 private을 걸어 허용한 사람만이 가져올 수 있도록 만드는 경우에 사용한다.
* `git add`
    * 변경 사항이 있는 file을 staging area에 추가
    * 내가 생성/수정한 file의 version을 관리하기 위해 선별하는 곳으로 file을 보내는 명령어
    * `git add (file name)` file name에 해당하는 특정 file을 staging area로 이동된다.
    * `git add.` 현재 위치에 있는 모든 file을 SA로 추가 한다는 명령어
        * `git rm --cached (file name)` SA에서 WD로 다시 이동시켜 주는 명령어
* `git commit`
    * SA에 있는 file들을 Respository(저장소)에 기록
    * `git commit -m (message)` 형식으로 입력
        * 협업시 팀원이 알아볼 수 있도록 message를 잘 입력해야 한다.
        * message는 반드시 입력해야 한다.
    * commit 입력시 누가 입력을 했는지 표시해야 한다.
* `git status`
    * 현재 git의 status를 보여준다.
    > untracted : 현재 file중에 생성된 file이 존재 한다. 즉 git version 관리가 되지 않은 file이 존재한다.
    > modified : 이미 관리되고 있는 file을 알려준다.
    >> 빨강색은 WD, 초록색은 SA에 있는 file을 보여준다.
    > changes : 변경 사항이 있는 file이 존재 한다.
* `git log`
    * 지금까지의 file의 변경 사항들을 모두 보여준다.
    * git log가 너무 길 경우 화살표 방향을 이용하여 제일 아래로 내려가면 (END)가 나오고 그 이후 `q`를 입력하면 나갈 수 있다.
* `git log --oneline`
    * commit 목록을 한줄로 볼 수 있다.
* `git config --global -l`
    * git global 설정 정보 보기
    * `git config --global user.email ''` 개발자의 email 입력
    * `git config --global user.name ''` 개발자 이름 입력
    * `git config --global --list`를 통해 개발자의 이름과 email을 알 수 있다.
        * global을 한번 설정해 두면 앞으로 자정하지 않아도 된다. 최초 1회 설정만 하면 된다.
    
=> git은 git 영역 내의 모든 file의 변경 사항을 감시 하고 있다.

## vim
* git bash에서 실행되는 명령어
* command mode
    * vim을 실행하면 기본적으로 command mode를 불러온다.
    * esc를 누르면 나갈 수 있다.
* edit mode : `i`를 누르면 command mode에서 edit mode로 바꿔 실행할 수 있다.
* `:wq`를 입력하면 file을 저장하고 vim에서 나갈 수 있다.
* `:q`를 하면 저장하지 않고 vim에서 나갈 수 있다.
* 저장 이후 `git commit -m (file name)`을 통해 저장한다면 'Please tell me who you are'이라는 문구와 함께 작성자가 누구 인지 묻는다.
        
### 로컬 = local
* 현재 사용자가 직접 접속하고 있느 기계 또는 시스템
* 개인 컴퓨터, 노트북, 태블릿 등 사용자가 직접 조하는 환경