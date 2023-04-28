import statistics as stat

list = [58,62,62,63,65,65,65,68,69,72,72,75,76,78,79,81,84,84,85,92,94,95,98]
avg = stat.mean(list)
size=len(list)
med= stat.median(list)
mod=stat.mode(list)

print(avg, med, mod)
print(size)

names = ['hola','que','puto']

length = {name:len(name) for name in names}
print(length)



