# №3 Из писка выбрать элементы, встречающиеся в нем единожды

colection = [1, 2, 1, 3, 2, 4, 5]
# count1 = 0
# colection_one_element = []
# for i in colection:
#     count1 = colection.count(i)
#     if count1 == 1:
#         colection_one_element.append(i)
# print(colection_one_element, end=' ')
                # Второй способ через лямбда выражение и filter
res = list(filter(lambda x: colection.count(x) == 1, colection))
print(res)
