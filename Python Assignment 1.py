#question 1

def quest1():
    n = input()
    grade = []
    students = []
    names = []

    for i in range(int(n)):
        individual = [input(), float(input())]
        students.append(individual)
        grade.append(individual[1])
    
    print(students)

    grade.sort()

    for j in students:
        if(j[1] == grade[1]):
            names.append(j[0])

    names.sort()

    for k in names:
        print(k)


#question 2

def quest2():
    def game(strn):

        for i in strn:
            if i not in list1:
                if(i in vowel):
                    kevein = kev(strn, i)
                else:
                    stuart = stu(strn, i)

        if kevin > stuart:
            print("Kevin " + str(kevin))
        elif stuart > kevin:
            print("Stuart " + str(stuart))
        else:
            print("Draw")

    def kev(strn, k):
        list1.append(k)
        kevin = strn.count(k)
        j = strn.index(k)+1
        for j in range(strn.index(k), len(strn)):
            strn2 = strn[strn.index(k):j]
            if(strn2 not in list1):
                kevin += strn.count(strn2)
        return kevin

    def stu(strn, s):
        list1.append(s)
        stuart = strn.count(s)
        j = strn.index(s)+1
        for j in range(strn.index(s), len(strn)):
            strn3 = strn[strn.index(s):j]
            if(strn3 not in list1):
                stuart += strn.count(strn3)
        return stuart

    kevin = 0
    stuart = 0
    list1 = []
    vowel = "AEIOU"
    strn = input()
    game(strn.upper())


#question 3


def quest3():
    n = int(input())
    scores = input()
    num = []
    j = 1

    for i in scores:
        if i != ' ':
            if j <= n:
                num.append(int(i))
                j += 1
            else:
                break

    maxNum = max(num)

    while maxNum in num:
        num.remove(maxNum)

    print(max(num))


while True:
    quest_num = int(input("Enter Question Number between 1-3 or 0 to exit"))
    if quest_num == 0:
        break

    if quest_num == 1:
        quest1()
    elif quest_num == 2:
        quest2()
    else:
        quest3()

