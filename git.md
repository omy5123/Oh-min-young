# Python day 2

git을 쓰는 이유

- 차이가 무엇이고 수정 이유를 log로 남길 수 있다

- 오픈소스 기반으로 되어있다.

## add / commit / push

- add : 커밋할 목록에 추가

- commit : 커밋 (create a snapshot) 만들기

- push : 현재까지의 역사 (commits) 가 기록되어 있는 곳에 새로 생성한 커밋들 반영하기

- 쥬피터 노트북을 쓰면 안됨.

- Git == Github 업로드해서 관리해주는 서비스이기에 아님.

 git config --global user.name

 git config --global user.email

TIL -> TODAY I LEARNED

touch git.md

# GIT

1.GIT 시작하기

```sh
$ git init
```

​		이제부터 해당 디렉토리를 git으로 관리하겠다.

2.상태 확인하기

```sh
$ git status스테이지에 올리기
```

3.스테이지에 올리기

```sh
$git add .
```

4.커밋하기(사진찍기)

```sh
$git commit -m '메세지'(m은 옵션)
```

5.로그 기록 확인하기

```sh
$git log
```

6.리모트(원격 저장소)등록하기(파이선 폴더랑 깃과 연결시켜줌)

```sh
$git remote add origin 원격저장소 주소
```

origin 은 그냥 폴더 이름 같은 느낌 -> shift+insert

git push-> git 로그인이 됨

7.파일 업로드하기(푸쉬하기)

```sh
$git push origin master
```

 ```sh
git config --global user.name "John"
 ```

내 이름을 알려줄 때. 모든 디렉토리에서 컨피그 없이 한 유저 이름으로 쓸 수 있음.

8.gitignore



집에서 다운받을 때

9.gitclone + clone의 url -> 집에서 쥬피터 노트북 볼 수 있음. ->없는 상태에서 다받는것

10.touch readme.md -> 파일 생성

cmd 창에서 .은 내위치 ..은 전폴더(desktop) .(파일명)은 숨김파일



최신화

git pull origin master



git remote -v : 저장되는 git의 목록을 볼 수 있음

git remote add (주소창의 이름) (url) : git 추가

git push github master -> github에 올린다/