import os
os.system("cls")

# # 1.m
# students = {
#   "Ali": {"math": 90, "en": 80, "it": 85},
#   "Vali": {"math": 70, "en": 85, "it": 88}
# }

# def ortacha(students,ism):
#     bal = students[ism].values()
#     print(f"{ism}",max(bal))

# ortacha(students,"Ali")
# ortacha(students,"Vali")


# 2.m
# def sonlar(lst):
#     print("Yig'indi: ",sum(lst))
#     tartib = sorted(lst)
#     a = tartib[-2:]
#     print(a)

# list = [4, 7, 1, 9, 3, 8]
# sonlar(list)
        

# 3.m

# def tartib(d):
#     natija = sorted(d,key = d.get)
#     qisqa = natija[::-1]
#     for i in qisqa:
#         print(i,end=" ")

# d = {"a": 5, "b": 2, "c": 8, "d": 1}
# tartib(d)
    

# 5.m
# def juftlar(lst):
#     list2 = []
#     for i in lst:
#         if i%2==0:
#             list2.append(i)
#     print(list2)

# list1 = [1,2,3,4,5,6,7,8]
# juftlar(list1)


# 6.m 
# def matnlar(matn):
#     d = {}
#     for i in matn:
#         d[i]=matn.count(i)
#     print(d)
# matn = 'hello'
# matnlar(matn)


# 7.m
# def sonlar(lst):
#     lst2 = []
#     for i in lst:
#         if i not in lst2:
#             lst2.append(i)
#     print(lst2)
# lst=[1,2,2,3,4,4,5]
# sonlar(lst)


# 8.m
# ombor = [
#  {"nom":"olma","miqdor":5},
#  {"nom":"nok","miqdor":9},
#  {"nom":"gilos","miqdor":2}
# ]
# def chiqar(ombor):
#     for i in ombor:
#         if i['miqdor'] >5:
#             print(i['nom'],end=" ")
# chiqar(ombor)
        
