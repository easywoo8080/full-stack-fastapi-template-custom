"""
파일명: api_router.py

설명:
    이 파일은 FastAPI 애플리케이션에서 여러 라우터 모듈을 통합하는 역할을 합니다.
    고정(fixed) 엔드포인트 라우터를 먼저 포함시키고, 그 다음 동적(dynamic) 엔드포인트 라우터를 포함하도록 순서를 명확히 지정합니다.

역할:
    - 여러 라우터 모듈을 한 곳에서 통합 관리
    - 라우팅 우선순위 제어: 고정 경로가 동적 경로보다 우선 처리되도록 설정
    - 애플리케이션 전체 API 경로 구조 구성
"""

from . import dynamic_router, fixed_router
from fastapi import APIRouter

router = APIRouter()
router.include_router(fixed_router.router)
router.include_router(dynamic_router.router)
