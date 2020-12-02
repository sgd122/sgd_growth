import os, sys, base64

# module    : 파이썬 소스파일
import lib1

print(lib1.mysum(1, 2))

# from lib1 import * # 절대 하지 말아야 할 행위
# 나중에 장고 settings 설정을 오버라이딩 할 때만 사용

# package   : 파이썬 소스코드가 들어있는 디렉토리
import lib2

print(lib2.mysum(1, 2))
