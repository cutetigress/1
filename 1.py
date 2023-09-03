import pandas as pd
data = pd.read_excel('C:/Users/LENOVO/Desktop/RightelInternet.xlsx')
question=data["assistant_question"]
yes_answer=data["user_yes_answer"]
no_answer=data["user_no_answer"]
step_yes=data["step_if_answer_is_yes"]
step_no=data["step_if_answer_is_no"]
f=data["is_answer"]

h=question.count()
print(question[0])
for i in range(1,h):
       
        if f[i]==0:
          
            answer=input(" لطفا جواب بله یا خیر را وارد نمایید   ")
            if answer=="بله":
                count1=step_yes[i]
                print(question[count1-1])
                if f[count1-1]==0:
                    continue
                else:
                    print(question[i])
                    key1=False
                    break
                
            elif answer=="خیر":
                count1 = step_no[i]
                print(question[count1-1])
                if f[count1-1]==0:
                    continue
                else:
                    print(question[i])
                    key1=False
                    break
                
            else:
                print("enter correct answer")
                break
print("موفق باشید")