# Dashboard > Python > Basic Data Types > Finding the percentage
if __name__ == '__main__':
    
    n = int(input())
    avg = 0.0
    student_marks = {}
    
    for _ in range(n):
        name, *line = input().split()
        scores = list(map(float, line))
        student_marks[name] = scores
    
    query_name = input()
    
    for _ in range(len(scores)):
        avg += student_marks[query_name][_]
    
    avg = avg / float(len(scores))
    print("%.2f" % avg)
