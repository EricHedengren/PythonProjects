alp = "efirxymnopqstu?cdzgh!. abjklvw"
code = "aefv @m&knszxydtghubc*wijopqrl"

message = input("What's the message: ")
newMessage = ''
for i in message:
    newMessage += code[alp.index(i)]
print(newMessage)

decode = input("Enter coded message: ")
decoded = ''
for i in decode:
    decoded += alp[code.index(i)]
print(decoded)