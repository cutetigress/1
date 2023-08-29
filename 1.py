
import pandas as pd
data = pd.read_excel('C:/Users/Administrator/Desktop/RightelInternet.xlsx', header=0)
question=data["assistant_question"]
yes_answer=data["user_yes_answer"]
no_answer=data["user_no_answer"]
step_yes=data["step_if_answer_is_yes"]
step_no=data["step_if_answer_is_no"]
f=data["is_answer"]
g=input("لطفا سوال خود را وارد نمایید:")
h=question.count()
f[1]=0
for i in range(h):
    if f[i]==0:
        print(question[i])
        answer=input(" لطفا جواب بله یا خیر را وارد نمایید   ")
        if answer=="بله":
            count1=step_yes[i]
            print(question[count1])
        elif answer=="خیر":
            count1 = step_no[i]
            print(question[count1])
        else:
            print("enter correct answer")

    else:
        print(question[i])










