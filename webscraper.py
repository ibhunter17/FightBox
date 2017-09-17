import requests
from bs4 import BeautifulSoup
import pandas
def FighterData(fighter):
   ga=[]
   n={}
   r=requests.get("http://www.ufc.ca/fighter/"+fighter)
   c=r.content
   soup=BeautifulSoup(c,"html.parser")
   tablestatvalues=soup.find_all("td",{"class":"value"})
   n["Record"]=tablestatvalues[0].text
   n["Summary"]=tablestatvalues[1].text
   n["Nickname"]=tablestatvalues[2].text
   n["From"]=tablestatvalues[3].text.replace("\n","").replace("\t","")
   n["Fights Out Of"]=tablestatvalues[4].text.replace("\n","").replace("\t","")
   n["Age"]=tablestatvalues[5].text
   n["Height"]=tablestatvalues[6].text
   n["Weight"]=tablestatvalues[7].text
   maxstats=soup.find_all("div",{"class":"max-number"})
   print(maxstats)
   maxstrikes = soup.find_all("div", {"id": "total-takedowns-number"})
   maxsstandingstrike = soup.find_all("div", {"class": "text-bar red-text-bar right-border"})
   maxclinchingstrike = soup.find_all("div", {"class": "text-bar dark-red-text-bar right-border"})
   maxgroundstrike = soup.find_all("div", {"class": "text-bar grey-text-bar"})
   percentsuccess=soup.find_all("div",{"id":"total-takedowns-number"})
   strikingdefense = soup.find_all("div", {"id": "striking-defense-pecentage"})
   takedowndefense = soup.find_all("div", {"id": "takedown-defense-percentage"})
   print(percentsuccess)
   n["MaxStrikesAttempted"]=int(maxstats[0].text)
   n["SuccesfulTotalStrikes"]=int(maxstrikes[0].text)
   n["SuccesfulStandingStrikes"]=int(maxsstandingstrike[1].text.replace("\n",""))
   n["SuccesfulClinchingStrikes"]=int(maxclinchingstrike[0].text.replace("\n",""))
   n["SuccesfulGroundStrikes"]=int(maxgroundstrike[0].text.replace("\n",""))
   n["StandingStrikePercentage"]="{0:.0f}%".format((n["SuccesfulStandingStrikes"]/n["SuccesfulTotalStrikes"])*100)
   n["StandingClinchingPercentage"]="{0:.0f}%".format((n["SuccesfulClinchingStrikes"]/n["SuccesfulTotalStrikes"])*100)
   n["StandingGroundPercentage"]="{0:.0f}%".format((n["SuccesfulGroundStrikes"]/n["SuccesfulTotalStrikes"])*100)
   n["StrikeLandedPercentage"]="{0:.0f}%".format((n["SuccesfulTotalStrikes"]/n["MaxStrikesAttempted"])*100)
   n["MaxTakedownsAttempted"]=int(maxstats[2].text)
   n["TotalTakedownsSuccesful"]=int(maxstrikes[1].text)
   n["SuccesfulSubmissions"]=int(maxsstandingstrike[3].text.replace("\n",""))
   n["SuccesfulPasses"]=int(maxclinchingstrike[1].text.replace("\n",""))
   n["SuccesfulSweeps"]=int(maxgroundstrike[1].text.replace("\n",""))
   n["Figther Name"]=fighter
   n["StrikingDefensePercentage"]="{0:.0f}%".format(int(strikingdefense[0].text.replace("\n","").replace(" ","").replace('%','')))
   n["TakedownDefensePercentage"] = "{0:.0f}%".format(int(takedowndefense[0].text.replace("\n", "").replace(" ", "").replace('%', '')))
   ga.append(n)
   return ga
