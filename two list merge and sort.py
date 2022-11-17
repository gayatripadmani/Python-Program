list1 = [10,20,30,40,50,60]
list2 = [5,15,25,35,36,37,40,41,65]
sorted_list = []

def merge_sorted_lists(list1, list2):

    while (list1 and list2):
        if (list1[0] <= list2[0]):
            item = list1.pop(0)
            sorted_list.append(item)
        else:
            item = list2.pop(0)
            sorted_list.append(item)

    sorted_list.extend(list1 if list1 else list2)
    return sorted_list

print (merge_sorted_lists(list1, list2))