def readAllInput():
    f = open("input", "r")
    return f.read().splitlines()

def parseGroups(allInputs):
    result = []
    group = []

    for input in allInputs:

        if input == '':
            result.append(group)
            group = []
        else:
            group.append(input)

    return result

def countQuestions(allGroups):
    result = 0
    for group in allGroups:
        allQuestions = ""
        for person in group:
            allQuestions = allQuestions + person

        print(allQuestions)
        numDistinctQuestions = len(''.join(set(allQuestions)))

        
        result = result + numDistinctQuestions

    return result

def countQuestionsEveryoneSaidYes(allGroups):
    result = 0
    # Iterate through groups
    for group in allGroups:
        
        # Get the first person in each group so that we can check their questions
        firstPerson = group[0]

        # Iterate through every question for the first person
        for questionFirstPersonSaidYes in firstPerson:

            # Keep track of how many people answered yes to the question
            count = 0

            # Iterate through every person in the group again
            for person in group:

                # If the question is in the person, then count it
                if questionFirstPersonSaidYes in person:
                    count = count + 1
            
            # If the count is equal to the number of people in the group, add it to our result
            if count == len(group):
                result = result + 1
        
    return result

if __name__ == "__main__":
    allInputs = readAllInput()
    allInputs.append('')

    listOfGroups = parseGroups(allInputs)

    # numQuestions = countQuestions(listOfGroups)
    
    print(countQuestionsEveryoneSaidYes(listOfGroups))
    