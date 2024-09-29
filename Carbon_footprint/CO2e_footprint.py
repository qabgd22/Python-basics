#  Define the CO2e emissions (in kgCO2e per kWh) for the electricity grid in the region

CO2e_per_kWh = 0.52 # example value for US grid

# Define a function to calculate the carbon footprint of air conditioning

def calculate_carbon_footprint(ac_power, hours_of_use, days_of_use):
    kWh = ac_power * hours_of_use * days_of_use / 1000.0

    total_CO2e = CO2e_per_kWh * kWh

    return total_CO2e

carbonFootPrint = calculate_carbon_footprint(1000, 8, 30)

print("The carbon footprint of air conditioning is: {:.2f} kgCO2e.".format(carbonFootPrint))



