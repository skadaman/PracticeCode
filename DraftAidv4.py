import pandas as pd
#Create pd data frames from excel data for each position
WR=pd.read_excel('/Users/sebastiankadamany/Desktop/DraftData2016.xls',sheetname= 'WR')
RB=pd.read_excel('/Users/sebastiankadamany/Desktop/DraftData2016.xls',sheetname= 'RB')
QB=pd.read_excel('/Users/sebastiankadamany/Desktop/DraftData2016.xls',sheetname= 'QB')
TE=pd.read_excel('/Users/sebastiankadamany/Desktop/DraftData2016.xls',sheetname= 'TE')
WR['Drafted']=0
RB['Drafted']=0
QB['Drafted']=0
TE['Drafted']=0
#Show sample of each dataframe
WR.head()
RB.head()
QB.head()
TE.head()

#define your draf postition, and create a function that uses that to know when you pick

rounds=int(raw_input("How many rounds does your draft have? "))
draftposition= int(raw_input("What is your draft position? "))
teams=int(raw_input("How many teams are in your league? "))
print "OK, got it,this should help you draft."
#this loop is not right
picks=[]
roundtrack=range(1,rounds)
drafteven= teams-draftposition
for r in roundtrack:
    if r==1:
        picks.append(draftposition)
    elif r%2!=0:
        p=r*teams-(teams-draftposition)
        picks.append(p)
    else:
        pe=r*teams-(draftposition-1)
        picks.append(pe)
print "Here are your picks ", picks
#Now move through picks
totalpicks=rounds*teams
print "There are %s total picks. You will need to enter the player and position for everyone." % totalpicks
print "When its your turn I'll show you your best options, dont forget to enter your picks too."


epick=range(1,totalpicks)
for e in epick:
   if e in picks:
       print "Here are your best options by position"
       print "WRs",WR[(WR.Drafted==0)].iloc[:,[0,12,13,14,15,18]].head(1)
       print "RBs",RB[(RB.Drafted==0)].iloc[:,[0,9,10,11,13,18]].head(1)
       print "QBs",QB[(QB.Drafted==0)].iloc[:,[0,3,4,5,6,18]].head(1)
       print "TEs",TE[(TE.Drafted==0)].iloc[:,[0,12,13,14,15,18]].head(1)
       pickedname=raw_input("What player did you select?(name lastname)")
       pickedposition=raw_input("What is his position?('WR','RB','QB','TE')").upper()
       if pickedposition=="WR" and pickedname in WR.Player:
         WR[(WR.Player==pickedname)].loc['Drafted']=1
         print "Wide Reciver it is, nice pick."
       elif pd.pickedposition=="RB"and pickedname in RB.Player:
         RB[(RB.Player==pickedname)].loc['Drafted']=1
         print "Running Back, run baby run."
       elif pickedposition=="QB" and pickedname in QB.Player:
         QB[(QB.Player==pickedname)].loc['Drafted']=1
         print "QB, let that ball fly."
       elif pickedposition=="TE"and pickedname in TE.Player:
         TE[(TE.Player==pickedname)].loc['Drafted']=1
         print "A good TE can save the day."
       else:
           print "Hmm must be a Defense or a Kicker, no problem."

   else:
      pickedname=raw_input("What player did they pick? (name lastname)")
      pickedposition=raw_input("What is his position?('WR','RB','QB','TE')").upper()
      if pickedposition=="WR":
         WR[(WR.Player==pickedname)].loc['Drafted']=1
         print "Got it,next!"
      elif pickedposition=="RB":
         RB[(RB.Player==pickedname)].loc['Drafted']=1
         print "Got it,next!"
      elif pickedposition=="QB":
         QB[(QB.Player==pickedname)].loc['Drafted']=1
         print "Got it,next!"
      elif pickedposition=="TE":
         TE[(TE.Player==pickedname)].loc['Drafted']=1
         print "Got it,next!"
      else:
         print "Hmm must be a Defense or a Kicker, no problem."

print "All done. That was fun!"
