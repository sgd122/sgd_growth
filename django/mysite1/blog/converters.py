class FourDigitYearConverter:
    # regex = r"\d{4}"
    regex = r"[23]\d{3}"

    def to_python(self, value: str) -> int:  # url로부터 추출한 문자열을 뷰에 넘겨주기 전에 변환
        return int(value)

    def to_url(self, value: int) -> str:  # url reverse 시에 호출
        return "%04d" % value