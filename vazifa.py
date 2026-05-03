import os 
os.system("cls")

# 1.m
# def func(matn):
#     sozlar = matn.split()
#     sanoq = {}

#     for soz in sozlar:
#         sanoq[soz] = sanoq.get(soz, 0) + 1

#     tartiblangan = sorted(sanoq.items(), key=lambda x: x[1], reverse=True)

#     natija = [soz for soz, soni in tartiblangan[:3]]

#     return " ".join(natija)


# matn = input("text kiriting: ")
# print(func(matn))


# 2.m
# 1-usul
# students = {
#   "Ali": {"math": 90, "en": 80},
#   "Vali": {"math": 70, "en": 85}
# }
# a = students['Ali'].values()
# print(sum(a)/len(a))

# b = students['Vali'].values()
# print(sum(b)/len(b))

# 2-usul
# students = {
#   "Ali": {"math": 90, "en": 80},
#   "Vali": {"math": 70, "en": 85}
# }
# def baholar(students,ism):
#     bal=students[ism].values()
#     return sum(bal)/len(bal)

# print(baholar(students,'Ali'))
# print(baholar(students,'Vali'))


# 3.m
# ombor = [
#     {"mahsulot": "olma", "miqdor": 5},
#     {"mahsulot": "nok", "miqdor": 9},
#     {"mahsulot": "shaftoli", "miqdor": 7},
#     {"mahsulot": "anor", "miqdor": 4},
#     {"mahsulot": "banan", "miqdor": 6},
#     {"mahsulot": "uzum", "miqdor": 8},
#     {"mahsulot": "gilos", "miqdor": 2},
#     {"mahsulot": "tarvuz", "miqdor": 1},
#     {"mahsulot": "qovun", "miqdor": 3},
#     {"mahsulot": "limon", "miqdor": 5}
# ]
# def omborlar(ombor):
#     jami=0
#     for i in ombor:
#         jami+=i["miqdor"]
#     print("Umumiy mahsulotlar miqdori: ",jami)

#     tartib = sorted(ombor,key = lambda i:i["miqdor"])
#     chiq = tartib[:3]
    
#     print("Eng kam qolgan 3 ta mahsulot: ",end="")
#     for i in chiq:
#         print(i["mahsulot"],end=",")

# omborlar(ombor)

    
# 4.m
# my_dict = {
#     "t": 3,
#     "p": 1,
#     "y": 2,
#     "o": 5,
#     "h": 4,
#     "n": 6,
# }
# def tartibla(soz):
#     tartib = sorted(soz,key=soz.get)
#     for i in tartib:
#         print(i)
    
# tartibla(my_dict)



# 5.m
# def sozlar(list):
#     list2 = []
#     for i in list:
#         if i != "" and i not in list2:
#             list2.append(i)
#     print(list2)

# sozlar(["olma", "", "olma", "gilos", ""])

    