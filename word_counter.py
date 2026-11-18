import string
with open('words.txt','w') as f:
    f.write("The quick brown fox jumps over the lazy dog.\n")
    f.write("The dog barks, and the fox runs away.\n")
    f.write("A quick fox is a happy fox, but the dog is not happy.\n")
    f.write("Python is fun, and python is powerful.\n")

def count_words(filename):
    try:
        with open(filename,'r') as f:
            content=f.read()
            content=content.lower()
        
            my_words=content.split()
        # print(my_words)
            my_dict={}
            for x in my_words:
                x=x.strip(string.punctuation)
                if x in my_dict:
                    my_dict[x]+=1
                else:
                    my_dict[x]=1
        return my_dict
    except FileNotFoundError:
        print("The file does not exist")
       
            


result=count_words('words.txt')
# print(result)
if result != None:
    sorted_dict=dict(sorted(result.items(),key=lambda pair:pair[1],reverse=True))
# print(sorted_dict)
    with open('counts.txt','w') as g:
        for x,y in sorted_dict.items():
            g.write(f"{x}: {y}\n")
        