Arr1 = [10,2,43,24,58,32,63,29,98,71]
Arr2 = []
print(f'Isi Array Awal = {Arr1}')
i = len(Arr1) - 1
while i >= 0 :
  Arr2.append(Arr1[i])
  i-=1
print(f'Isi Array setelah dibalik = {Arr2}')
