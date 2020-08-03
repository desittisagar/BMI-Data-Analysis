import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

life = pd.read_csv("life.csv")
bmi_men = pd.read_csv("bmi_men.csv")
bmi_women = pd.read_csv("bmi_women.csv")

life_exp = []
bmi_men_dict = {}
bmi_women_dict = {}

for i in range(0,186):
	life_exp.append(list(life.iloc[i,:]))								# list
	bmi_men_dict[bmi_men.loc[i][0]] = list(bmi_men.loc[i][1:])			# dict
	bmi_women_dict[bmi_women.loc[i][0]] = list(bmi_women.loc[i][1:])	# dict


#2 - making of bmi_all - avg of men and women

bmi_all = {}

for i in range(0,186):
	l1 = np.array(list(bmi_men.loc[i][1:]))
	l2 = np.array(list(bmi_women.loc[i][1:]))
	bmi_all[bmi_men.loc[i][0]] = (l1+l2)/2


bmi_all = pd.DataFrame(data = bmi_all)


#3 - min, max and median of bmi values in a user given year

while True:
	year = str(input("Select a year to find statistics (1980 to 2008): "))
	if year.isnumeric():
		pos = int(year) - 1980
		#print(min(list(bmi_all.iloc[pos,:])))
		min_val = min(list(bmi_all.iloc[pos,:]))
		max_val = max(list(bmi_all.iloc[pos,:]))
		temp_list = list(bmi_all.iloc[pos,:])
		temp_list.sort()
		min_country = ''
		max_country = ''

		for i in range(0,186):
			if min_val == bmi_all.iloc[pos,i]:
				min_country = bmi_all.columns[i]
			if max_val == bmi_all.iloc[pos,i]:	
				max_country = bmi_all.columns[i]

		print(f"In {year}, countries with minimum and maximum BMI values were '{min_country}' and '{max_country}' and Median BMI value in {year} was {round(((temp_list[92]+temp_list[93])/2.000),5)}")
		print("\n\n")
		break
	else:
		print("<error> That is an invalid year.")
		continue	


#4 - men's and women's bmi percentage difference

print("Men vs women BMI in highest population countries: \n")

y1 = 2004-1980
y2 = 2005-1980
y3 = 2006-1980
y4 = 2007-1980
y5 = 2008-1980

bmi_men_avg = round((bmi_men_dict['China'][y1]+bmi_men_dict['China'][y2]+bmi_men_dict['China'][y3]+\
				bmi_men_dict['China'][y4]+bmi_men_dict['China'][y5])/5.0,2)

bmi_women_avg = round((bmi_women_dict['China'][y1]+bmi_women_dict['China'][y2]+bmi_women_dict['China'][y3]+\
				bmi_women_dict['China'][y4]+bmi_women_dict['China'][y5])/5.0,2)


bmi_percent = round(((abs(bmi_women_avg - bmi_men_avg))/((bmi_women_avg + bmi_men_avg)/2.0)) * 100,2)

print("*** China ***")
print("Men: ",bmi_men_avg)
print("Women: ",bmi_women_avg)
print("Percent Differnce: ",bmi_percent)
print("\n")


bmi_men_avg = round((bmi_men_dict['India'][y1]+bmi_men_dict['India'][y2]+bmi_men_dict['India'][y3]+\
				bmi_men_dict['India'][y4]+bmi_men_dict['India'][y5])/5.0,2)

bmi_women_avg = round((bmi_women_dict['India'][y1]+bmi_women_dict['India'][y2]+bmi_women_dict['India'][y3]+\
				bmi_women_dict['India'][y4]+bmi_women_dict['India'][y5])/5.0,2)


bmi_percent = round(((abs(bmi_women_avg - bmi_men_avg))/((bmi_women_avg + bmi_men_avg)/2.0)) * 100,2)

print("*** India ***")
print("Men: ",bmi_men_avg)
print("Women: ",bmi_women_avg)
print("Percent Differnce: ",bmi_percent)
print("\n")


bmi_men_avg = round((bmi_men_dict['United States'][y1]+bmi_men_dict['United States'][y2]+bmi_men_dict['United States'][y3]+\
				bmi_men_dict['United States'][y4]+bmi_men_dict['United States'][y5])/5.0,2)

bmi_women_avg = round((bmi_women_dict['United States'][y1]+bmi_women_dict['United States'][y2]+bmi_women_dict['United States'][y3]+\
				bmi_women_dict['United States'][y4]+bmi_women_dict['United States'][y5])/5.0,2)


bmi_percent = round(((abs(bmi_women_avg - bmi_men_avg))/((bmi_women_avg + bmi_men_avg)/2.0)) * 100,2)

print("*** united States ***")
print("Men: ",bmi_men_avg)
print("Women: ",bmi_women_avg)
print("Percent Differnce: ",bmi_percent)
print("\n")


#5 - life exp plot

while True:

	country_name = str(input("Enter the country to visualize life expectancy data: "))
	f = 0
	for i in range(0,186):
		if str(life.loc[i][0].lower()) == str(country_name.lower()):
			name = life.loc[i][0]
			f = 1
			break
	if f == 0:
		print("<error> '"+country_name+"' is not a valid country.")
		continue		
	else:
		x = list(life.loc[i][1:])
		y = [i for i in range(1980,2009)]

		print("Plot for '"+str(life.loc[i][0])+"' opens in a new window.\n")

		plt.plot(x,y)
		plt.xlabel('life expectancy')
		plt.ylabel('years')
		plt.show()
		break

#6 - plot graph bmi world wide to life exp

y_bmi_world = []

for i in range(0,29):
	x = 0
	for j in range(0,186):
		x += bmi_all.iloc[i][j]
	x = x/186.0	
	y_bmi_world.append(x)

y_life = []

for i in range(1,30):
	x=0
	for j in range(0,186):
		x += life.iloc[j][i]
	x = x/186.0	
	y_life.append(x)

print("Correlation opens in a new window.\n")

x = [i for i in range(1980,2009)]

fig = plt.figure()
ax1 = fig.add_subplot()
ax1.set_xlabel('Years')
ax1.plot(x, y_life, 'b*-')
ax1.tick_params(axis = 'y', labelcolor = 'b')
ax1.set_ylabel('Avg Life Exp', color = 'b')

ax2 = ax1.twinx()
ax2.plot(x, y_bmi_world, 'ro-')
ax2.tick_params(axis = 'y', labelcolor = 'r')
ax2.set_ylabel('avg world wide bmi', color = 'r')
plt.show()