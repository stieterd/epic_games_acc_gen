import pickle

class biemel:

	Red = 0x10
	Green = 0x40
	Blue = 0x20

with open("object.myfile", 'wb') as writer:

	pickle.dump(biemel, writer)
	#writer.write(biemel)

with open("object.myfile", 'rb') as reader:

	boemel = pickle.load(reader)

print(hex(boemel.Red))