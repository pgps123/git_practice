from random import *
En_word = []
Ko_word = []
num_list = []
succed_word = []
failure_word = []
while True:
    temp = input("영단어 입력(취소하기위해 0입력) > ")
    En_word.append(temp)
    if temp == "0":
        break
    temp = input("뜻 입력 > ")
    Ko_word.append(temp)
print("총 단어수 =", len(En_word))
while len(num_list) < len(En_word):
    num = randint(0, len(En_word) - 1)
    check = randint(0, 1)
    if num not in num_list:
        num_list.append(num)
        print("남은단어 : {0}".format(len(En_word) - len(num_list)))
        if check:
            print(En_word[num])
            temp = input("뜻 입력 > ")
            if temp == Ko_word[num]:
                print("정답!")
                succed_word.append((En_word[num], Ko_word[num]))
            else:
                print("오답! 정답은 {0}입니다.".format(Ko_word[num]))
                failure_word.append((En_word[num], Ko_word[num]))
        else:
            print(Ko_word[num])
            temp = input("영단어 입력 > ")
            if temp == En_word[num]:
                print("정답!")
                succed_word.append((En_word[num], Ko_word[num]))
            else:
                print("오답! 정답은 {0}입니다.".format(En_word[num]))
                failure_word.append((En_word[num], Ko_word[num]))
        print()

print()
print("-" * 50)
print("성공한 단어 리스트 > ", end='')
print(succed_word)
print("-" * 50)
print()
print("-" * 50)
print("실패한 단어 리스트 > ", end='')
print(failure_word)
print("-" * 50)