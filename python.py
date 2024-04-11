import random 
import subprocess
import time

def play_audio(file_path):
    subprocess.run(["afplay", file_path])

with open("/Users/baekjonghwan/Downloads/Ai/2day_word_game_problem/data/word.txt",'r',encoding='utf8') as file:
    words = [line.strip() for line in file]

print("준비? 아무 키를 입력하세요.")
input()
while 1 :
    if len(words):
        print("시작합니다")
        
        correct = 0
        start_time = time.time()
        
        for i in range(0,4) :
            random_word = random.choice(words)
            print("선택된 단어:", random_word)
            a = input()
            if random_word == a:
                print("정답입니다")
                play_audio("/Users/baekjonghwan/Downloads/Ai/2day_word_game_problem/assets/good.wav")
                correct += 1
            elif random_word != a:
                print("오답입니다")
                play_audio("/Users/baekjonghwan/Downloads/Ai/2day_word_game_problem/assets/bad.wav")
    
        end_time = time.time()
        result = end_time - start_time

    print("종료되었습니다.")
    print("게임에 걸린 시간:", int(result), "초")
    print("맞힌 수:", correct)
    
    while True:
        print("재도전?(y/n)")
        re = input()
        if re == 'y':
            break
        if re == 'n':
            exit()
        else:
            print("잘못 입력하셨습니다")
  
