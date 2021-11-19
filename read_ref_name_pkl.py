import pickle

f=open("ref_name.pkl","rb")
ref_dictt=pickle.load(f)
print(ref_dictt)
f.close()
