numList= []
num1= int(input('Input a number:'))
num2= int(input ('Input a second number:'))
num3= int(input ('Input a third number:'))


numList.append(num1)
numList.append(num2)
numList.append(num3)

Average= sum(numList)/len(numList)
MinList= min(numList)
MaxList= max(numList)

resultsDict= {'Average': Average, 'Minimum':MinList, 'Maximum': MaxList}

print('Average of' , numList[0], numList[1], numList[2], 1 end=' ')
print('is', resultsDict['Average'])
