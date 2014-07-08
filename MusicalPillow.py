__author__='Aditya Cherla'

"""
credits to jonrsharpe@stackoverflow for the main logic.
I was writing a pretty messy code he showed the smart way. 

This is an implementation of the musical pillow problem.
The getWinner method gives the last remaining person in the circle.
You need to pass the number of the people 
"""

def getWinner(input1,input2):
	list_of_people = list(range(1,input1+1))
	#print("List of people:"+str(list_of_people))
	song_length=input2
	index = -1
	while len(list_of_people) > 1:
		index = (index + song_length) % len(list_of_people)
		del list_of_people[index]
		index -= 1

	return list_of_people[0]


if __name__ == '__main__':
	print(str(getWinner(11,4)))

