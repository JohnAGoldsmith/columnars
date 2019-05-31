
import csv

outfileName = "genealogy.tex"
outfile = file (outfileName, "w")
svgoutfileName = "genealogy.html"
svgoutfile = file(svgoutfileName, "w")


header=r"""
\documentclass[final, 12pt]{beamer}
%\usepackage[size=custom,width=200,height=107,scale=.5,orientation=portrait]{beamerposter}
%\usepackage[scale=1.24]{beamerposter} % Use the beamerposter package for laying out the poster
\usepackage[width=36in,scale=.5,orientation=landscape]{beamerposter}

\usepackage{pst-slpe}
\usepackage{pst-grad}
\usepackage{pst-node}
\usepackage{pst-blur}
 
\definecolor{teacher}{HTML}{0000FF}  
\definecolor{hostile}{HTML}{FF0000}  
\definecolor{influence}{HTML}{808080}  
\definecolor{colleagues}{RGB}{64 200 0}
\definecolor{other}{RGB}{255 255 255} 


\definecolor{anthropologist1}{HTML}{FFB3B3}  
\definecolor{anthropologist2}{HTML}{FFE6E6}
\definecolor{anthropologist3}{HTML}{CCCC00}
 
\definecolor{linguist1}{HTML}{DBA909}  
\definecolor{linguist2}{HTML}{F8EDCB} % EDBB99
\definecolor{linguist3}{HTML}{533419}
\definecolor{linguist-line}{HTML}{D2691E}

\definecolor{linguist-fill2}{RGB}{255 255 0}
\definecolor{linguist-fill3}{RGB}{255 255 0}
\definecolor{linguist-fill4}{RGB}{255 255 0}
 
\definecolor{philosopher1}{HTML}{66FF66} 
\definecolor{philosopher2}{HTML}{EBFCF3}
\definecolor{philosopher3}{HTML}{00FF00} 
 

\definecolor{psychologist1}{HTML}{00FFFF}
\definecolor{psychologist2}{HTML}{EBFCF3} % aqua (BLUE)
\definecolor{psychologist3}{HTML}{269900}
\definecolor{psychologist-fill3}{HTML}{00FF00}
 
\definecolor{sociologist1}{HTML}{DDFF00}  
\definecolor{sociologist2}{HTML}{DDFFCC}
\definecolor{sociologist3}{HTML}{ACCC00}
\definecolor{sociologist-line}{HTML}{D2691E}

\definecolor{logician1}{HTML}{73AE9D}  
\definecolor{logician2}{HTML}{DDFFCC}
\definecolor{logician3}{HTML}{ACCC00}


 

\definecolor{linglog1}{HTML}{FF7F24} % for barhillel 
\definecolor{linglog2}{HTML}{FFE6E3}
\definecolor{linglog3}{HTML}{FF0000}
 
\definecolor{mathematician1}{HTML}{BCA9F5}  
\definecolor{mathematician2}{HTML}{E0ECF8}
\definecolor{mathematician3}{HTML}{0000FF}

 
\definecolor{other-fill}{HTML}{D3D3D3}  
 

  

%-----------------------------------------------------------
% Define the column widths and overall poster size
% To set effective sepwid, onecolwid and twocolwid values, first choose how many columns you want and how much separation you want between columns
% In this template, the separation width chosen is 0.024 of the paper width and a 4-column layout
% onecolwid should therefore be (1-(# of columns+1)*sepwid)/# of columns e.g. (1-(4+1)*0.024)/4 = 0.22
% Set twocolwid to be (2*onecolwid)+sepwid = 0.464
% Set threecolwid to be (3*onecolwid)+2*sepwid = 0.708
\setlength{\paperwidth}{54in} % A0 width: 46.8in
\setlength{\paperheight}{36in} % A0 height: 33.1in
 \setlength{\topmargin}{-0.5in} % Reduce the top margin size
\usepackage{graphicx}  % Required for including images
\usepackage{booktabs} % Top and bottom rules for tables 
\begin{document}
  
\begin{frame}[t] % The whole poster is enclosed in one beamer frame
 
\psset{xunit=1.6cm,yunit=.4cm,linewidth=3pt}
\psset{gradangle=135,gradmidpoint=0.5,framesep=6pt}  

\begin{pspicture}(-5, 80)(120, 240)
%\begin{pspicture}(-25, 80)(135, 240)
 

\psset{fillstyle=solid,fillcolor=linguist-fill4,framearc=0.5}
\psset{linecolor=linguist-line}
\psset{shadow=true}

%\psframe(13.5,140)(18.5,153) % kazan school box
%\psframe(18,162)(23,195)
%\psframe(24,162)(28,200) % moscow circle
%\psframe(29,170)(33,210)   % prague Circle
%\rput(31,206 ){\psframebox[linecolor=black,fillcolor=linguist-fill2]{\Large Prague Linguistic Circle }}

%\psframe[fillcolor=philosopher1](38,177)(49,195)   % vienna Circle
%\psframe[fillcolor=philosopher1](33,135)(47,162)   % brentano circle
%\psframe[fillcolor=philosopher1](33.5,176)(37,200)   % Polish logicians 

% Generations: ellipses
%\psellipse[fillstyle=solid,shadow=true,blur=true](6.5,80)(6,14)  %1st ellipse
%\psellipse(6.5,119)(5,12)  %2nd ellipse
%\psellipse (6.5,147)(6,13)  %3rd ellipse
%\psellipse[fillcolor=linguist-fill3,linestyle=solid](5,200)(10,20)  %sapir circle
%\psellipse[fillcolor=psychologist-fill3,linestyle=solid](58,189)(6,8)  %gestalt circle
%\psellipse[fillcolor=psychologist-fill3,linestyle=solid](68,143)(4,25)  %wundt circle


%\psset{fillcolor=linguist2}

%\rput(3.3,154 ){\psframebox[ framesep=10pt] { \Large Neogrammarians    }} 
%\rput(5,160){\psframebox[ linecolor=linguist-line,framesep=10pt]{ \LARGE Third Generation   }}
%\rput(2,112 ){\psframebox [linecolor=linguist-line,framesep=10pt]{ \LARGE Second Generation   }}
%\rput(2,85 ){\psframebox[linecolor=linguist-line,framesep=10pt,shadow=false,shadowsize=1,blur=true]{ \LARGE First Generation   }}




%\psframe[fillcolor=linguist-fill2,linestyle=none,framearc=0.5](14,212)(37,235)   % machine translation
%\psframe[fillcolor=linguist-fill2,linestyle=none,framearc=0.5](20,201)(28,225)   % machine translation
%\psframe[fillcolor=linguist-fill2,linestyle=none,framearc=0.5,shadow=false](27,212)(28.5,225)   % machine translation

%\rput(32,230 ){\psframebox{\begin{tabular}{c}{\LARGE Machine translation  }  \end{tabular}}}      
      

%\rput(2,220 ){\psframebox{\begin{tabular}{c}{\Large Sapir circle }  \end{tabular}}} 

%\psset{linecolor=linguist-line}
%\rput(19,165 ){\psframebox{\begin{tabular}{c}{\Large St Petersburg School }\\1900-1918 \end{tabular}}}
%\rput(18,144 ){\psframebox{\begin{tabular}{c}{\Large Kazan School }\\1874-1883 \end{tabular}}}
%\rput(25,165 ){\psframebox{\begin{tabular}{c}{\Large Moscow School }\\  \end{tabular}}}
%\rput(31,166 ){\psframebox{\begin{tabular}{c}{\Large Prague Circle }\\  \end{tabular}}}
%\rput(48,189 ){\psframebox[linecolor=black,fillcolor=philosopher1]{\Large Vienna Circle }}
%\rput(62,188 ){\psframebox[linecolor=black,fillcolor=psychologist3]{\Large Gestalt }}


%sociology

%\psset{gradangle=135,gradmidpoint=0.5,framesep=6pt,fillcolor=sociologist1,framearc=0.5}
%\psset{linecolor=sociologist3}
%\rput(-25,150 ){\psframebox[fillcolor=linguist-fill2,linecolor=sociologist-line,framesep=10pt,shadow=false,shadowsize=1,blur=true]{ \LARGE First Generation   }}
%\psellipse[shadow=true,fillstyle=solid](-14.8,204)(8.5,9)  %5th ellipse
%\psellipse[shadow=true,fillstyle=solid](-15,200)(8,16)  %2nd generation
%\psellipse[shadow=true,fillstyle=solid](-15,153)(8,16)  %1ST GENERATION
%\psellipse[shadow=true,fillstyle=solid](-15,120)(8,6)  %1st ellipse

\psframe[fillcolor=linguist-fill2,linestyle=none,framearc=0.5](-5,150)(25,245)   % Chicago sociology
\psframe[fillcolor=linguist-fill2,linestyle=none,framearc=0.5](27,150)(45,245)   % Columbia sociology
\psframe[fillcolor=linguist-fill2,linestyle=none,framearc=0.5](47,150)(65,245)   % Harvard sociology
%\psellipse[shadow=true,fillstyle=solid](-5,180)(10,10)  % Columbia ellipse
%\psellipse[shadow=true,fillstyle=solid](10.4,19)(3,10)  % Harvard ellipse
%\psellipse[shadow=true,fillstyle=solid](-15,160)(3,8)  % UChicago ellipse
%\psellipse[shadow=true,fillstyle=solid](-15,186)(3,4)  % bernard ogburn and chapin


%\psset{shadow=false}

   

"""


 

footer = """
\end{pspicture}
\end{frame}
\end{document}

"""

lastName = "lastName"
thisKey = "thisKey"
firstName = "firstName"
thisKey  = "thisKey"
xcoor = "xcoor"        
born = "born"
died = "died"
myLineColor = "myLineColor"
myProfession = "myProfession"

angleA="angleA"
armA="armA"
offsetA="offsetA"
angleB="angleB"
armB="armB"
offsetB="offsetB"
fromNode = "fromNode"
toNode = "toNode"


class People:
        def __init__(self):
                self.peopleList = list()
        def addPerson(self, thisPerson):
                self.peopleList.append(thisPerson)
         
       
class Person:

      
        
#        def __init__ (self, myFirstName, myLastName,myBirthYear,myDeathYear,x, profession="linguist", myKey= ""):
        def __init__ (self, facts):
                
                self.data = dict()
                for i in range(len(facts)):
                        fact = facts[i]
                        if fact[:4] == "key:":
                                self.data[thisKey] = fact[4:]
                                
                        else:
                                self.data[thisKey] = facts[2]        
                print self.data[thisKey], row, 228	
                self.data[firstName] = row[1]
                self.data[lastName] = row[2]
                self.data[born] = int(row[3])
                if len(row[4].strip()) > 0:
                        self.data[died] = int(row[4])
                else:
                        self.data[died] = ""
                self.data[xcoor] = int(row[5])
                self.data[myProfession] = row[6]
                
class Links:
        def __init__(self):
                self.linkList = list()
        def addLink(self,thisLink):
                self.linkList.append(thisLink)

class Link:
        def __init__(self, fromPerson, toPerson, angle1,arm1,offset1,angle2,arm2,offset2,thisLineColor="teacher"):
                self.data=dict()
                self.data[fromNode] = fromPerson
                self.data[toNode] = toPerson
                self.data[angleA]=angle1
                self.data[armA]=arm1
                self.data[offsetA]=offset1
                self.data[angleB]=angle2
                self.data[armB]=arm2
                self.data[offsetB]=offset2
                self.data[myLineColor]= thisLineColor 

#print header
print >>outfile, header


myPeople = People()
myLinks = Links()

with open ('genealogy.csv', 'r') as infile:
        genealogies = csv.reader(infile)
        for row in genealogies:
                #print 261, row
                if row[0]=="#":
                        continue
                p = Person(row)
                myPeople.addPerson(p)


#		if row[0].strip() == "P":
#                        print 268, row, len(row[7]), 267
#	                if len(row[7]) == 0:
#        	                p = Person(row[1],row[2],row[3],row[4],row[5],row[6])
#        	                myPeople.addPerson(p)
#                	if len(row[7] ) >0 :
#                        	p = Person(row[1],row[2],row[3],row[4],row[5],row[6],row[7])
#                        	myPeople.addPerson(p)
                               
 
 
 

#svgFormat = "<rect x=\"{0}\" y=\"{1}\" width=\"50\" height = \"50\", style=\"fill:rgb(0,0,255);stroke-width:3;stroke:rgb(0,0,0)\" /> " 
svgFormat = "<rect x=\"{0}\" y=\"{1}\" width=\"50\" height = \"50\", style=\"fill:rgb(0,0,255);stroke-width:3;stroke:rgb(0,0,0)\" /> " 
print >>svgoutfile, """<!DOCTYPE html>
<html>
<body>"""
print >>svgoutfile, "<svg width=\"2500\" height = \"2000\" >"


print >>outfile, "\\psset{fillstyle=gradient,gradmidpoint=.5,gradangle=45}" 
formatstring = "\\rput({0:>4},{1:<3}) {{\\rnode{{{2:13}}} {{\\psframebox[{3:25}]{{ \\begin{{tabular}}{{c}}   {4:>13} {5:<13} \\\\ {6}--{7} \\end{{tabular}} }} }} }} "
for person in myPeople.peopleList:    

        if len(person.data[thisKey])  == 0:
                person.data[thisKey] = person.data[lastName]
        print person.data[lastName]
        ycoor = (person.data[born] - 1700)
        thisLastName = person.data[lastName]
        thisLastName =  "\Large{\\textsc{" + thisLastName + "} }"
        if person.data[myProfession]=="philosopher":
                color_string = "gradbegin=philosopher1,gradend=philosopher2,linecolor=philosopher3" 
        elif person.data[myProfession]=="psychologist":
                color_string = "gradbegin=psychologist1,gradend=psychologist2,linecolor=psychologist3" 
        elif person.data[myProfession]=="philpsych":
                color_string = "gradbegin=philosopher1,gradend=psychologist2,linecolor=psychologist3"
        elif  person.data[myProfession]=="sociologist":
                color_string = "gradbegin=sociologist1,gradend=sociologist2,linecolor=sociologist3"
        elif  person.data[myProfession] == "anthropologist":
                color_string = "gradbegin=anthropologist1, gradend=anthropologist2,linecolor=white"                
        elif  person.data[myProfession] == "mathematician":
                color_string = "gradbegin=mathematician1,gradend=mathematician2,linecolor=white"         
        elif  person.data[myProfession] == "logician":
                color_string = "gradbegin=logician1,gradend=logician2,linecolor=white"       
                #print person.data         
        else:
                color_string = "gradbegin=linguist1,gradend=linguist2,linecolor=linguist3"       
 
        print >>outfile, formatstring.format(person.data[xcoor],ycoor, person.data[thisKey], color_string,person.data[firstName],thisLastName,person.data[born], person.data[died])
        
       
        svgOut = svgFormat.format(str(float(person.data[xcoor])*20.0), ycoor*7)
        print >>svgoutfile, svgOut


print >>svgoutfile, "</svg>" 
print >>svgoutfile, "</body>"
print >>svgoutfile, "</html>"  

angleA="angleA"
armA="armA"
offsetA="offsetA"
angleB="angleB"
armB="armB"
offsetB="offsetB"
 
 
 
 

print >>outfile, "\\psset{linearc=0.5,linecolor=teacher}"

print >>outfile, "\\psset{fillstyle=none}"


p = Link("Sorokin", "Merton",90,2,0,-90,4,0)
myLinks.addLink(p)

p = Link("Parsons", "Merton",90,0,1,-90,1,-1)
myLinks.addLink(p)

p = Link("Parsons", "Garfinkel",90,0,0,-90,1,-1)
myLinks.addLink(p)

p = Link("Parsons", "Bellah",90,0,-.5,-90,1,-1)
myLinks.addLink(p)



p = Link("GHMead", "Blumer",90,0,1,-90,7,2, "teacher")
myLinks.addLink(p)

p = Link("GHMead", "Faris",90,0,-1,180,7,0, "teacher")
myLinks.addLink(p)

p = Link("GHMead", "Cottrell",90,0,2,-90,7,0, "teacher")
myLinks.addLink(p)


p = Link("Thomas", "Blumer",90,0,1,-90,11,-1, "teacher")
myLinks.addLink(p)


p = Link("GHMead", "Wirth",90,0,0,-90,6.5,1, "teacher")
myLinks.addLink(p)

p = Link("Small", "Wirth",90,0,0,-90,11,.3, "teacher")
myLinks.addLink(p)

p = Link("Burgess", "Wirth",90,0,0,-90,2,-1, "teacher")
myLinks.addLink(p)

p = Link("Thomas", "Wirth",90,0,0,-90,7,-0.3, "teacher")
myLinks.addLink(p)
 
p = Link("Park", "Hughes",90,0,1,-90,3,0, "teacher")
myLinks.addLink(p)
 
p = Link("Park", "Blumer",90,0,0,-90,2,1, "teacher")
myLinks.addLink(p)
 
p = Link("Ogburn", "Stouffer",90,0,0,-90,1,0, "teacher")
myLinks.addLink(p)
 
p = Link("Hughes", "Goffman",90,0,1,-90,3,-1, "teacher")
myLinks.addLink(p)
 
p = Link("Warner", "Goffman",90,0,0,-90,3,0, "teacher")
myLinks.addLink(p)
 

p = Link("Hughes", "Becker",90,0,0,-90,1,0, "teacher")
myLinks.addLink(p)
 
p = Link("Goffman", "Schegloff",90,0,0,-90,3,0, "teacher")
myLinks.addLink(p)
 
p = Link("Wirth", "Shils",90,0,0,-90,2,0, "teacher")
myLinks.addLink(p)
 
p = Link("Garfinkel", "Schegloff",90,0,0,-90,1,-1, "teacher")
myLinks.addLink(p)



 
 
p = Link("Allport", "Bruner", 90,1,-.2,-90,1,.5 )
myLinks.addLink(p)

p = Link("Sapir", "Lasswell", 180,1,.4,-90,1,0, "colleagues" )
myLinks.addLink(p)

p = Link("Giddings", "Ogburn", 90,1,1,-90,4,0, "teacher" )
myLinks.addLink(p)

p = Link("Giddings", "Odum", 90,1,0.5,-90,1,0, "teacher" )
myLinks.addLink(p)

p = Link("Giddings", "Chapin", 90,1,-0.5,-90,5,0.3, "teacher" )
myLinks.addLink(p)

p = Link("Hall", "Chapin", 90,1,-0.5,-90,3,-.3, "teacher" )
myLinks.addLink(p)
  
p = Link("Small", "Bernard", 90,1,-1,-90,8,.3, "teacher" )
myLinks.addLink(p)

p = Link("Giddings", "Small", 180,0,0,00,1,0, "hostile" )
myLinks.addLink(p)

p = Link("Dewey", "Park", 1,1,0,180,1,0, "colleagues" )
myLinks.addLink(p)
  
p = Link("Dewey", "GHMead",0,1,.4,180,1,0, "colleagues" )
myLinks.addLink(p)
  
p = Link("Thomas", "Znaniecki", 0,0,0,-90,0,0, "colleagues" )
myLinks.addLink(p)



p = Link("Simmel", "Park", 0,0,0,-90,0,0, "teacher" )
myLinks.addLink(p)
  

p = Link("Lazarsfeld", "Merton", 0,0,0,  180,2,0, "colleagues" )
myLinks.addLink(p)
  

for link in myLinks.linkList:
        thisAngleA = link.data[angleA]
        thisArmA = link.data[armA]
        thisOffsetA = link.data[offsetA]
        thisAngleB = link.data[angleB]
        thisArmB = link.data[armB]
        thisOffsetB = link.data[offsetB]
        thisLineStyle = "solid"
        thisLineColor = link.data[myLineColor]
        if thisLineColor=="postDoc":
                thisLineColor ="teacher"
                thisLineStyle = "dashed"
        formatstring = "\\ncangle[angleA={0:<3},armA={1:<4},offsetA={2:<5},angleB={3:<3},armB={4:<3},offsetB={5:<5},linecolor={6:<10},linestyle={7}]{{{8}}}{{{9}}}"
        #print >>outfile, formatstring.format(link.data[angleA],link.data[armA],link.data[offsetA],link.data[angleB],link.data[armB],link.data[offsetB],myLineColor,myLineStyle,link.data[fromNode],link.data[toNode])
        print >>outfile, formatstring.format(thisAngleA, thisArmA,thisOffsetA,thisAngleB, thisArmB, thisOffsetB,thisLineColor,thisLineStyle,link.data[fromNode], link.data[toNode]) 


print >>outfile, footer
outfile.close()
