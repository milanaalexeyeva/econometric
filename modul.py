myDict = {'word': "Econometrics",
'sentence': "If the implementation is easy to explain, it may be a good idea.",
'big_list': ["python", 3, "anaconda", 3.6, "jupyter", 10, "lessons", "many", 99],
'empty_list': []
}
#1,2
if not myDict['word'].isupper():
    myDict['word'] ="Applied_"+ myDict['word'].upper() 

#3
sentences = myDict['sentence'].split(" ")
sentences[2] = "Milana"
new_sentence = " ".join(sentences)
myDict['sentence'] = new_sentence

#4
for item in myDict['big_list']:
    if type(item) == str:
        print(item[0])
 #5       
sum = 0
for item in myDict['big_list']:
    if type(item) == int:
        sum+= item
print(sum)
sum1 = 0
myDict['big_list'].remove(myDict['big_list'][-1])
myDict['big_list'].append(87)
for item in myDict['big_list']:
    if type(item) == int:
        sum1+= item
print(sum1)



#7
my_list = []
count_odd = 0
count_prime = 0
for i in range(10,100):
    my_list.append(i)

for number in my_list:
    if number % 2 == 0:
        count_prime +=1
    elif number % 2 == 1:
        count_odd +=1

print(count_odd, count_prime)


for key in myDict:
    print(myDict[key])
