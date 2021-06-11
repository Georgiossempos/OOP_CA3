from daft_scraper.search import DaftSearch, SearchType
from daft_scraper.search.options import (
    PropertyType, PropertyTypesOption, Facility, FacilitiesOption,
    PriceOption, BedOption
)
from daft_scraper.search.options_location import LocationsOption, Location
import csv

cityLocations = {
  "dublin 1": Location.DUBLIN_1_DUBLIN,
  "dublin 2": Location.DUBLIN_2_DUBLIN,
  "dublin 3": Location.DUBLIN_3_DUBLIN,
  "dublin 4": Location.DUBLIN_4_DUBLIN,
  "dublin 5": Location.DUBLIN_5_DUBLIN,
  "dublin 6": Location.DUBLIN_6_DUBLIN,
  "dublin 7": Location.DUBLIN_7_DUBLIN,
  "dublin 8": Location.DUBLIN_8_DUBLIN,
  "dublin 9": Location.DUBLIN_9_DUBLIN,
  "dublin city": Location.DUBLIN_CITY

}

# user enters dublin
# you check for dublin in an array then assign that to the options
city = input("Enter city location [`dublin 1`]: ")


# apply an algorithn that takes in these listings and does some magic to return a shorter list(give me all the apartments, flats, ect.)
# Algorithm: 
# (1) get all rentals in a given location
def getAllApartmentRentalsInLocation(city):
    # set location, property type (apartment) and number of beds
    options = [
        LocationsOption([cityLocations[city]]), #location entered by user
        PropertyTypesOption([PropertyType.APARTMENT]), #only apartments
        BedOption(1, 1), #1 bedroom
        PriceOption(0, 1500), #1500 budget per month
    ]   

    # make request to api to get the listings (Scrape)
    api = DaftSearch(SearchType.RENT)
    listings = api.search(options)
    return listings

# (2) sort results by price - smallest to biggest
def sortResultsByPrice(listings):
    sortedResults = sorted(listings, key=lambda x: x.price)
    return sortedResults

# (3) remove duplicate properties
#def removeDuplicateProperties(sortedResults):
 #   noDuplicates = list(dict.fromkeys(sortedResults))
  #  return noDuplicates

listings = getAllApartmentRentalsInLocation(city)
sortedListingsByPrice = sortResultsByPrice(listings)
#print(apartment.title, "|", apartment.price, "|", apartment.url)

# then save this small list into a CSV file
with open('apartmentsInDublin.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["Address", "Price", "Daft URL"])
    # add data to file
    for apartment in sortedListingsByPrice:
        writer.writerow([apartment.title, apartment.price, apartment.url])
