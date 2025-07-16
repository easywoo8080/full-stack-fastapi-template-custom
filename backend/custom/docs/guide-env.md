
# .env 환경 설정

```
# api를 호출하는 uri prefix
# 각 api 호출 엔드포인트 앞에 붙는다.
# if 엔드 포인트가 /login/get이면 실제 호출은 http://서버주소:포트/api/v1/login/get
API_V1_STR=/api/v1

# Domain
# This would be set to the production domain with an env var on deployment
# used by Traefik to transmit traffic and aqcuire TLS certificates
DOMAIN=localhost
# To test the local Traefik config
# DOMAIN=localhost.tiangolo.com

# Used by the backend to generate links in emails to the frontend
# ko : 백엔드에서 프런트엔드로의 이메일 링크를 생성하는 데 사용됩니다.
# fastAPI에서 허용하는 frountend host 주소 및 port
FRONTEND_HOST=http://localhost:5173
VITE_API_URL=http://localhost:8000
# In staging and production, set this env var to the frontend host, e.g.
# FRONTEND_HOST=https://dashboard.example.com

# Environment: local, staging, production
ENVIRONMENT=local

PROJECT_NAME="프로젝트 명"
STACK_NAME=프로젝트_명

# Backend

# CORS허용할 주소들
BACKEND_CORS_ORIGINS="http://localhost,http://localhost:5173,https://localhost,https://localhost:5173,http://localhost.tiangolo.com"
SECRET_KEY=your_secrey_key
FIRST_SUPERUSER=admin@example.com(아무거나해도 상관없는듯)
FIRST_SUPERUSER_PASSWORD=your_password(아무거나해도 상관없는듯)

# Emails
SMTP_HOST=
SMTP_USER=
SMTP_PASSWORD=
EMAILS_FROM_EMAIL=info@example.com
SMTP_TLS=True
SMTP_SSL=False
SMTP_PORT=587

# Postgres
# ko : PostgreSQL 데이터베이스 연결 정보입니다. 기본 유저 정보
POSTGRES_SERVER=server_address
POSTGRES_PORT=server_port
POSTGRES_DB=database_name
POSTGRES_USER=database_user
POSTGRES_PASSWORD=user_password

# OUTLIER_SERVER
# ko : Outlier 데이터베이스 연결 정보입니다. 이상치 관련 데이터
POSTGRES_SERVER=server_address
POSTGRES_PORT=server_port
POSTGRES_DB=database_name
POSTGRES_USER=database_user
POSTGRES_PASSWORD=user_password

SENTRY_DSN=

# Configure these with your own Docker registry images
DOCKER_IMAGE_BACKEND=backend
DOCKER_IMAGE_FRONTEND=frontend


```



# gpt

# `.env` 환경 설정 정리

## 기본 API 설정
- `API_V1_STR=/api/v1`  
  각 API 호출 엔드포인트 앞에 붙는 prefix  
  예: `/login/get` → `http://서버주소:포트/api/v1/login/get`

## 도메인 설정
- `DOMAIN=localhost`  
  Traefik에서 트래픽 전달 및 TLS 인증서 획득용  
  ※ 로컬 테스트: `localhost.tiangolo.com` 가능

## 프런트엔드 관련
- `FRONTEND_HOST=http://localhost:5173`  
  백엔드에서 이메일 링크 등 생성 시 사용
- `VITE_API_URL=http://localhost:8000`  
  프런트에서 API 호출 시 사용하는 URL

## 환경 구분
- `ENVIRONMENT=local`  
  사용 환경: local / staging / production

## 프로젝트 정보
- `PROJECT_NAME="프로젝트 명"`
- `STACK_NAME=프로젝트_명`

## CORS 설정
- `BACKEND_CORS_ORIGINS="http://localhost,http://localhost:5173,https://localhost,https://localhost:5173,http://localhost.tiangolo.com"`

## 관리자 계정
- `SECRET_KEY=nivuskorea032`
- `FIRST_SUPERUSER=admin@example.com`
- `FIRST_SUPERUSER_PASSWORD=your_password`

## 이메일 설정
- `SMTP_HOST=`
- `SMTP_USER=`
- `SMTP_PASSWORD=`
- `EMAILS_FROM_EMAIL=info@example.com`
- `SMTP_TLS=True`
- `SMTP_SSL=False`
- `SMTP_PORT=587`

## PostgreSQL (기본 DB)
- `POSTGRES_SERVER=server_address`
- `POSTGRES_PORT=server_port`
- `POSTGRES_DB=database_name`
- `POSTGRES_USER=database_user`
- `POSTGRES_PASSWORD=user_password`

## Outlier DB (이상치 관련)
- `POSTGRES_SERVER=server_address`
- `POSTGRES_PORT=server_port`
- `POSTGRES_DB=database_name`
- `POSTGRES_USER=database_user`
- `POSTGRES_PASSWORD=user_password`

## Sentry
- `SENTRY_DSN=`

## Docker 이미지
- `DOCKER_IMAGE_BACKEND=backend`
- `DOCKER_IMAGE_FRONTEND=frontend`
