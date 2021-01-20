oscar = int(input())
message = ""

if oscar == 88:
    message = "Leo finally won the Oscar! Leo is happy"
elif oscar == 86:
    message = "Not even for Wolf of Wall Street?!"
elif oscar < 88 :
    message = "When will you give Leo an Oscar?"
elif oscar > 88:
    message = "Leo got one already!"

print(message)