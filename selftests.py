import datahandaling
import getdata
import json

def Test():
    # Run Self Tests To ensure the Code can Opperate
    print("Checking Dependecies")
    try:
        if getdata:
            print("Getdata module is installed")
        else:
            print("Getdata module are not installed")
            exit("Please install the Getdata module")
        if json:
            print("Json module is installed")
        else:
            print("Json module are not installed")
            exit("Please install the Json module")
    except:
        print("Dependecie Test Failed")
        exit("Fatal")
    print("All Dependecies are installed")
    
    print("Running Internet Acccess Test")
    try:
        internet = getdata.HeartBeat.InternetCheck()
        if internet == True:
            print("Internet Access Test Passed")
        else:
            print("Internet Access Test Failed")
            print("Please check your internet connection")
            exit("No internet connection")
    except:
        print("Fatal Error Occured During Internet Test.")
        exit("Internet Test Failed")
    print("Running API Test")
    try:
        postcode = 'RG14'
        fuel_providers = [
            ("Sainsbury's", getdata.GetData.Sainsburys),
            ("Shell", getdata.GetData.Shell),
            ("AppleGreen", getdata.GetData.AppleGreen),
            ("Ascona", getdata.GetData.Ascona),
            ("Asda", getdata.GetData.Asda),
            ("BP", getdata.GetData.BP),
            ("Esso Tesco", getdata.GetData.ET),
            ("Jet", getdata.GetData.Jet),
            ("Karen", getdata.GetData.Karen),
            ("Morrisons", getdata.GetData.Morisons),
            ("Moto", getdata.GetData.Moto),
            ("Motor", getdata.GetData.Motor),
            ("Rontec", getdata.GetData.RonTec),
            ("SGN", getdata.GetData.SGN),
        ]
        succes = 0
        fail = 0

        matching_stations = []
        for name, get_method in fuel_providers:
            try:
                data = get_method()
            except:
                error = Exception
                exit("Api Test")
            if data is not None:
                print(name, "API Test Passed")
                succes=+1
            else:
                print(name, "API Test Failed")
                fail=+1
        if succes >= fail:
            print("API Test Passed")
        else:
            print("API Test Failed")
    except:
        print("API Test Encounted Fatal Error")
        exit("Error Occured")