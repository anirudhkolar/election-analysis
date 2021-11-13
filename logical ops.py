counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties:
    print("El Paso is in the list of counties")
else:
    print("El Paso is not in the list of counties")

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties and "Arapahoe" in counties:
    print("El Paso and Arapahoe are in the list of counties.")
else:
    print("El Paso or Arapahoe is not in the list of counties")

counties = ["Arapahoe","Denver","Jefferson"]
if "El Paso" in counties or "Arapahoe" in counties:
    print("El Paso or Arapahoe is in the list of counties.")
else:
    print("El Paso and Arapahoe are not in the list of counties")