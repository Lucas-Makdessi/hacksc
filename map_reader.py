import pickle


dic = pickle.load(open("data_set.txt", 'rb'))

for key, value in dic.items():
    print("Entry: ", end="")
    print(key, value)


