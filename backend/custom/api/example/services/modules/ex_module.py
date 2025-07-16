from typing import Literal
import pandas as pd
from sklearn.impute import KNNImputer


def caculate_add(a: int, b: int) -> int:
    """
    두 정수의 합을 계산하는 함수

    Parameters
    ----------
    a : int
        첫 번째 정수
    b : int
        두 번째 정수

    Returns
    -------
    int
        두 정수의 합
    """
    return a + b
