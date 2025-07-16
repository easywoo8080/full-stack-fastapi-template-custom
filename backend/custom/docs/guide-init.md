
> fastAPI 템플릿에서는 uv로 환경설정이 됨

# All-in-One

.env 설정이 올바르게 되어있다면 아래의 명령어로 실행까지 가능하다.
os는 window로 상정되어있다.
```bash
cd backend
uv sync
# os별로 가상환경 실행법이 다르다.
.\.venv\Scripts\activate
alembic upgrade head
uvicorn app.main:app --reload
```

---

# fastAPI 최초 설정 및 프로젝트 실행법
## 가상환경 셋팅
```bash
# 가상환경 패키지 관리 ( 일괄 설치 )
# pyproject.toml와 uv.lock을 가지고 가상환경을 일괄 설치합니다.
# sync는 모든 패키지 설치, uv sync --dev 개발용 별도 설치

uv sync
```

## 가상환경 실행
```bash
# 가상환경 실행(Window)
# mac은 알아서
.\.venv\Scripts\activate
```

## alembic로 최초 database 셋팅(user, item, alembic_version 테이블 생성)

```bash
# psql crete etnct uuid( 최초 1회 db생성 명령어)
# alembic
alembic upgrade head
```

> [!fail]
> 만약 alembic가 실패했을 경우 [c프로시저 어쩌구 uuid-ossp 필요해 등등] 
> 아래 코드를 db소유주 이상의 계정으로 접속하여 해당 db에 익스텐스하세요
>
>> ```sql
>> CREATE EXTENSION IF NOT EXISTS "uuid-ossp"
>> ```

## fastAPI 실행
```bash
# run fastAPI
# 파일 위치 : 메소드 명
uvicorn app.main:app --reload

```

## 기타(간단한 uv 사용법)
```bash
# 패키지 추가 명령어(자동으로 패키지 관리가 되어 앞으로 uv sync할대마다 설치 됨)
uv add {package-name}

# 임시 패키지 추가 
uv pip install {package-name}
```

