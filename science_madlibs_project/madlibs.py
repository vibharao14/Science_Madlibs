#Introduction


#Gather info

#Generate Title

#Authors
print()
author = input("What's your name? ")

#Abstract(summary of the study)
print(f"Ah, {author}, the renowed scientist! The scientific community will be ecstatic to hear about your findings! But before your scientific journal is released, I want to ask you some questions directly. ")

noun1 = input("Enter a noun: ")
noun2 = input("Enter a plural noun: ")
location = input("Enter a location: ")
adverb1 = input("Enter an adverb: ")
tool = input("Enter a tool: ")
pastverb = input("Enter the past tense of a verb(ex hid, disappeared, ran, exploded): ")

while True:
	try:
		num = int(input("Enter a number(ex 1, 2, 3, 4): "))
		break
	except ValueError:
		print("Please enter an integer. ")
		

#Intro: Why the study is important
print(f"Wow, {noun2} are so important. It's a good thing you thought of measuring how a {noun1} affects them. "

	f"I want to hear more about the significant impact your study had. ")

animal = input("Enter an animal: ")
color = input("Enter a color: ")
material = input("Enter a material: ")
happy_verb = input("What do you do when you're happy? Enter a verb: ")

#Methods: We used blank to measure blank

#Results: Percentage of blank showed behavior/trait

#References: Citations to other papers


#Print Abstract
print("ABSTRACT:")
print("_" * 40)
print(f"This study shows the effect of a {noun1} on a group of {noun2} in {location}. ")
print(f"We measured {num} {noun2} using a {tool}. Our results showed that the {noun2} ")
print(f"{adverb1} {pastverb} whenever confronted with a {noun1}. ")

#Print Introduction
print("INTRODUCTION:")
print("_" * 40)
print(f"This study is one of the most important to all of humanity. Knowing about a {noun1} causing {noun2} to "

	f"{adverb1} {pastverb[:-2]} helps us save every {animal} trapped in {color} {material} containers. " 

	f"{noun2} {happy_verb} with joy whenever they see a safe {animal}.")
