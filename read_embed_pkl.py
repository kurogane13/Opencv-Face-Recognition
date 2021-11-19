import pickle

f=open("ref_embed.pkl","rb")
ref_dictt=pickle.load(f)
print(ref_dictt)
f.close()
