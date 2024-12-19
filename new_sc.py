import pandas as pd

val = input("file name: ")
print("hmtl and css have been created")
df = pd.read_excel(val, skiprows=2, usecols=[1, 2, 3])
#df = df.fillna("")
#print(df.head())
                                                                
days_of_week = {"понедельник", "вторник", "среда",
                "четверг", "пятница", "суббота", "воскресенье"}

s = "<html>\n<head></head>\n<style>\n"
with open('style.css', 'r') as file:
    s += file.read()
s += "</style>\n<table>\n"


count = 0
for index, row in df.iterrows():
        if index > 0: break
        s += "<tr>\n"
        for col in row:
            if count == 2:
                s = s + """<th class="width">""" + str(col)
            else:
                s = s + "<th>\n" + str(col)
            s += "</th>\n"
            count += 1
        s += "</tr>\n"

for index, row in df.iterrows():
    if index > 1:
        s += "<tr>\n"
        for col in row:
            if str(col).lower() in days_of_week:
                s = s + "<td>" + str(col)
            else:
                s += "<td>\n"
                if str(col) == 'nan':
                    s += ""
                else:
                    s += str(col)
            s += "</td>\n"
        s += "</tr>\n"
s += "</table></body>\n</html>"
#print(s)
with open('spreadsheet.html', 'w') as file:
    file.write(s)


        
        


        
    


