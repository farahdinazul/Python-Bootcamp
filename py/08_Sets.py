flowers = {"roses", "magnolias", "peonies"}
numbers = {1,2,3,4,5}
flowers.add("lily")
print(flowers)
flowers.discard('roses')
print(flowers)
flowers.remove("magnolias")
print(flowers)

set1 = {1,2,3,4,}
set2 = {3,4,5,6}
print(set1.union(set2))
print(set2.intersection(set1))
print(set2.difference(set1))

