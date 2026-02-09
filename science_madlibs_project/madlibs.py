#Introduction


#Gather info

#Generate Title

#Authors
def get_author():
	author = input("What's your name? ")

	#Abstract(summary of the study)
	print(f"Ah, {author}, the renowned scientist! The scientific community will be ecstatic to hear about your findings! But before your scientific journal is released, I want to ask you some questions directly. ")
	return author

author = get_author()

def study_conditions():
	noun1 = input("Enter a noun: ")
	noun2 = input("Enter a plural noun: ")
	location = input("Enter a location: ")
	adverb1 = input("Enter an adverb: ")
	tool = input("Enter a tool: ")
	pastverb = input("Enter the past tense of a verb(ex hid, disappeared, ran, exploded): ")
	return noun1, noun2, location, adverb1, tool, pastverb

noun1, noun2, location, adverb1, tool, pastverb = study_conditions()

def get_num():
	while True:
		try:
			num = int(input("Enter a number(ex 1, 2, 3, 4): "))
			break
		except ValueError:
			print("Please enter an integer. ")
	return num

num = get_num()		

def get_percentages():
	while True:
		try:
			percentage = float(input("What's your favorite number between 1 and 100?" ))
			percentage2 = float(input("What's your second favorite number between 1 and 100? "))
			break
		except ValueError:
			print("Please enter a float")
	return percentage, percentage2
percentage, percentage2 = get_percentages()

#Intro: Why the study is important
def print_intro(noun1, noun2):
	print(f"Wow, {noun2} are so important. It's a good thing you thought of measuring how a {noun1} affects them. "

		f"I want to hear more about the significant impact your study had. ")
print_intro(noun1, noun2)
def get_animal_data():
	animal = input("Enter an animal: ")
	color = input("Enter a color: ")
	material = input("Enter a material: ")
	happy_verb = input("What do you do when you're happy? Enter a verb: ")
	return animal, color, material, happy_verb
animal, color, material, happy_verb = get_animal_data()
#Methods: We used blank to measure blank
def print_methods(animal):
	print(f"Every {animal} certainly has you to thank for your contributions to their safety. They want to know  "

		f"how you did it. They've promised to be the top readers of your scientific journal when it's ready. "
		f"They also want to get some exact numbers from you. ")
print_methods(animal)
#Results: Percentage of blank showed behavior/trait
def results_data(percentage):
	correlated = percentage >= 50
	adj = input("Enter an adjective: ")
	return correlated, adj
correlated, adj = results_data(percentage)
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

#Print Methods
print("METHODS:")
print("_" * 40)
print(f"We used a {tool} to conduct 300 trials. In one of the trials, the {tool} began smoking slightly, so "

	f"that could've skewed the results. For that trial, we replaced the {tool} with a bunsen burner. " 

	f"Everything else remained consistent. We placed each of the {noun2} on a {noun1} and swung the {tool}"

	f" around in a circle {num*2} times before taking a picture and writing down the measurement.")

#Print Results
print("RESULTS: ")
print("_" * 40)
print(f"Results show that {percentage}% of {noun2} {adverb1} {pastverb[:-2]} when exposed to a {noun1}. ")
if (correlated):
	print(f"This means that there is a notable correlation there. ")
else:
	print(f"This means there isn't a strong correlation there, but the effect on the {color} {material}"
	f" situation is still extremely clear(and helpful). ")
print(f"{percentage2}% of researchers are now pushing for {noun1} {animal} saviors as a result. ")
#Add graph image generator 
