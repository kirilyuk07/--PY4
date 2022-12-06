def delete(list_, index=-1):
    if index >= 0:
        return list_[:index] + list_[index+1:]
    else:
        return list_[-1:index:-1][::-1] + list_[index-1::-1][::-1]

print(delete([0, 1, 2], index=0))
print(delete([0, 1, 2], index=1))
print(delete([0, 1, 2]))
# пустая строка