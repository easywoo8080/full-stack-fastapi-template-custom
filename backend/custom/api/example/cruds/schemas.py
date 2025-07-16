"""
파일명: schemas.py

설명:
    이 파일은 API 요청(Request) 및 응답(Response)에 사용되는 데이터 구조를 정의합니다.
    각 클래스는 Pydantic의 BaseModel을 상속받으며, 유효성 검사와 직렬화/역직렬화를 자동으로 처리합니다.

    구조적으로는 VO(Value Object)와 유사하며, 값 자체에 의미를 부여하고,
    상태를 가지지 않는 불변 객체처럼 작동합니다. 다만 이 스키마는 도메인 객체가 아닌,
    외부 인터페이스(API 입출력)를 위한 용도로 사용됩니다.

주요 역할:
    - 클라이언트 입력값 검증
    - API 응답 데이터 정의
    - 문서화(OpenAPI) 자동화 지원
    - 내부 모델과 분리된 경량 데이터 전달 객체(DTO)로 사용
"""

from pydantic import BaseModel, Field
from typing import Optional
from uuid import UUID
