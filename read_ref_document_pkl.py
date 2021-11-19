import pickle

f=open("ref_document.pkl","rb")
ref_dictt=pickle.load(f)
print(ref_dictt)
f.close()
