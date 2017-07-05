class StringOpreation:
    def letterOcrence(self):
        str1 = raw_input("Enter a random String : ")
        letter=raw_input("Enter a Letter to check the occurrence :")
        print "Given Letter is accured "+ str(str1.count(letter,0,len(str1)))+" times"
    def letterOcrence1(self):
        str2 = raw_input("Enter a random String : ")
        subStr=raw_input("Enter a Letter to check the occurrence :")
        for i in range(len(str2)):
            if str2.startswith(subStr, i):
                print "start location is : "+str(i)
        print "Given Sub String is accured " + str(str2.count(subStr, 0, len(str2))) + " times"
    def letterOccurrance3(self):
        str3 = raw_input("Enter a random String : ")
        find = raw_input("Enter a word you want to replace : ")
        repl = raw_input("Enter the New word :")
        print "String after replaced : "+str3.replace(find,repl)
obj=StringOpreation()
j=0
while(j==0):
    holder=raw_input( "\n\n\n1-To check occurrences  of a Letter in a String :\n" \
      "2-To check the occurrences  of Sub String in a String :\n" \
      "3-To repalce words in a String : \n" \
      "4-Exit")
    if(holder=='1'):
        obj.letterOcrence()
    if(holder=='2'):
        obj.letterOcrence1()
    if(holder=='3'):
        obj.letterOccurrance3()
    if(holder=='4'):
        j += 1


