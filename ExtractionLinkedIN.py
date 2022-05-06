from bs4 import BeautifulSoup

with open("abhi.html", encoding="utf8") as fp:
    soup = BeautifulSoup(fp, 'html.parser')



#Panel Intro
PanelIntro = soup.find('div', {'class': 'mt2 relative'})


#Nom prénom
nomprenom_= PanelIntro.find("h1")
nomprenom = nomprenom_.get_text().strip()
print("nombre",nomprenom)

#Titre post
works_at_loc = PanelIntro.find("div", {'class': 'text-body-medium'})
works_at = works_at_loc.get_text().strip()
print("work",works_at )

#Localisation
location_loc = PanelIntro.find("span", {'class': 'text-body-small inline t-black--light break-words'})
location= location_loc.get_text().strip()
print("location",location)

#Cordonnées

#Infos (Description)
#Expérience
#Panel Intro
PanelExperience = soup.findAll('a', {'data-field': 'experience_company_logo'})

print("PanelExperience", PanelExperience)

#ember857

#Formation

#Bénévolat
#Compétence
#Licences et certification
#Langues
