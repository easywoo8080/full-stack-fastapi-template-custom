"""
역할:
    SQL 데이터베이스와 직접 상호작용하는 공통 데이터 접근 함수입니다.
    ORM 기반 조회뿐 아니라 필요 시 raw SQL 쿼리 실행도 담당합니다.
    데이터베이스에서 읽기(Read) 작업을 수행하며,
    DB 세션을 통해 쿼리를 실행하고 결과를 반환하는 역할을 합니다.

    즉, 애플리케이션 내에서 SQL 쿼리(ORM, raw SQL 모두 포함)를 실행하는
    공통 CRUD 처리 계층에 해당합니다.
"""

from sqlmodel import Session, select, text
from sqlmodel import Session
from typing import Any, Dict, List, Sequence, Type, Optional
from sqlmodel import SQLModel, Session, select

from .models import MyNosqlTableCode

def get_meas_data(
    *, model: Type[SQLModel], session: Session
) -> Optional[Sequence[SQLModel]]:
    statement = select(model)
    results = session.exec(statement).all()
    return results if results else None


def get_meas_data_code(*, session: Session) -> List[MyNosqlTableCode]:
    statement = select(MyNosqlTableCode)
    results = session.exec(statement).all()
    return list(results)


def get_active_users_raw(session: Session) -> List[Dict[str, Any]]:
    query = """
    SELECT id, data, meas_dtm, group_id
    FROM "MEASURE".my_nosql_table_data_filter
    ORDER BY id
    LIMIT 100
    """
    # raw SQL 실행 (execute 사용)
    result = session.execute(text(query))
    return [dict(row) for row in result]
