# Constants

CARBON_PER_LITER_OF_FUEL = 2.31 # kg of CO2 per litre of fuel burned
#AVERAGE_FUEL_EFFICIENCY = 10.9 # km per litre of fuel burned
AVERAGE_FUEL_DENSITY = 0.75 # kg of fuel per litre

distance_travelled = 1000 # km
fuel_efficiency = 8.5 # km per litre

# Define function for calculating carbon footprint

def calculate_carbon_footprint(distance_travelled, fuel_efficiency):
    fuel_consumed = distance_travelled / fuel_efficiency

    carbon_emitted = fuel_consumed * AVERAGE_FUEL_DENSITY * CARBON_PER_LITER_OF_FUEL 

    return carbon_emitted

transport_carbon_footprint = calculate_carbon_footprint(distance_travelled, fuel_efficiency)
transport_carbon_footprint = "{:,.3f}".format(transport_carbon_footprint)

print(f"Carbon footprint for travelling {distance_travelled} km with a fuel efficiency of {fuel_efficiency} km/L: {transport_carbon_footprint} kgCO2e.")