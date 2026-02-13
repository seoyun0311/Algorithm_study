# 입력 : 패스워드
# 1. 모음(a e i o u) 하나 반드시 포함
# 2. 모음이 3개 연속 or 자음이 3개 연속 으로 오면 안됨
# 3. 같은 글자가 연속적으로 두번 오면 안됨
# 3-1. ee와 oo는 허용
# 출력 : 패스워드 출력 평가
# 출-1 : 1,2,3 모두 통과 시 "<입력> is acceptable." 출력
# 출-2 : 1,2,3 중에 하나라도 통과 못할 시 "<입력> is not acceptable." 출력
import sys

input = sys.stdin.readline
VOWELS = set("aeiou")

def acceptable(pw: str) -> bool:
    has_vowel = False
    streak = 0            # 연속 카운트
    prev_is_vowel = None  # 직전 문자가 모음인지 여부

    for i, ch in enumerate(pw):
        is_vowel = ch in VOWELS

        # 조건1: 모음 포함 여부
        if is_vowel:
            has_vowel = True

        # 조건3: 같은 글자 2연속 금지(ee, oo만 허용)
        if i > 0 and pw[i - 1] == ch:
            if ch not in ("e", "o"):
                return False

        # 조건2: 모음/자음 3연속 금지
        if prev_is_vowel is None or prev_is_vowel != is_vowel:
            streak = 1
            prev_is_vowel = is_vowel
        else:
            streak += 1
            if streak >= 3:
                return False

    return has_vowel

def main():
    while True:
        pw = input().strip()
        if pw == "end":
            break
        if acceptable(pw):
            print(f"<{pw}> is acceptable.")
        else:
            print(f"<{pw}> is not acceptable.")

if __name__ == "__main__":
    main()


