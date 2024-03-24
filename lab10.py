import re
# dot - . --> Can Be everything
# \w (lowercase w) --> Matches All Characters Without Special Characters (Only A Word Character)
#  --> space, line break, line read, line feed, tabulator
# \W (UPPERCASE W) --> Matches All The Special Characters Only (Not A Word Character )
#  --> space, line break, line read, line feed, tabulator
# \d (lowercase d) --> Only The Digit Characters
# \D (UPPERCASE D) --> Everything Without Digit Characters
# \s (lowercase s) --> Space Characters Only 
# \S (UPPERCASE S) --> Everything Without Space Characters Only
# ^ --> Means Not, Ex: [^a] -> Matches Execpt "a"
# - --> Means To, Ex: [0-9] -> Matches 0 To 9 Only, [a-f] -> Matches a To f Only
# + --> Takes The Character After Ex: \d+ -> returns [5, 13, 50]
# * --> Returns All The Characters Before The Given Characters


# test = re.findall(r"\w*or", txt)
def Task1():
    mtxt=" joxr.nohre@jth.hj.se, bjox@se, adam@example.com, jox@jox@jox.com."
    Task1_print = re.findall(r"\s\w+(?:\.\w+)*@\w+\.\w+(?:\.\w+)?",mtxt)
    print("the email is ", Task1_print)

def Task2():
    htmltxt= """bla bla bla <h1>My Rubric </h1> bla bla bla. """    
    Task2_print = re.findall(r"<h1>\s*(.*?)\s*</h1>",htmltxt)
    print("the text is ", Task2_print)

def Task3():
    f = open("tabla.html",encoding="utf-8")
    txt = f.read()
    result = re.findall(r'<td class="svtTablaTime">\s*(\d+\.\d+)\s*</td>\s*<td.*?>\s*<h4.*?>\s*Simpsons\s*</h4>\s*(?:<div.*?>\s*)*<p.*?>\s*.*?(Säsong)\s(\d+).*?(\d+).*?(\d+)\.\s(.*?)\..*?\s*(Regi.*?)?\..*?\s*</p>', txt )
    for i in result:
        print('_____________________')
        print(' Tid: ', i[0])
        print(' Säsong: ', i[2]) 
        print(' Avsnitt: ', i[3], '/', i[4])
        print(' Handlingar: ', i[5]) 
Task1()
Task2()
Task3()