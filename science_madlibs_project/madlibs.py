#Introduction


#Gather info

#Generate Title

#Authors
print()
author = input("What's your name? ")

#Abstract(summary of the study)
print(f"Ah, {author}, the renowed scientist! The scientific community will be ecstatic to hear about your findings! But before your scientific journal is released, I want to ask you some questions directly.")

noun1 = input("Enter a noun: ")
noun2 = input("Enter a plural noun: ")
location = input("Enter a location: ")
adverb1 = input("Enter an adverb: ")
tool = input("Enter a tool: ")
while True{
	try:
		num = int(input("Enter a number(ex 1, 2, 3, 4): "))
		pastverb = input("Enter the past tense of a verb(ex hid, disappeared, ran, exploded):")
	except ValueError:
		print("Please enter an integer.")
		
}
#Intro: Why the study is important

#Methods: We used blank to measure blank

#Results: Percentage of blank showed behavior/trait

#References: Citations to other papers


#Print Abstract
print("ABSTRACT:")
print("_" *10)
print(f"This study shows the effect of a {noun1} on a group of {noun2} in {location}.")
print(f"We measured {num} {noun2} using a {tool}. Our results showed that the {noun2}")
print(f"{adverb1} {pastverb} whenever confronted with a {noun1}")


