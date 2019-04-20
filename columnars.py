
import csv

outfileName = "genealogy-larger.tex"
outfile = file (outfileName, "w")
svgoutfileName = "genealogy-larger.html"
svgoutfile = file(svgoutfileName, "w")

mainColumn = 20

header=r"""
\documentclass[draft]{beamer}
\usepackage[orientation=portrait, size=a0, scale=1.0]{beamerposter}
%\usepackage{geometry}
\geometry{paperwidth=36in, paperheight=24in}

\setlength{\paperwidth}{42in}
\setlength{\textwidth}{40in}
\setlength{\paperheight}{30in}
\setlength{\textwidth}{28in}

\usepackage{pstricks}
\usepackage{pst-slpe}
\usepackage{pst-grad}
\usepackage{pst-node}
%\usepackage{xcolor}

\definecolor{anthropologist1}{HTML}{FFFF00}  
\definecolor{anthropologist2}{HTML}{FFFFCC}
\definecolor{anthropologist3}{HTML}{CCCC00}

\definecolor{linguist1}{HTML}{FF7F24}  
\definecolor{linguist2}{HTML}{FFD700} % FFA07A
\definecolor{linguist3}{HTML}{FFA07A}
\definecolor{linguist-line}{HTML}{D2691E}
 

\definecolor{logician1}{HTML}{FF6666}  
\definecolor{logician2}{HTML}{FFE6E3}
\definecolor{logician3}{HTML}{FF0000}

\definecolor{linglog1}{HTML}{FF7F24} % for barhillel 
\definecolor{linglog2}{HTML}{FFE6E3}
\definecolor{linglog3}{HTML}{FF0000}
 
\definecolor{mathematician1}{HTML}{BCA9F5}  
\definecolor{mathematician2}{HTML}{E0ECF8}
\definecolor{mathematician3}{HTML}{0000FF}

\definecolor{philosopher1}{HTML}{00FFFF} 
\definecolor{philosopher2}{HTML}{EBFCF3}
\definecolor{philosopher3}{HTML}{269900}
 
\definecolor{phillogic1}{HTML}{00FF7F}
\definecolor{phillogic2}{HTML}{EAEAEA}

\definecolor{philpsych1}{HTML}{00FFFF}  
\definecolor{philpsych2}{HTML}{66FF66} % FFA07A
\definecolor{philpsych3}{HTML}{347C2C} 

\definecolor{psychologist1}{HTML}{66FF66}
\definecolor{psychologist2}{HTML}{EBFCF3 } % aqua (BLUE)
\definecolor{psychologist3}{HTML}{00FF00}
\definecolor{psychologist-fill3}{HTML}{00FF00}

\definecolor{sociologist1}{HTML}{FFDD00}

\definecolor{hostile}{RGB}{255 0 0 }
\definecolor{teacher}{RGB}{0 0 255}
\definecolor{colleagues}{RGB}{64 200 0}
\definecolor{influence}{RGB}{10 128 10}
\definecolor{other}{RGB}{255 255 255}
\definecolor{gestalt-fill}{RGB}{255 255 0}

\definecolor{fillcolor3}{RGB}{0 255 127}
\definecolor{russianschool}{RGB}{255, 230, 204}
\definecolor{circle}{RGB}{255, 230, 204}

\definecolor{linguist-fill1}{RGB}{255 255 0}
\definecolor{linguist-fill2}{RGB}{255 255 0}
\definecolor{linguist-fill3}{RGB}{255 255 0}
\definecolor{linguist-fill4}{RGB}{255 255 0}

\definecolor{sociologist1}{HTML}{DDFF00}  
\definecolor{sociologist2}{HTML}{DDFFCC}
\definecolor{sociologist3}{HTML}{ACCC00}
\definecolor{sociologist-line}{HTML}{D2691E}

\newrgbcolor{psychology-fill1}{ 0.0 1.0 1.0  }
\newrgbcolor{gestalt-fill} { 0.0 1.0 1.0  }

\newrgbcolor{fillcolor1}{ 0.0 1.0 1.0  }
\newrgbcolor{fillcolor2}{ 0.0 1.0 8.0  }

\definecolor{other-fill}{HTML}{D3D3D3}  
 

%-----------------------------------------------------------
% Define the column widths and overall poster size
% To set effective sepwid, onecolwid and twocolwid values, first choose how many columns you want and how much separation you want between columns
% In this template, the separation width chosen is 0.024 of the paper width and a 4-column layout
% onecolwid should therefore be (1-(# of columns+1)*sepwid)/# of columns e.g. (1-(4+1)*0.024)/4 = 0.22
% Set twocolwid to be (2*onecolwid)+sepwid = 0.464
% Set threecolwid to be (3*onecolwid)+2*sepwid = 0.708
\setlength{\paperwidth}{54in} % A0 width: 46.8in
\setlength{\paperheight}{70in} % A0 height: 33.1in
 \setlength{\topmargin}{-0.5in} % Reduce the top margin size
\usepackage{graphicx}  % Required for including images
\usepackage{booktabs} % Top and bottom rules for tables 
\begin{document}
  
\begin{frame}[t] % The whole poster is enclosed in one beamer frame
 
\psset{xunit=1.0cm,yunit=1.0cm,linewidth=3pt}
\psset{gradangle=135,gradmidpoint=0.5,framesep=6pt}  

\begin{pspicture}(0, 0)(135, 240)
 

\psset{fillstyle=solid,fillcolor=linguist-fill4,framearc=0.5}
\psset{linecolor=linguist-line}
\psset{shadow=true}
 

\psset{shadow=false}

   

"""


 

footer = """
\end{pspicture}
\end{frame}
\end{document}

"""

##                                                                        Classes      


class Entity:
        def __init__(self, name,xcoor,ycoor):
                self.data=dict()
                print 165, name, xcoor, ycoor
                print 167, name, xcoor,ycoor
                self.data["name"] = name
                self.data["xcoor"] = xcoor
                self.data["ycoor"] = ycoor
               
class Entities: 
        def __init__(self):
                self.entityList = list()
                self.entityDict = dict()
        def addEntity(self, thisEntity):
                self.entityList.append(thisEntity)
                self.entityDict[thisEntity.data["name"]] = thisEntity
class People:
        def __init__(self):
                self.peopleList = list()
                self.peopleDict = dict()
        def addPerson(self, thisPerson):
                self.peopleList.append(thisPerson)
                self.peopleDict[thisPerson.data["thisKey"]] = thisPerson
         
       
class Person:
        def __init__ (self, myRowNumber, myFirstName, myLastName,myBirthYear,myDeathYear,x, profession="linguist", myKey= ""):
               
                self.data = dict()
                self.data["firstName"] = myFirstName
                self.data["lastName"]  = myLastName
                self.data["thisKey"]   = myKey
                self.data["born"]      = int(myBirthYear)
                self.data["died"]      = myDeathYear
                self.data["rowNumber"] = myRowNumber
                self.data["xcoor"] = mainColumn
                self.data["thisKey"] = myKey
                self.data["myProfession"] = profession
                    
class Links:
        def __init__(self):
                self.linkList = list()
        def addLink(self,thisLink):
                self.linkList.append(thisLink)

class Link:
        def __init__(self, from_Person, to_Entity, angle1,arm1,offset1,angle2,arm2,offset2,thisLineColor="teacher"):
                self.data=dict()
                self.data["fromNode"] = from_Person
                self.data["toEntity"] = to_Entity
                self.data["angleA"]=angle1
                self.data["armA"]=arm1
                self.data["offsetA"]=offset1
                self.data["angleB"]=angle2
                self.data["armB"]=arm2
                self.data["offsetB"]=offset2
                self.data["myLineColor"]= thisLineColor 


##                                                                                          Beginning of program

print >>outfile, header
 
myPeople = People()
myEntities = Entities()
myLinks = Links()

##                                                                                          Read spreadsheet
with open ('everybody.csv', 'r') as infile:
        genealogies = csv.reader(infile)
        row_index = 0
        for row in genealogies:
            	print row
                if row[0] == "end":
                      
                        break
                elif row[0]== "#":
                        continue
                elif row[0]=="P":
                        print 247, row
                        p = Person(row_index, row[1],row[2],row[3],row[4],row[5],row[6])
                        if len(row[6])==0:
                                p.data["thisKey"] = p.data["lastName"]
                              
                                if len(row[3]) == 0:
                                        row[3]=1700
                                if len(row[4]) == 0:
                                        row[4]= mainColumn
                        myPeople.addPerson(p)
                        row_index += 1
                elif row[0] == "E":
                         
                        e = Entity(row[1],row[3], row[4])
                        myEntities.addEntity(e)
                elif row[0] == "L":
                        L = Link(row[1],row[2],row[3],row[4],row[5],row[6],row[7],row[8]) 
                        myLinks.addLink(L)
 
svgFormat = "<rect x=\"{0}\" y=\"{1}\" width=\"50\" height = \"50\", style=\"fill:rgb(0,0,255);stroke-width:3;stroke:rgb(0,0,0)\" /> " 
print >>svgoutfile, """<!DOCTYPE html>
<html>
<body>"""
print >>svgoutfile, "<svg width=\"2500\" height = \"2000\" >"


 
print >>outfile, "\\psset{fillstyle=gradient,gradmidpoint=.5,gradangle=45}" 
formatstring = "\\rput({0:>4},{1:<3}) {{\\rnode{{{2:13}}} {{\\psframebox[{3:25}]{{ \\begin{{tabular}}{{c}}   {4:>13} {5:<13} \\\\ {6}--{7} \\end{{tabular}} }} }} }} "
for person in myPeople.peopleList:    
        if len(person.data["thisKey"])  == 0:
                person.data["thisKey"] = person.data["lastName" ]    
        ycoor = person.data["rowNumber"]*4 + 80
        if person.data["myProfession"]=="philosopher":
                color_string = "gradbegin=philosopher1,gradend=philosopher2,linecolor=philosopher3" 
        elif person.data["myProfession"]=="psychologist":
                color_string = "gradbegin=psychologist1,gradend=psychologist2,linecolor=psychologist3" 
        elif person.data["myProfession"]=="philpsych":
                color_string = "gradbegin=philosopher1,gradend=psychologist2,linecolor=psychologist3"
        elif  person.data["myProfession"]=="sociologist":
                color_string = "gradbegin=sociologist1,gradend=sociologist2,linecolor=sociologist3"
        elif  person.data["myProfession"] in ["anthropologist","mathematician"]:
                color_string = "gradbegin=other-fill,gradend=other-fill,linecolor=white"                
        else:
                color_string = "gradbegin=linguist2,gradend=linguist1,linecolor=linguist3"       
        print >>outfile, formatstring.format(person.data["xcoor"],ycoor, person.data["thisKey"], color_string,person.data["firstName"],person.data["lastName"],person.data["born"], person.data["died" ])
        svgOut = svgFormat.format(str(float(person.data["xcoor"])*20.0), ycoor*7)
        print >>svgoutfile, svgOut
print >>svgoutfile, "</svg>" 
print >>svgoutfile, "</body>"
print >>svgoutfile, "</html>"  

print >>outfile, "% \n%Entities\n\n"
print "entities"
formatstring = "\\rput({0:>4},{1:<3}) {{\\rnode{{{2:13}}} {{\\psframebox[gradbegin=linguist2,gradend=linguist1,linecolor=linguist3]{{ \\begin{{tabular}}{{c}}   {2:>13} \end{{tabular}} }} }} }} "
for entity in myEntities.entityList:    
        color_string = "gradbegin=linguist2,gradend=linguist1,linecolor=linguist3"   
        ycoor = entity.data["ycoor"]   
        print 197, entity.data
        print >>outfile, formatstring.format(entity.data["xcoor"],entity.data["ycoor"], entity.data["name"]  )
        print            formatstring.format(entity.data["xcoor"],entity.data["ycoor"], entity.data["name"] )



angleA="angleA"
armA="armA"
offsetA="offsetA"
angleB="angleB"
armB="armB"
offsetB="offsetB"
 
 
 
 

print >>outfile, "\\psset{linearc=0.5,linecolor=teacher}"

print >>outfile, "\\psset{fillstyle=none}"

#p=Link("CIA", "Dostert",270,0,-15, 180,0,0)
#myLinks.addLink(p)
 
  

for link in myLinks.linkList:
        thisAngleA = link.data[angleA]
        thisArmA = link.data[armA]
        thisOffsetA = link.data[offsetA]
        thisAngleB = link.data[angleB]
        thisArmB = link.data[armB]
        thisOffsetB = link.data[offsetB]
        thisLineStyle = "solid"
        thisLineColor = link.data["myLineColor"]
        if thisLineColor=="postDoc":
                thisLineColor ="teacher"
                thisLineStyle = "dashed"
        formatstring = "\\ncangle[angleA={0:<3},armA={1:<4},offsetA={2:<5},angleB={3:<3},armB={4:<3},offsetB={5:<5},linecolor={6:<10},linestyle={7}]{{{8}}}{{{9}}}"
        #print >>outfile, formatstring.format(link.data[angleA],link.data[armA],link.data[offsetA],link.data[angleB],link.data[armB],link.data[offsetB],myLineColor,myLineStyle,link.data[fromNode],link.data[toNode])
        print 338, formatstring
        print >>outfile, formatstring.format(thisAngleA, thisArmA,thisOffsetA,thisAngleB, thisArmB, thisOffsetB,thisLineColor,thisLineStyle,link.data["fromNode"], link.data["toEntity"]) 
         

print >>outfile, footer
outfile.close()
