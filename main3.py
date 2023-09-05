import pandas as pd

data = pd.read_excel('C:/Users/Administrator/Desktop/RightelInternet.xlsx')
current_step=0
question = data.loc[current_step,"assistant_question"]
print(question)
main_key=True
while main_key:
        f = data.loc[current_step, "is_answer"]
        if f==0:
                question = data.loc[current_step+1,"assistant_question"]
                answer = input(" لطفا جواب بله یا خیر را وارد نمایید   ")
                if answer == "بله":
                        step_yes = data.loc[current_step,"step_if_answer_is_yes"]
                        question = data.loc[step_yes, "assistant_question"]
                        print(question)
                        current_step=step_yes
                elif answer == "خیر":
                        step_no = data.loc[current_step, "step_if_answer_is_no"]
                        question = data.loc[step_no, "assistant_question"]
                        print(question)
                        current_step = step_no
                else:
                        print("لطفا پاسخ صحیح را وارد کنید")
                        continue
        else:
                main_key=False
                break
print("موفق باشید به امید دیدار")