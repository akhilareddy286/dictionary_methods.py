# print(dir(dict))

# print(len(['clear', 'copy', 'fromkeys', 'get', 'items', 'keys', 'pop', 'popitem', 'setdefault', 'update', 'values']))

# a={1:"",2: "akhila",3: 8,4: 6.7,}
# print(a,type(a))
# a.clear()
# print(a)

# a={1:"", 2: "akhila", 3: 6, 4: 5.6,
# 5: "reddy",}
# print(a)
# a.copy()
# print(a)

# a=[50,60,70,80,90]
# b=dict.fromkeys(a)
# print(b,type(b))
# print(dict.fromkeys(a,"hello"))

# a={1: "", 2:"akhila", 3: 9, 4: 2.3,
# 5: [2,4], 6: (5,6), 7:{2,8},
# 8:{2,"reddy"}}
# print(a.get(2))
# print(a.get(10))
# print(a.pop(5))
# print(a.pop(25))
# print(a.popitem())

# a={
# 1: "hi akhila",
# 2: "welcome to josh innovations",
# 3: "for python learning"
# }
# print(a[1])
# print(a[5])  # key error


# a={1: "", 2:"akhila", 3: 9, 4: 2.3,
# 5: [2,4], 6: (5,6), 7:{2,8},
# 8:{2,"reddy"}}
# print(a[1],type(a[1]))
# print(a[3],type(a[3]))
# print(a,type(a))
# print(a.keys())
# print(a.values())
# print(a.items())

# a={1: "", 2:"akhila", 3: 9, 4: 2.3,
# 5: [2,4], 6: (5,6), 7:{2,8},
# 8:{2,"reddy"}}
# a.update({8: 'hello world'})
# print(a)
# a.update({10: 'python'})
# print(a)


a={1: "", 2:"akhila", 3: 9, 4: 2.3,
5: [2,4], 6: (5,6), 7:{2,8},
8:{2,"reddy"}}
a.setdefault(8,'hello')
print(a)
a.setdefault(10,'python')
print(a)