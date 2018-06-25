import itertools
items=[i for i in range(20)]
print(items[10:])
aaa=iter(items)
for i in itertools.islice(aaa,10,21,2):
    print(i)
aaa=iter(items)
for i in itertools.dropwhile(lambda x:x<10,aaa):
    print (i)
