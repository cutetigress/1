import pandas as pd
data = pd.read_excel('C:/Users/LENOVO/Desktop/RightelInternet.xlsx')
question=data["assistant_question"]
yes_answer=data["user_yes_answer"]
no_answer=data["user_no_answer"]
step_yes=data["step_if_answer_is_yes"]
step_no=data["step_if_answer_is_no"]
f=data["is_answer"]
g=input("لطفا سوال خود را وارد نمایید:")
h=question.count()
f[1]=0
key1=True
while key1:
        i=0
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
            break
    
        else:
            print(question[i])
            key1=False