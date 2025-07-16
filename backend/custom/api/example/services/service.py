"""
파일명: example_service.py

설명:
    이 파일은 비즈니스 로직을 수행하는 서비스 계층의 예시 구현입니다.
    외부 모듈의 핵심 기능(caculate_add)을 호출하여 연산을 수행하며,
    API 계층과 DB 세션 사이에서 로직 처리를 담당합니다.

역할:
    - 비즈니스 로직 함수 정의 및 실행
    - 외부 서비스/모듈 함수 호출을 통한 작업 수행
    - 파라미터 수신으로 유연한 기능 제공(예: 페이징 시뮬레이션)
    - 데이터베이스 세션을 인자로 받아 필요 시 DB 작업 연계 가능
"""

from custom.api.example.services.modules.ex_module import caculate_add

from sqlmodel import Session


def select_age_add(session: Session, a: int = 1, b: int = 3) -> int:
    """
    Test function to check if the service is running.
    Parameters are accepted to simulate paging.
    """
    results = caculate_add(1, 3)
    return results
