############################
#   Remy Rasmus Koptelkov  #
#Ülesanne09


import datetime
kuud=["jaanuar","veebruar","märts"]
aeg = datetime.datetime.now()
print(aeg.strftime("%d.%B %Y "))

print(aeg.strftime("%d.")+kuud[int(aeg.strftime("%m"))-1]+aeg.strftime(" %Y "))


print()

ik = "50405302345"
aasta = int("20"+ik[1]+ik[2])
kuu = int(ik[3]+ik[4])
paev = int(ik[5]+ik[6])

from datetime import datetime
start_date = datetime(int(aeg.strftime("%Y")),int(aeg.strftime("%m")),int(aeg.strftime("%d")),0,0)
end_date = datetime(aasta,kuu,paev,0,0)
difference  = end_date - start_date
difference_in_years = (difference.days + difference.seconds/86400)/365.2425
print(abs(int(difference_in_years)))