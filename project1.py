print("Quiz")

# x representing all the questions in a list
x = [["Which is a noun?", {"a":"proper noun", "b":"big noun", "c":"small noun", "d":"verb noun"}],
      ["Which is a verb?", {"a":"Bus", "b":"Go", "c":"camera", "d":"Next"}],
      ["What program is this?", {"a":"html", "b":"java", "c":"python", "d":"nodejs"}],
      ["10 x 10 is ?", {"a":"200", "b":"100", "c":"380", "d":"290"}],
      ["Which is not a verb?", {"a":"Bus", "b":"Go", "c":"come", "d":"throw"}],
      ["What type of programming language is python?", {"a":"high level", "b":"java", "c":"low level", "d":"nodejs"}],
      ["Which is a country?", {"a":"oyo", "b":"ibadan", "c":"togo", "d":"cape town"}],
      ["what is the 1st color of nigerian flag?", {"a":"yellow", "b":"Gold", "c":"cream", "d":"green"}],
      ["20 x 3 is ?", {"a":"20", "b":"30", "c":"550", "d":"60"}],
      ["1 x 1 is ?", {"a":"2", "b":"1", "c":"3", "d":"4"}],
      ]

scores = 0
for i in x:
    
    print(i)
    answer = input("Answer is option: ")

    
    if i == x[0] and answer == ("a"):
         scores += 1
         print(f'Your current scores is: {scores}')
    if i == x[1] and answer == ("b"):
         scores += 1
         print(f'Your current scores is: {scores}')
    if i == x[2] and answer == ("c"):
         scores += 1
         print(f'Your current scores is: {scores}')
    if i == x[3] and answer == ("b"):
         scores += 1
         print(f'Your current scores is: {scores}')
    if i == x[4] and answer == ("a"):
         scores += 1
         print(f'Your current scores is: {scores}')
    if i == x[5] and answer == ("a"):
         scores += 1
         print(f'Your current scores is: {scores}')
    if i == x[6] and answer == ("c"):
         scores += 1
         print(f'Your current scores is: {scores}')
    if i == x[7] and answer == ("d"):
         scores += 1
         print(f'Your current scores is: {scores}')
    if i == x[8] and answer == ("d"):
         scores += 1
         print(f'Your current scores is: {scores}')
    if i == x[9] and answer == ("b"):
         scores += 1
         print(f'Your current scores is: {scores}')
    else:
         print("You are wrong")
    
print (f'Your total score is: {scores}')
print ("DONE WITH QUIZ!!!")
# answer key (a,b,c,b,a,a,c,d,d,b)
