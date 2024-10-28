from matplotlib import pyplot as plt
processor_name=["intel","AMD","snapdragon","tensor"]
use=[200,100,250,50]
plt.bar(processor_name,use,color='aqua',width=0.2)
plt.xlabel("processor_name"),
plt.ylabel("number of users")
plt.title("processors users in a community")
plt.show()
