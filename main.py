import inquirer
from bestsellers import *
from memory_profiler import profile

@profile
def main():
    QUESTION_1 = "Look up year range"
    QUESTION_2 = "Look up month/year"
    QUESTION_3 = "Search for author"
    QUESTION_4 = "Search for title"
    QUESTION_5 = "Quit"

    questions = [
        inquirer.List("question", message="What would you like to do?", choices=[
            QUESTION_1, QUESTION_2, QUESTION_3, QUESTION_4, QUESTION_5
        ])
    ]

    answers = inquirer.prompt(questions)
    
    if answers['question'] == QUESTION_1:
        questions = [
            inquirer.Text("start_year", message="Enter beginning year"),
            inquirer.Text("end_year", message="Enter ending year")
        ]

        answers = inquirer.prompt(questions)
        find_by_year_range("./bestsellers.txt", int(answers["start_year"]), int(answers["end_year"]))
    elif answers['question'] == QUESTION_2:
        questions = [
            inquirer.Text("month", message="Enter month (as a number, 1-12)"),
            inquirer.Text("year", message="Enter year")
        ]

        answers = inquirer.prompt(questions)
        find_by_month_year("./bestsellers.txt", int(answers["month"]), int(answers["year"]))
    
    elif answers['question'] == QUESTION_3:
        questions = [
            inquirer.Text("author", message="Enter an author's name (or part of a name)"),
        ]

        answers = inquirer.prompt(questions)
        find_by_author("./bestsellers.txt", answers["author"])
    
    elif answers['question'] == QUESTION_4:
        questions = [
            inquirer.Text("title", message="Enter a title (or part of a title)"),
        ]

        answers = inquirer.prompt(questions)
        find_by_title("./bestsellers.txt", answers["title"])
    
    elif answers['question'] == QUESTION_5:
        print("Bye!")
        exit()




if __name__ == "__main__":
    while True:
        main()

        questions = [
            inquirer.Confirm("ask", message="Do you want to continue?")
        ]

        answers = inquirer.prompt(questions)

        if not answers['ask']:
            print("Bye!")
            break

