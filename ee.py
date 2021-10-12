import random

answer = random.randint(1,100)
limit = 1
while(limit !=-1) :
    guess = int(input(str(answer)+"     1부터 100까지의 숫자 중 하나를 고르시오 : "))
    if guess > answer :
        print(guess,"보다 더 작은 수로 다시 맞춰보세요")
        limit+=1
    elif guess < answer :
        print(guess,"보다 더 큰 수로 다시 맞춰보세요")
        limit+=1
    else :
        print("축하합니다! 정답은 ",answer, " 시도 횟수 : ",limit,"회")
        limit = -1
