"""
파일명: static_routes.py

설명:
    이 파일은 FastAPI에서 정적(고정) 엔드포인트들을 선언하는 곳입니다.
    아이템 조회, 생성 등의 기본 CRUD API와 테스트용 고정 경로를 포함합니다.

역할:
    - 고정된 URL 경로로 API 엔드포인트를 정의
    - 사용자 권한에 따른 데이터 필터링 및 페이징 처리
    - 데이터베이스 세션과 연동한 트랜잭션 관리
    - 테스트용 별도 고정 API 엔드포인트 제공
"""

from app.api.deps import get_current_active_superuser
from fastapi import APIRouter, Depends

from ...dependencies.dep import SessionDep
from app.models import Message

from . import API_PREFIX, API_TAGS

router = APIRouter(prefix=API_PREFIX, tags=API_TAGS)


@router.get("/test01", dependencies=[Depends(get_current_active_superuser)])
def get_test(
    session: SessionDep,
    skip: int = 0,
    limit: int = 100,
) -> Message:
    """
    테스트 전용 API입니다. 이건 라우터 분리한 곳에서 밖에 없지요
    """

    print("테스트 전용 API입니다.")
    return Message(message="Item 테스트 전용 API입니다 successfully")
