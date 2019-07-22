import datetime
import pandas

def readcsv():
	df = pandas.read_csv('kion.csv', encoding='sjis', skiprows=[1,2])

	days = {}
	months = {}
	weeks = {}
	for i, row in df.iterrows():
		dt = datetime.datetime.strptime(row['Date/Time'], '%Y-%m-%d %H:%M:%S')
		if dt < datetime.datetime(2019, 6, 4):
			continue
		if dt.date() not in days:
			days[dt.date()] = [None] * 24
		temp = float(row['No.1'])
		days[dt.date()][dt.hour] = temp

		week = (dt - datetime.timedelta(days=dt.weekday())).date()
		if week not in weeks:
			weeks[week] = []
		weeks[week].append(temp)

		month = datetime.date(dt.year, dt.month, 1)
		if month not in months:
			months[month] = []
		months[month].append(temp)

	return (df, days, months, weeks)
