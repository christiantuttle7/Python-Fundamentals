grades = [ [23,45,88], 99, [100, [101, 40], 34, 56], 14, 16, 19]
grades2 = [1,2,3,4,5,6]

def find_max_grade(grades):
    max = 0
    for grade in grades:
        if(type(grade) == type([])):
            ans = find_max_grade(grade)
            if(ans > max):
                max = ans
        elif(grade>max):
            max = grade
        
        
    return max

answer=find_max_grade(grades)
print(answer)