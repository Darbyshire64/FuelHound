import getdata
import json

# Welcome User
#print("Welcome To Fuel Price Directory")

print("Initialising And Testing Integrity")
# Initialize an array to store matching stations
matching_stations = []

# Gather Search Data
#postal = input("Enter The First Section of Your Postal Code: ")

#Validate Data
#if len(postal) > 4:
    #print("Invalid Postal Code")
    #exit()
#try:
    #postal = str(postal)
#except:
    #print("Invalid Postal Code")
    #exit()
postal = "RG14"

print("Searching For Stations Near You")
# Sainsbury's
Sbdata = getdata.GetData.Sainsburys()
if Sbdata is None:
    print("Request To Sainsburys API Failed")
else:
    print("Request To Sainsburys API Successful")
    # Parse the data
    sbdataprocessing = json.loads(Sbdata)

    # Find DataTime
    print(f"Data Time: {sbdataprocessing['last_updated']}")

    # Iterate through the data and match the postal code
    for site in sbdataprocessing['stations']:
        site_postal = site['postcode'].split(' ')[0]
        if site_postal == postal:
            matching_stations.append(site)
            print(f"Match found: {site['site_id']}")
            print(f"Address: {site['address']}")

    print("Sainsburys Search: Complete")
    

SHLdata = getdata.GetData.Shell()
if SHLdata is None:
    print("Request To Shell API Failed")
else:
    print("Request To Shell API Successful")
    # Parse the data
    SHLdataprocessing = json.loads(SHLdata)

    # Find DataTime
    print(f"Data Time: {SHLdataprocessing['last_updated']}")

    # Iterate through the data and match the postal code
    for site in SHLdataprocessing['stations']:
        site_postal = site['postcode'].split(' ')[0]
        if site_postal == postal:
            matching_stations.append(site)
            print(f"Match found: {site['site_id']}")
            print(f"Address: {site['address']}")

    print("Shell Search: Complete")


AGdata = getdata.GetData.AppleGreen()
if AGdata is None:
    print("Request To AppleGreens API Failed")
else:
    print("Request To AppelGreens API Successful")
    # Parse the data
    AGdataprocessing = json.loads(AGdata)

    # Find DataTime
    print(f"Data Time: {AGdataprocessing['last_updated']}")

    # Iterate through the data and match the postal code
    for site in AGdataprocessing['stations']:
        site_postal = site['postcode'].split(' ')[0]
        if site_postal == postal:
            matching_stations.append(site)
            print(f"Match found: {site['site_id']}")
            print(f"Address: {site['address']}")

    print("AppleGreen Search: Complete")

Adata = getdata.GetData.Ascona()
if Adata is None:
    print("Request To Ascona API Failed")
else:
    print("Request To Ascona API Successful")
    # Parse the data
    Adataprocessing = json.loads(Adata)

    # Find DataTime
    print(f"Data Time: {Adataprocessing['last_updated']}")

    # Iterate through the data and match the postal code
    for site in Adataprocessing['stations']:
        site_postal = site['postcode'].split(' ')[0]
        if site_postal == postal:
            matching_stations.append(site)
            print(f"Match found: {site['site_id']}")
            print(f"Address: {site['address']}")

    print("Ascona Search: Complete")

ASdata = getdata.GetData.Asda()
if ASdata is None:
    print("Request To Asda API Failed")
else:
    print("Request To Asda API Successful")
    # Parse the data
    ASdataprocessing = json.loads(ASdata)

    # Find DataTime
    print(f"Data Time: {ASdataprocessing['last_updated']}")

    # Iterate through the data and match the postal code
    for site in ASdataprocessing['stations']:
        site_postal = site['postcode'].split(' ')[0]
        if site_postal == postal:
            matching_stations.append(site)
            print(f"Match found: {site['site_id']}")
            print(f"Address: {site['address']}")

    print("Asda Search: Complete")

Bdata = getdata.GetData.BP()
if Bdata is None:
    print("Request To BP API Failed")
else:
    print("Request To Bp API Successful")
    # Parse the data
    Bdataprocessing = json.loads(Bdata)

    # Find DataTime
    print(f"Data Time: {Bdataprocessing['last_updated']}")

    # Iterate through the data and match the postal code
    for site in Bdataprocessing['stations']:
        site_postal = site['postcode'].split(' ')[0]
        if site_postal == postal:
            matching_stations.append(site)
            print(f"Match found: {site['site_id']}")
            print(f"Address: {site['address']}")

    print("Bp Search: Complete")

ETdata = getdata.GetData.ET()
if ETdata is None:
    print("Request To Esso Tesco API Failed")
else:
    print("Request To Esso Tesco API Successful")
    # Parse the data
    ETdataprocessing = json.loads(ETdata)

    # Find DataTime
    print(f"Data Time: {ETdataprocessing['last_updated']}")

    # Iterate through the data and match the postal code
    for site in ETdataprocessing['stations']:
        site_postal = site['postcode'].split(' ')[0]
        if site_postal == postal:
            matching_stations.append(site)
            print(f"Match found: {site['site_id']}")
            print(f"Address: {site['address']}")

    print("Esso Tesco Search: Complete")

Jetdata = getdata.GetData.Jet()
if Jetdata is None:
    print("Request To Jet API Failed")
else:
    print("Request To Jet API Successful")
    # Parse the data
    Jetdataprocessing = json.loads(Jetdata)

    # Find DataTime
    print(f"Data Time: {Jetdataprocessing['last_updated']}")

    # Iterate through the data and match the postal code
    for site in Jetdataprocessing['stations']:
        site_postal = site['postcode'].split(' ')[0]
        if site_postal == postal:
            matching_stations.append(site)
            print(f"Match found: {site['site_id']}")
            print(f"Address: {site['address']}")

    print("Jet Search: Complete")
Karendata = getdata.GetData.Karen()
if Karendata is None:
    print("Request To Karen API Failed")
else:
    print("Request To Karen API Successful")
    # Parse the data
    Karendataprocessing = json.loads(Karendata)

    # Find DataTime
    print(f"Data Time: {Karendataprocessing['last_updated']}")

    # Iterate through the data and match the postal code
    for site in Karendataprocessing['stations']:
        site_postal = site['postcode'].split(' ')[0]
        if site_postal == postal:
            matching_stations.append(site)
            print(f"Match found: {site['site_id']}")
            print(f"Address: {site['address']}")

    print("Karen Search: Complete")
Morrisondata = getdata.GetData.Morisons()
if Morrisondata is None:
    print("Request To Morrison API Failed")
else:
    print("Request To Morrison API Successful")
    # Parse the data
    Morrisondataprocessing = json.loads(Morrisondata)

    # Find DataTime
    print(f"Data Time: {Morrisondataprocessing['last_updated']}")

    # Iterate through the data and match the postal code
    for site in Morrisondataprocessing['stations']:
        site_postal = site['postcode'].split(' ')[0]
        if site_postal == postal:
            matching_stations.append(site)
            print(f"Match found: {site['site_id']}")
            print(f"Address: {site['address']}")

    print("Morrison Search: Complete")
Motodata = getdata.GetData.Moto()
if Motodata is None:
    print("Request To Moto API Failed")
else:
    print("Request To Moto API Successful")
    # Parse the data
    Motodataprocessing = json.loads(Motodata)

    # Find DataTime
    print(f"Data Time: {Motodataprocessing['last_updated']}")

    # Iterate through the data and match the postal code
    for site in Motodataprocessing['stations']:
        site_postal = site['postcode'].split(' ')[0]
        if site_postal == postal:
            matching_stations.append(site)
            print(f"Match found: {site['site_id']}")
            print(f"Address: {site['address']}")

    print("Moto Search: Complete")
motordata = getdata.GetData.Motor()
if motordata is None:
    print("Request To motor API Failed")
else:
    print("Request To motor API Successful")
    # Parse the data
    motordataprocessing = json.loads(motordata)

    # Find DataTime
    print(f"Data Time: {motordataprocessing['last_updated']}")

    # Iterate through the data and match the postal code
    for site in motordataprocessing['stations']:
        site_postal = site['postcode'].split(' ')[0]
        if site_postal == postal:
            matching_stations.append(site)
            print(f"Match found: {site['site_id']}")
            print(f"Address: {site['address']}")

    print("motor Search: Complete")


print(f"Matching Stations: {matching_stations}")
