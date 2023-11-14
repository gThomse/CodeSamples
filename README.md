# CodeSamples


CodeSamples has 6 Subdirectories:
	Output Graphs
	Data
	Excel
	powerBI
	py
	sql

Output Graphs holds images of two graphs with python from two data sources:

	3 Years worth.png :
		Max, Min and Rain data from 10/6/2020 for the Townsville (Qld) region 
			Data source: Results TAB of "Townsville Forecast .xlsm"  in data subfolder

	Exchange Rate Graph.png:
		1 Australian $ buys (Exchange Rates)
			Data Source: Rate History Table in "RBA ExchRatesHistory.accdb" in data subfolder


Data 
	Flights.xlsm:
		The Bookings Tab has a travel internary with departure and arrival times in locl timzones.
		This spreadsheet is used as input to to convert the departure and arrival times into Australian EST for family to 
			track progress locally

	Forecast Data.xlsx:
		The results TAB holds the daily fornight weather forcast for Townsville for a few years.

	RBA ExchRatesHistory.accb:
		Holds the Australian Exchange Rate for 20 + countries since 1/5/2020

	YouTube py lite.db:
		Is an SQLite database holding details of some of my favourite programming videos

	YouTube python.accdb:
		Holds the same details as "YouTube py lite.db" but in MS Access format.
		The Main Table is called "python videos", but it also holds Git. HTML CSS, JavaScript, Sublime Text, Visual Studios vidoes 
			as well as Python vidoes.

Excel
	Flights.xlsx
		As above in Data
	Forecast Data.xlsx
		AS above in Data
	Townsville Forecast.xlsm
		Uses Power Query Editor to Massage data in Dorecast Data.xlsx
		It's used to visualise the weather data in 4 graphs (with slicers)

PowerBI
	Data Forecasts.pbix
		Uses "Forecast Data.xlsx" data to transform data to create a dashboard 
	Foreign Exchange Rates for Australia.pbix
		Uses "RBA ExchRatesHistory.accb" to create a dashboard
	YouTube py list.pbix
		Uses  "YouTube py lite.db" to create a dashboard to graphically show my favourite YouTube Owners vidoes.

py
	YT Create sqlite.py
	YT Create sqlite Indexes.py
	YT Query sqlite.py
		3 utility scripts to create the table, to index it, and a query within "YouTube py lite.db"
	
	1 YouTube Python.py
		Outputs to MS access database	
	2 You Tube Python sqlite.py
		Outputs to an SQLite database (for the fun of the exercise)

		Both use a Google API to query my YouTube saved playlist.
		
		
	Candian and USA Exchange.py
		Used to create MathPlotLib graph used to create the Exchange Rate Graph.png

	"International Appointments.py"
		Is a utility I wrote to list times around the world of destinations I have friends and family.

	"flight time2.py" and Flights.xlsx
		Is a utility I wrote to convert airline arrival and departure times on my travel schedule to local dates and times for relatives in Australia wanting to track the trip.

	"HEIC_to_JPG.py"
		Is a utility I wrote to convert HEIC pictures to JPG format. 

	"Read Weather.py"
		Used to read ""Townsville Forecast.xlsm" and use pandas, amd MathPlotLib to create "Max T, Min T, and Rain since " graph / image in Output Graphs "3 Years worth.png".

	"Recipelinks HomeCookingAdventure.py"
		The first sample "Recipelinks HomeCookingAdventure.py", is a utility to scrape and provide descriptions and 'redirection' links of recipes from a provided URL provided by one of my favourite cooking sites, www.homecooking.adventure.
		I wrote it to simplify the extracting and selection of recipe links for loading into my favourite Recipe App, Paprika. To reduce my keystrokes.

	RBA 07.py
		Used to call MathPlotLib to display Exchange data summary "Exchange Rate Graph.png" 

	findFile.py
		Very early code used to find the path to a file of a know file in a subdirectory. 
			It works but there are better ways. 

		These days I perfer to use Environment variables to provide the start location of a path, if I don't want to 
		hard code it. 

	flight_time_2.py
		Is incorrectly named. 
		It is used to show me local times from around the world, from multiple timezones for international calls
		(Yes I know you can use mose clock apps to show this but, this app can be used for future times not just the current moment. Plus it was easy and fun to write)

sql
	Maintenace Progress 2.sql and Pole Voltage.sql are two scripts I wrote for maintenace tracking and Regulatory counts previously.
	They hold no propriety / sensitive information. 

	Pole Voltage:
		Provides a count of different poles. The script also use the nvl oracle function to include a pole (worse case count) for consideration. 

	Maintenace Progress 2.sql
		Drops and re creates a temporary table to store the resutls of multiple queries  for future reprots or other applications. 
		Originally it was run remote to reduce comms traffic over a slow internet. 

