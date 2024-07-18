# ++++++++++++++++++++++++++++++++++++++++++ headers +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

import clr
import sys
from h2pl import *
clr.AddReference('System')
clr.AddReference('System.Windows.Forms')
clr.AddReference('System.Drawing')
from System.Windows.Forms import *
from System.Drawing import *
from System import *
from h2pl.macro import *
from System import DateTime
print    """ A program  for the calculation of Mean for WetSpass project
'Author Khodayar Abdollahi   <kabdolla@vub.ac.be>,
Dept. of Hydrology and Hydraulic Engineering, Vrije Universiteit Brussel
(c) 2011
"""

class MeanCalc():
    def __init__(self):
       pass
    class Model(Form):
#       | <=required indentation 
         
        def __init__(self):
         #A function to load GUI
          self.loadpage()          
  
        def DoSomething(self, sender, e):
            try:
                 if len(self.Tboxworkingdir.Text)<1:
                      raise Exception("What folder? Working directory is empty." ) 
                
                 currenstep=int(self.Tboxstarttimestep.Text)
                 finaltimstep=int(self.Tboxendtimestep.Text)
                 self.gotError=False
                 curPeriodNo=0
                 #curPeriodNo=self.TxtFirstStepNo.Text           
           
                 while currenstep < finaltimstep+1 and self.gotError==False:               
                
                     self.Sumup(currenstep) 
                     print "Processing started for time step "+str(currenstep)
               
                     currenstep=currenstep+1
            
                 print "Stat has been run successfully!"
                 MessageBox.Show("statistics has been run successfully!"+'\n' +"To see the results check  output  "+'\n' + self.Tboxworkingdir.Text+"\\"+self.TxtSimulations.Text)
            except Exception, exceptionObject: 
                  MessageBox.Show(exceptionObject.Message.ToString() +'\n' +'Line ' + str(sys.exc_info()[-1].tb_lineno) + '\n'+ "failed to finish the job")
                  return
            finally:
                 pass    
            
            
        def EditMyself(self, sender, e):
                showeditor("")
        def ButworkdirClick(self, sender, e):
                self.folderBrowserDialog1 = FolderBrowserDialog()
                if self.folderBrowserDialog1.ShowDialog() == DialogResult.OK:                    
                   self.Tboxworkingdir.Text= self.folderBrowserDialog1.SelectedPath                   
                else:
                       print "Note there is no folder ...\\inputs\\maps\\ in selected directory!"                 
        def  Sumup(self,ii):
           try:
                    i=str(ii)
                    if ii==1:
                         report(self.Tboxworkingdir.Text+"\\"+self.TxtSimulations.Text,"Running at "+DateTime.Now.ToString()+ " ")
                         self.linData="No"+"\t"+"rain"+"\t"+"wind"+"\t"+"pet"+"\t"+"temp"+"\t"+"gwdepth"+"\t"+"lai"
                         report(self.Tboxworkingdir.Text+"\\"+self.TxtSimulations.Text,self.linData)
                         
                    workingdir(self.Tboxworkingdir.Text+"\\") 
                    
                    if(IO.File.Exists(self.Tboxworkingdir.Text+"\\rain\\rain"+i+".asc")== True):
                        rastermap(self.Tboxworkingdir.Text+"\\rain\\rain"+i+".asc","rain"+i)
                        X1=cal("MEAN(rain"+i+")")
                    else:
                        X1="?"
                        
                    if(IO.File.Exists(self.Tboxworkingdir.Text+"\\wind\\wind"+i+".asc")== True):
                        rastermap(self.Tboxworkingdir.Text+"\\wind\\wind"+i+".asc","wind"+i)
                        X2=cal("MEAN(wind"+i+")")
                    else:
                        X2="?"
                        
                    if(IO.File.Exists(self.Tboxworkingdir.Text+"\\pet\\pet"+i+".asc")== True):
                        rastermap(self.Tboxworkingdir.Text+"\\pet\\pet"+i+".asc","pet"+i)
                        X3=cal("MEAN(pet"+i+")")
                    else:
                        X3="?" 
                        
                    if(IO.File.Exists(self.Tboxworkingdir.Text+"\\temp\\temp"+i+".asc")== True):
                        rastermap(self.Tboxworkingdir.Text+"\\temp\\temp"+i+".asc","temp"+i)
                        X4=cal("MEAN(temp"+i+")")
                    else:
                        X4="?"                        
                    
                    if(IO.File.Exists(self.Tboxworkingdir.Text+"\\gwdepth\\gwdepth"+i+".asc")== True):
                        rastermap(self.Tboxworkingdir.Text+"\\gwdepth\\gwdepth"+i+".asc","gwdepth"+i)
                        X5=cal("MEAN(gwdepth"+i+")")
                    else:
                        X5="?" 
                        
                    if(IO.File.Exists(self.Tboxworkingdir.Text+"\\lai\\lai"+i+".asc")== True):
                        rastermap(self.Tboxworkingdir.Text+"\\lai\\lai"+i+".asc","lai"+i)
                        X6=cal("MEAN(wind"+i+")")
                    else:
                        X5="?"                         
                    
                    self.linData=i+"\t"+X1+"\t"+X2+"\t"+X3+"\t"+X4+"\t"+X5
                    report(self.Tboxworkingdir.Text+"\\"+self.TxtSimulations.Text,self.linData)
                    
   
 
           except Exception, exceptionObject:                
                  MessageBox.Show(exceptionObject.Message.ToString() +'\n' +'Line ' + str(sys.exc_info()[-1].tb_lineno) + '\n'+ "ERROR in aggregation of MAPS!")
                  raise Exception(exceptionObject.Message.ToString()  )  
                  

                
                
        def loadpage(self):
                #Define  labelworkindir
                self.labelworkindir = Label()
                self.labelworkindir.Font = Drawing.Font("Microsoft Sans Serif", 9, Drawing.FontStyle.Bold, Drawing.GraphicsUnit.Point, 0)
                self.labelworkindir.Location = Point(8, 4)
                self.labelworkindir.Name = "labelworkindir"
                self.labelworkindir.Size = Drawing.Size(250, 23)
                self.labelworkindir.Text = "WetSpass '~\\inputs\\maps\\'  directory:"            
                self.Controls.Add(self.labelworkindir)
                #Define  Tboxworkingdir
                self.Tboxworkingdir = TextBox()
                self.Tboxworkingdir.Location = Point(82, 34)
                self.Tboxworkingdir.Name = "Tboxworkingdir"
                self.Tboxworkingdir.Size = Drawing.Size(350, 20)
                self.Tboxworkingdir.Text=""
                self.Controls.Add(self.Tboxworkingdir)
                 #< Define  butworkingdir
                self.butworkingdir = Button()   
                self.butworkingdir.Location = Point(435, 34)
                self.butworkingdir.Name = "butworkingdir"
                self.butworkingdir.Size = Drawing.Size(30, 23)
                self.butworkingdir.Text = "..."
                self.butworkingdir.UseVisualStyleBackColor = True
                self.butworkingdir.Click += self.ButworkdirClick
                self.Controls.Add(self.butworkingdir) 
                        
                #Define the first button
                self.butDoSomthing = Button()                
                self.butDoSomthing.BackgroundImageLayout = ImageLayout.None
                self.butDoSomthing.Location = Point(350, 80)
                self.butDoSomthing.Name = "butDoSomthing"
                self.butDoSomthing.Size = Drawing.Size(100, 25)
                self.butDoSomthing.Text = "Start"
                self.butDoSomthing.Click += self.DoSomething
                self.Controls.Add(self.butDoSomthing) 
                
                #Define the second button              
                self.butEditme = Button()                
                self.butEditme.BackgroundImageLayout = ImageLayout.None
                self.butEditme.Location = Point(350, 115)
                self.butEditme.Name = "butEditme"
                self.butEditme.Size = Drawing.Size(100, 25)
                self.butEditme.Text = "Edit Me!"
                self.butEditme.Click += self.EditMyself 
                self.Controls.Add(self.butEditme) 
                
                #< Page object>  labelNoOfTimeSteps
                self.labelNoOfTimeSteps = Label()
                self.labelNoOfTimeSteps.Font = Drawing.Font("Microsoft Sans Serif", 9, Drawing.FontStyle.Bold, Drawing.GraphicsUnit.Point, 0)
                self.labelNoOfTimeSteps.Location = Point(8, 150)
                self.labelNoOfTimeSteps.Name = "labelNoOfTimeSteps"
                self.labelNoOfTimeSteps.Size = Drawing.Size(129, 23)
                self.labelNoOfTimeSteps.Text = "Result file:"
                self.Controls.Add(self.labelNoOfTimeSteps) 
                #< Page object>  Tboxnooftimsteps
                self.TxtSimulations = TextBox()
                self.TxtSimulations.Location = Point(182, 150)
                self.TxtSimulations.Name = "Tboxnooftimsteps"
                self.TxtSimulations.Size = Drawing.Size(80, 20)
                self.TxtSimulations.Text="Summery.txt"
                self.Controls.Add(self.TxtSimulations) 


                #< Page object>  labelStartTimeSteps
                self.labelStartTimeSteps = Label()
                self.labelStartTimeSteps.Font = Drawing.Font("Microsoft Sans Serif", 9, Drawing.FontStyle.Bold, Drawing.GraphicsUnit.Point, 0)
                self.labelStartTimeSteps.Location = Point(8, 184)
                self.labelStartTimeSteps.Name = "labelStartTimeSteps"
                self.labelStartTimeSteps.Size = Drawing.Size(129, 23)
                self.labelStartTimeSteps.Text = "Starting time step:"
                self.Controls.Add(self.labelStartTimeSteps) 
                
                #< Page object>  Tboxstarttimestep
                self.Tboxstarttimestep = TextBox()
                self.Tboxstarttimestep.Location = Point(182, 184)
                self.Tboxstarttimestep.Name = "Tboxstarttimestep"
                self.Tboxstarttimestep.Size = Drawing.Size(50, 20)
                self.Tboxstarttimestep.Text="1"
                self.Controls.Add(self.Tboxstarttimestep)
                 
                
                #< Page object>  Tboxendtimestep
                self.Tboxendtimestep = TextBox()
                self.Tboxendtimestep.Location = Point(182, 218)
                self.Tboxendtimestep.Name = "Tboxendtimestep"
                self.Tboxendtimestep.Size = Drawing.Size(50, 20)
                self.Tboxendtimestep.Text="48"
                self.Controls.Add(self.Tboxendtimestep)
                
                #< Page object>  labelFinalTimeSteps
                self.labelFinalTimeSteps= Label()
                self.labelFinalTimeSteps.Font = Drawing.Font("Microsoft Sans Serif", 9, Drawing.FontStyle.Bold, Drawing.GraphicsUnit.Point, 0)
                self.labelFinalTimeSteps.Location = Point(8, 218)
                self.labelFinalTimeSteps.Name = "labelFinalTimeSteps"
                self.labelFinalTimeSteps.Size = Drawing.Size(129, 23)
                self.labelFinalTimeSteps.Text = "Final time step:"
                self.Controls.Add(self.labelFinalTimeSteps)
               #============Form====================== 
                  
                # And finally what is MainForm

                self.Size = Size(480, 320)
                self.allowclose=0
                self.MinimizeBox = 1
                self.ShowInTakbar = 0
                self.FormBorderStyle = FormBorderStyle.Sizable
                self.GetStayOnTop = 1 
                rootpath=IO.Path.GetFileNameWithoutExtension( Application.ExecutablePath)     
                self.Icon= Icon(rootpath+"\\"+rootpath+".ico")
                self.Name = "Mean"
                self.Text = "MeanCalc: Summarize input maps. Empowered  by H2PL framework!" 
               
MeanCalcPage=MeanCalc.Model().Show()
print    "Hi, this is the first exprience with H2PL"

