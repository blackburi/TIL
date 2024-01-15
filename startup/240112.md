Local & Remote Repository / Github에 대하여

# Remote Repository
* = 원격 저장소
* code와 version관리 이력을 online 상의 특정 위치에 저장하여 여러 개발자가 협업하고 code를 공유할 수 있는 저장 공간이다.
* public 상태이기 떄문에 누구나 접근 가능하며 여러 사람이 협업하기에 용이하다.
* Gitlab, Github, Bitbucket 등이 있다.
    * Gitlab은 회상서 대부분 사용하며 private으로 사용하기 위해서는 Github를 많이 사용한다.
    * 앞으로 나는 github를 이용해볼 것이다.

# Local & Remote Repository

## connect local & remote repository
* 대부분의 경우 local repository는 개인 computer가 되는 경우가 많다.
* remote repository는 생성해야 한다.
    * [github](https://github.com/blackburi/TIL)에서 remote repository를 생성한다.
* `git init`으로 git의 영역으로 설정된 곳에서 `git remote add (nickname) (URL)`의 형태로 입력하여 local repository와 remote repository를 연결한다.
    * 대부분의 개발자들은 `git remote add origin (URL)`을 사용하여 nickname을 origin으로 대부분 사용한다. 무엇을 사용하든 상관은 없다.
    * 만약 기존 repository를 잘못 설정했다면 `git remote remove (nickname)`을 통해서 설정된 repository를 삭제할 수 있다.
    * URL은 remote repository의 address를 의미한다.
* local & remote repository가 연결되어 있는지를 보기 위해서는 `git remote -v`를 입력해보면 된다.

## push
* local repository와 remote repository가 연결된 이후에 local repository에서 remote repository로 data를 upload하는 명령어이다.
* local repository에서 remote repository로 이동하기 위해선 명령어가 필요하다.
    * `git push -u (nickname) (branch)`의 형태로 data를 upload할 수 있다.
    * 이때 nickname은 local repository에서 설정한 것(origin)이고, branch는 remote repository에서의 이름을 의미한다.
        * 나의 경우 github에서의 branch는 master이기 때문에 앞으로 branch는 master로 사용할 것이다.
        * `git push -u origin master`
    * 주의해야 할 점은 commit이 있어야만 push가 가능하다. commit을 통해 local repository로 data를 옮겨야만 push를 통해 local repository에서 remote repository로 data를 옮길 수 있다.

## local & remote repository 주의점
* remote repository를 사용하는 이유는 여러 사람이 협업을 하기 위함이다. 따라서 push하는 경우 조심해야 한다.
* A project(ver1)을 P와 Q 두 사람이 작업하려한다.
    1. P와 Q가 모두 A(version1)을 pull(or clone)을 한다.
    2. P와 Q가 작업을 마치고 push할 때 충돌이 일어나지 않기 위해서는 version information이 동일해야 한다. P가 작업을 마치면 A(version2), Q가 작업을 미치고 A(verison2')가 되었다.
        * P와 Q가 동시에 push를 하면 A의 version정보다 동일하지 않아 충돌이 일어난다.
    3. P가 A(version2)를 먼저 push하고 Q가 A(version2)를 pull한 이후에(version information을 맞춘 이후에) A(version2')를 push해야 한다.

## pull & clone
* `git pull origin master` remote repository의 변경 사항만을 받아옴(update)
    * remote repository와 local repository 모두 존재 해야 'pull'이 가능
* `git clone remote_repo_url` remote repository 전체를 복제(download)
    * remote repostitory는 존재하고 local repository가 없는 경우 local repository에 remote repository를 복제하는 경우에 사용된다.
    * 최초 1회에만 사용하면 된다.

* 'A'에서 작업하여(v1) remote repository에 push했다.
> local repository가 있는 경우
> pull -> (작업) -> add -> commit -> push 순서로 진행한다.
>
> local repository가 없는 경우
>
> clone -> (작업) -> add -> commit -> push 순서로 진행한다.

# gitignore
* git에서 특정 file이나 directory를 추적하지 않도록 설정하는데 사용되는 text file
    * 이때 '추적하지 않는다'는 의미는 version관리를 할 필요가 없다는 것을 뜻한다.
* project에 따라 공유하지 않아야 하는 것들도 존재하기 때문에 사용하는 기능이다.
> 사용법 예시
> 1. `touch .gitignore` gitignore file 생성 (file명 앞에 반드시 '.'을 입력, 확장자는 없음)
>       * `ls -a`로 생성되었는지 확인할 수 있다.
> 2. `vim .gitignore`를 통해 gitignore에 설정할 파일을 찾는다
> 3. vim
> 4. git init
> 5. git status로 확인

## 
* file이름 앞에 `.`이 존재 한다면 숨겨진 파일을 의미한다
* 따라서 `ls`를 사용하면 보이지 않지만 `ls -a`를 하면 전부 볼 수 있다.

* gitignore는 중요도가 높은 (보안이 필요한) 경우이거나 필요성이 낮은 경우 지정한다.

## gitignore 주의사항
* 이미 git의 관리를 받는 파일이라 디렉토리는 

* gitignore 설정 서비스
* 운영체제, 프레임워크. 프로그래밍, 
a.txt 수정
a.txt는 git commit이 한번된 상태
commit 후 .gitignore에 등록이 되면
어떻게 될까요?

1. 버전 관리 대상에서 빠질까요?
2. 아니면 게속 버전 관리가 될까요?

정답은 : 2번
이미 관리 대상이라면 .gitignore에 등록을 해도 관리 대상에 포함이 이미 되어있기 때문에 변경사항이 추적되고 있다.
.gitignore는 관리 대상에 포함되지 않도록 막는 역할을 한다.
한번이라도 commit이 된 file을 .gitignore에 등록하려면
git rm --cached파일명
명령어를 이용해서 관리 대상에서 삭제해야 한다.

# github활용
1. project 협업
2. 개인 포트폴리오
    * github에 commit을 하는 만큼 profile에 잔디를 심는다고 표현하는 commit contribution을 볼 수 있다. 내가 commit을 할 때마다 색이 채워진다.
    * 단 github에 등록된 email과 `git config --global user.email ''`에 등록된 email이 **동일**해야 commit contribution이 채워진다.

* TIL(=Tody I Learn)을 통해 내가 학습한 것을 기록
* 개인, team project code를 공유

## TIL
* = Today I Learn
* 매일 내가 배운 것을 Markdown으로 정리해서 문서화하는 것
    * 단순히 배운 것만을 필기하는 것이 아닌 스스로 더 나아가 어떤 학습을 했는지를 기록하는 것

## '문서화'의 중요성
* 신입 개발자에게 요구되는 가장 중요한 항목
* 'https://d2.naver.com/news/3435170' 꼭 읽어보면 좋은 자료