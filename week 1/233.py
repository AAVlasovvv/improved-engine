f1 = open('input.txt', 'r')
L2 = f1.read()

A = list(L2)

L = []
GL = ['а', 'у', 'о', 'ы', 'и', 'э', 'я', 'ю', 'ё', 'е']
SG = ['б', 'в', 'г', 'д', 'ж', 'з', 'й', 'к', 'л', 'м', 'н', 'п', 'р', 'с', 'т', 'ф', 'х', 'ц', 'ч', 'ш', 'щ', 'ь', 'ъ']
L.append(A[0])
for i in range(1,len(A)):
    if (A[i-1] in SG) and (A[i] in GL):
        L.append(A[i] +'c' + A[i])
    else:
        L.append(A[i])
print(''. join(L))