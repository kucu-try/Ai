import random
from pygame import mixer  # pygame 모듈에서 mixer 가져오기
import time

# 단어 확인 함수 정의
def check_word(input_word, correct_word):
    if input_word == correct_word:
        mixer.music.load('good.wav')  # 맞을 때의 소리 파일
        mixer.music.play()
        print("맞았습니다!")
        return True
    else:
        mixer.music.load('bad.wav')  # 틀렸을 때의 소리 파일
        mixer.music.play()
        print("틀렸습니다!")
        return False

# word.txt 파일 경로 설정
word_file = "word.txt"

# word.txt 파일 열어서 단어 목록 가져오기
with open(word_file, 'r', encoding='utf8') as file:
    word_list = file.readlines()

# 공백 문자 제거
word_list = [word.strip() for word in word_list]

# 단어 목록에서 랜덤하게 선택하여 단어 생성
words = random.sample(word_list, 5)

# mixer 초기화
mixer.init()

# 정답 수 및 시작 시간 초기화
correct_count = 0
start_time = time.time()

# 각 단어에 대한 음성 출력 및 사용자 입력 처리
for word in words:
    # 단어 표시
    print(f"단어: {word}")
    # 사용자 입력 받기
    user_input = input("위 단어를 입력하세요: ")
    # 정답 확인 및 정답 수 증가
    if check_word(user_input, word):
        correct_count += 1

# mixer 종료
mixer.quit()

# 종료 시간 기록 및 걸린 시간 계산
end_time = time.time()
elapsed_time = end_time - start_time

# 결과 출력
print(f"정답 수: {correct_count}/{len(words)}")
print(f"걸린 시간: {elapsed_time:.2f}초")