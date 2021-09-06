import random

print("Hello to my polish quiz")
name = input("What's your name?")
print(name, "Enjoy this quiz")

user_input = int(input("Please select a level:\n 1 for easy \n 2 for medium \n 3 for advanced "))

question_prompts = [
    "what does a dog mean?\n a) pies\n b) kot\n c) miska\n d) kon \n",
    "What does a cat mean?\n a) dom\n b) kot\n c) szafa\n d) krokodyl \n",
    "What does a horse mean?\n a) pies\n b) malpa\n c) ptak\n d) kon \n",
    "What does a home mean?\n a) kogut\n b) miska\n c) dom\n d) okno \n",
    "What does a mirror mean?\n a) ananas\n b) lustro\n c) igla\n d) dzien \n",
    "What does a window mean?\n a) okno\n b) puszka\n c) komputer\n d) drzwi \n",
    "What does a spoon mean?\n a) pies\n b) roleta\n c) widelec\n d) lyzka \n",
    "What does a book mean?\n a) szafa\n b) ksiazka \n c) biblioteka\n d) zeszyt \n",
    "What does  pink mean?\n a) czerwony\n b) rozowy\n c) zolty\n d) zielony \n",
    "What does a bowl mean?\n a) talerz\n b) kot\n c) miska\n d) garnek \n",
]
question_prompts2 = [
    "what does  abash mean?\n a) zmieszac sie\n b) utulic\n c) pogadac\n d) przypomniec \n",
    "What does  adequate mean?\n a) wszystkiego\n b) odpowiednie\n c) ogromny\n d) wystarczajacy \n",
    "What does a boondoggle mean?\n a) niemily\n b) znany\n c) przyjemny\n d) bezsensowny pomysl \n",
    "what does clairvoyant mean?\n a) slabowidzacy\n b) jasnowidzacy\n c) daltonista\n d) zadufany \n",
    "What does encompass mean?\n a) ujac\n b) zalatac\n c) ugrzasc\n d) zdac \n",
    "What does a malediction mean?\n a) ujmowanie\n b) latanie\n c) zlorzeczenie\n d) krzyczenie \n",
    "what does outwit mean?\n a) zbadac\n b) przechytrzyc\n c) zaczarowac\n d) przejrzec \n",
    "What does  spatial mean?\n a) mikroskopijny\n b) znany\n c) brzydki\n d) przestrzenny \n",
    "What does unequivocal mean?\n a) jednoznaczny\n b) jednorozec\n c) inny\n d) klopotliwy \n",
    "what does a yeoman mean?\n a) krol sredniowieczny\n b) kon ciagnacy woz\n c) gospodarz sredniorolny\n d) krolewna wdowa \n",

]
question_prompts3 = [
    "what does  abscond mean?\n a) zepsuc\n b) znalesc\n c) pogadac\n d) uciec \n",
    "What does  solicitous mean?\n a) pieczolowity\n b) smiecacy\n c) brudny\n d) wystarczajacy \n",
    "What does expurgate mean?\n a) wychodzic\n b) wyciagac\n c) cenzurowac\n d) zapominac \n",
    "what does fallacious mean?\n a) upadly\n b) zjednoczony\n c) wysportowany\n d) zwodniczy \n",
    "What does grandiloquent mean?\n a) stary\n b) pompatyczny\n c) staromodny\n d) zadbany \n",
    "What does hapless mean?\n a) niefortunny\n b) pomocny\n c) zapobiegawczy\n d) przystepny \n",
    "what does an iconoclast mean?\n a) chytry\n b) zwinny\n c) zaczarowany \n d) obrazoburca \n",
    "What does incontrovertible mean?\n a) introwertyk\n b) znany\n c) niezaprzeczalny\n d) zamkniety \n",
    "What does maudlin mean?\n a) ckliwy\n b) apatyczny\n c) inny\n d) zadbany \n",
    "what does remiss mean?\n a) remis\n b) niedbalstwo\n c) rownosc\n d) zalozenie \n",

]


class Question:
    def __init__(self, prompt, answer):
        self.prompt = prompt
        self.answer = answer


questions = [
    Question(question_prompts[0], "a"),
    Question(question_prompts[1], "b"),
    Question(question_prompts[2], "d"),
    Question(question_prompts[3], "c"),
    Question(question_prompts[4], "b"),
    Question(question_prompts[5], "a"),
    Question(question_prompts[6], "d"),
    Question(question_prompts[7], "b"),
    Question(question_prompts[8], "b"),
    Question(question_prompts[9], "c"),
]

random.shuffle(questions)

questions2 = [
    Question(question_prompts2[0], "a"),
    Question(question_prompts2[1], "b"),
    Question(question_prompts2[2], "d"),
    Question(question_prompts2[3], "b"),
    Question(question_prompts2[4], "a"),
    Question(question_prompts2[5], "c"),
    Question(question_prompts2[6], "b"),
    Question(question_prompts2[7], "d"),
    Question(question_prompts2[8], "a"),
    Question(question_prompts2[9], "c"),
]
random.shuffle(questions2)
questions3 = [
    Question(question_prompts3[0], "d"),
    Question(question_prompts3[1], "a"),
    Question(question_prompts3[2], "c"),
    Question(question_prompts3[3], "d"),
    Question(question_prompts3[4], "b"),
    Question(question_prompts3[5], "a"),
    Question(question_prompts3[6], "d"),
    Question(question_prompts3[7], "c"),
    Question(question_prompts3[8], "a"),
    Question(question_prompts3[9], "b"),
]
random.shuffle(questions3)


def run_test(questions):
    score = 0
    for question in questions:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print(name, ", you got" + str(score) + "/" + str(len(questions)) + "correct")


def run_test2(questions2):
    score = 0
    for question in questions2:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print(name, ", you got" + str(score) + "/" + str(len(questions)) + "correct")


def run_test3(questions3):
    score = 0
    for question in questions3:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print(name, ", you got" + str(score) + "/" + str(len(questions)) + "correct")


if user_input == 1:
    run_test(questions)
elif user_input == 2:
    run_test2(questions2)
elif user_input == 3:
    run_test3(questions3)