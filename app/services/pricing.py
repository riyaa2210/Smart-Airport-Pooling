# app/services/pricing.py

def calculate_fare(base_rate, distance_km, rate_per_km, passengers_in_cab, demand_factor=1.0):
    """
    Fare Formula:
    Fare = (Base + Distance * Rate) * (1 / Passengers) * Demand
    """

    if passengers_in_cab <= 0:
        passengers_in_cab = 1

    fare = (
        (base_rate + (distance_km * rate_per_km))
        * (1 / passengers_in_cab)
        * demand_factor
    )

    return round(fare, 2)
