import math

a = ((0, 3, 1, 3, math.inf, math.inf),
     (3, 0, 4, math.inf, math.inf, math.inf),
     (1, 4, 0, math.inf, 7, 5),
     (3, math.inf, math.inf, 0, math.inf, 2),
     (math.inf, math.inf, 7, math.inf, 0, 4),
     (math.inf, math.inf, 5, 2, 4, 0))

top = 5
ribs = a[top]  # список ребер от точки
looked_top = [top]  # пройденные точки
res = [math.inf] * len(a)  # результат Дейкстры
res[top] = 0
optimal_connection = [0] * len(a)

def min_path(res, looked_top):  # получаю индекс наименьшего
    s = math.inf
    a = 0
    for i, q in enumerate(res):
        if i not in looked_top:
            if q < s:
                s = q
                a = i
    return s, a


while len(looked_top) != len(a):
    for i, q in enumerate(ribs):
        if i not in looked_top and res[i] > (ribs[i] + res[top]):
            res[i] = ribs[i] + res[top]
            optimal_connection[i] = top
    min, index = min_path(res, looked_top)
    top = index
    ribs = a[top]
    looked_top.append(top)

print(res)
print(optimal_connection)
print(looked_top)
