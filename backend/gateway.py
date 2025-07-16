# parent/main.py
from fastapi import FastAPI
from app.main import app as app  # ⬅️ 기존 app
from custom.main import app as custom  # ⬅️ 커스텀 서브앱
gateway = FastAPI(
    title="Gateway",
    docs_url="/gateway/docs",  # 게이트웨이 Swagger
)


# 추가 서브앱이 있으면 계속 mount
gateway.mount("/custom", custom)


# /v1 경로에 서브앱 전체를 장착
gateway.mount("/", app)

