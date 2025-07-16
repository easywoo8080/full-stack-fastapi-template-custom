# 코드 스타일 가이드

## black 라이브러리를 통해 코드 스타일을 통일합니다. 

아래의 코드를 가상환경에서 실행해주세요.
이미 설치되어있을 경우 사용하시면 됩니다. 
이 패키지는 개발 환경에서만 사용되므로 꼭 --dev를 붙여주세요
```bash
uv add black --dev
```


### 사용법

```bash
# 현재 디렉토리와 모든 하위 디렉토리의 .py 파일을 변경합니다.
# 사용하지 않는 import를 제거하는 기능은 없습니다.
# 오로지 코드 스타일만 변경합니다.
black .
```


```bash
# 특정 파일만 변경을 원한다면
black <파일명>

# 예시:
# black main.py
# black src/utils/helper.py
```


## docstring

Python Coding 규칙 숙지,

## 코드 스타일
- [black](https://pypi.org/project/black/)

자유롭게 작성 후 최종 output는 `black .`으로 작업하기

## Docstring
 - PEP-257: [https://peps.python.org/pep-0257/](https://peps.python.org/pep-0257/) 
    - 참고자료 [[Python] 독스트링 (Docstrings)](https://jh-bk.tistory.com/15) 

---

### 📌 PEP 257 핵심 요약

1. **Docstring 정의**
    - Python 객체(모듈, 클래스, 함수 등)에 대한 설명을 포함하는 문자열.
    - 객체 정의 바로 아래 줄에 **삼중 따옴표(`"""`)**로 작성.
        
2. **형식 규칙**
    - **한 줄 요약**은 첫 번째 줄에 작성하며, 마침표(`.`), 물음표(`?`), 느낌표(`!`)로 끝낼 것.
    - **한 줄 요약 뒤에 공백 줄**을 추가하고, 필요 시 추가 설명을 여러 줄에 걸쳐 작성.
    - **줄바꿈된 설명은 들여쓰기 없이 좌측 정렬**로 작성.
        
3. **함수 및 메서드**
    - 무엇을 하는지 설명하며, **매개변수나 반환값에 대한 타입 설명은 선택**.
    - `"""Return the sum of x and y."""`와 같이 한 줄이면 충분한 설명은 한 줄로.
        
4. **클래스**
    - 목적 및 사용 방법 설명.
    - `__init__`의 설명은 클래스 설명에 포함하거나 따로 문서화 가능.
        
5. **모듈**
    - 모듈의 목적, 제공하는 클래스/함수/예외 설명.
    - 모듈 최상단에 docstring 위치.
        
6. **형식 스타일**
    - 문자열 시작과 종료는 항상 **삼중 따옴표 (`"""`)** 사용.
    - **명령형 문장** 사용 권장 (예: "Return", "Compute", "Raise" 등).
    - 한 줄 요약은 대문자로 시작.
        

---

### ✅ 예시

```python
def add(x, y):
    """Return the sum of x and y"""
    """ x와 y의 합을 반환합니다. """
    return x + y

class Person:
    """
    사람에 대해 표현합니다.

    Attributes:
        name: 이름.
        age: 나이.
    """
    def __init__(self, name, age):
        self.name = name
        self.age = age
```

---
