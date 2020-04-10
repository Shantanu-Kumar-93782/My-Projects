class Question:
    def __init__(self,questionid,correctoption,score):
        self.questionId = questionid
        self.correctoption = correctoption
        self.status = 'Not Answered'
        self.score = score


class QuestionPaper:
    def __init__(self,paperid,questionList):
        self.paperid = paperid 
        self.questionList = questionList
    
    def checkSolutions(self,dict1):
        for qus in self.questionList:
            for qid,opt in dict1.items():
                if qus.questionId == qid:
                    if qus.correctoption == opt:
                        qus.status = 'Correct'
                    else:
                        qus.status = 'Incorrect'
    def findResult(self):
        total = 0
        max_score=0
        for questions in self.questionList:
            max_score += questions.score
            if questions.status == 'Correct':
                total += questions.score
            elif questions.status == 'Incorrect':
                total -= 0.1 * questions.score
        per = (int(total)//max_score) * 100
        if per >= 80:
            return "Pass"
        else:
            return "Fail"


if __name__ == '__main__':
    count = int(input())
    questions = []            
    for i in range(count):
        qid = int(input())
        option = int(input())
        score = int(input())
        questions.append(Question(qid,option,score))
    q = QuestionPaper(12398,questions)
    answers={}
    ans = int(input())
    for i in range(ans):
        ques = int(input())
        option = int(input())
        answers.update({ques:option})
    q.checkSolutions(answers)
    for question in q.questionList:
        print(question.questionId,question.status)
    print(q.findResult())