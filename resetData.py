import pickle

name = input("Name of the data file?\n")

# f = open(name+".data", 'rb')
# value = pickle.load(f)
# f.close()

# print("value in file:", value)

f = open(name+".data", 'wb')
pickle.dump(0, f)
f.close()

f = open(name+".data", 'rb')
value = pickle.load(f)
f.close()

print("value in file after reset:", value)
