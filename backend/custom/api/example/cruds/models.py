"""
이 파일은 PostgreSQL MEASURE 스키마 내 데이터베이스 테이블과 매핑되는
SQLModel 기반 ORM 모델 정의를 포함합니다.

- MeasData: 측정 데이터 저장용 테이블 매핑 (복합 PK: 측정 시각, 태그 ID, 데이터 타입, 태그 그룹)
- MyNosqlTableCode: 태그 코드 및 메타데이터 관리용 테이블 매핑
- MyNosqlTableDataFilter: 이상치 필터링용 데이터 저장 테이블 매핑
- MyNosqlTable: JSONB 형식의 NoSQL 데이터 저장용 테이블 매핑

각 클래스는 필드별 데이터 타입, PK, 제약 조건을 명확히 지정해
애플리케이션에서 데이터베이스와 타입 안정성을 보장하며 연동 가능하도록 설계되었습니다.
"""

from typing import Optional, ClassVar, Dict
from sqlmodel import SQLModel, Field
from sqlalchemy import *  # type: ignore
from datetime import datetime
from sqlalchemy.dialects.postgresql import JSONB


class MeasData(SQLModel, table=True):
    __tablename__: ClassVar[str] = "meas_data"
    __table_args__: ClassVar[Dict[str, str]] = {"schema": "MEASURE"}

    meas_dtm: datetime = Field(
        sa_column=Column(TIMESTAMP, primary_key=True), description="측정 시각"
    )
    tag_id: str = Field(
        sa_column=Column(VARCHAR(100), primary_key=True), description="계측 태그 ID"
    )
    datatyp: str = Field(
        sa_column=Column(VARCHAR(10), primary_key=True), description="데이터 타입"
    )
    tag_group: str = Field(
        sa_column=Column(VARCHAR(100), primary_key=True), description="태그 그룹"
    )
    datavalue: Optional[float] = Field(
        default=None,
        sa_column=Column(Numeric(16, 4), nullable=True),
        description="측정값",
    )
    datavalid: Optional[str] = Field(
        default=None,
        sa_column=Column(CHAR(1), nullable=True),
        description="유효성 여부",
    )
    update_yn: Optional[str] = Field(
        default=None, sa_column=Column(CHAR(1), nullable=True), description="갱신 여부"
    )


class MyNosqlTableCode(SQLModel, table=True):
    # Pylance 호환을 위해 ClassVar로 타입 명시
    __tablename__: ClassVar[str] = "my_nosql_table_code"
    __table_args__: ClassVar[Dict[str, str]] = {"schema": "MEASURE"}
    id: Optional[int] = Field(
        default=None,
        primary_key=True,
        sa_column_kwargs={
            "server_default": text(
                "nextval('\"MEASURE\".my_nosql_table_id_seq'::regclass)"
            )
        },
    )
    tag_id: Optional[str] = Field(default=None, max_length=100, description="db tag id")
    tag_desc: Optional[str] = Field(
        default=None, max_length=100, description="db tag 설명"
    )
    plc_id: Optional[str] = Field(default=None, max_length=100, description="plc id")
    plc_desc: Optional[str] = Field(
        default=None, max_length=100, description="plc 설명"
    )
    plc_addr: Optional[str] = Field(
        default=None, max_length=100, description="plc 주소"
    )
    plc_panel: Optional[str] = Field(
        default=None, max_length=100, description="plc 판넬"
    )
    group_id: Optional[int] = Field(
        default=None, description="그룹 id (유입펌프장, 생물반응조 등등)"
    )
    need_filter: Optional[int] = Field(
        default=None, description="이상치 제거 대상 여부"
    )


class MyNosqlTableDataFilter(SQLModel, table=True):
    __tablename__: ClassVar[str] = "my_nosql_table_data_filter"
    __table_args__: ClassVar[Dict[str, str]] = {"schema": "MEASURE"}

    id: Optional[int] = Field(
        default=None,
        sa_column=Column(
            Integer,
            primary_key=False,
            server_default=text(
                "nextval('\"MEASURE\".my_nosql_table_data_filter_id_seq'::regclass)"
            ),
        ),
    )
    data: Optional[dict] = Field(default=None, sa_column=Column(JSONB))
    meas_dtm: datetime = Field(..., description="측정 시각")
    group_id: int = Field(..., description="my_nosql_table_code의 id", primary_key=True)


class MyNosqlTable(SQLModel, table=True):
    __tablename__: ClassVar[str] = "my_nosql_table"
    __table_args__: ClassVar[Dict[str, str]] = {"schema": "MEASURE"}

    id: Optional[int] = Field(
        default=None,
        sa_column=Column(
            Integer,
            server_default=text(
                "nextval('\"MEASURE\".my_nosql_table_id_seq'::regclass)"
            ),
        ),
    )
    data: Optional[dict] = Field(default=None, sa_column=Column(JSONB))
    meas_dtm: datetime = Field(..., description="측정 시각", primary_key=True)
    group_id: int = Field(..., description="my_nosql_table_code의 id", primary_key=True)
