```python
import numpy as np

def lcoh(capex, opex_annual, lifetime_years, wacc, annual_h2_production_kg):
    """
    LCOH simplifié (€/kg H2)
    """
    # Facteur d'actualisation pour une annuité
    annuity_factor = (wacc * (1 + wacc) ** lifetime_years) / ((1 + wacc) ** lifetime_years - 1)

    annualized_capex = capex * annuity_factor
    total_annual_cost = annualized_capex + opex_annual

    return total_annual_cost / annual_h2_production_kg


print("=== LCOH Hydrogen Model – Demo ===\n")

# Hypothèses communes
lifetime = 20
wacc = 0.07
annual_production = 10_000_000  # kg H2 / an (fictif)

scenarios = {
    "Bas": {
        "capex": 200_000_000,  # €
        "opex_annual": 8_000_000
    },
    "Central": {
        "capex": 250_000_000,
        "opex_annual": 10_000_000
    },
    "Haut": {
        "capex": 320_000_000,
        "opex_annual": 12_000_000
    }
}

results = {}

for name, params in scenarios.items():
    lcoh_value = lcoh(
        capex=params["capex"],
        opex_annual=params["opex_annual"],
        lifetime_years=lifetime,
        wacc=wacc,
        annual_h2_production_kg=annual_production
    )
    results[name] = lcoh_value
    print(f"Scénario {name} : LCOH = {lcoh_value:.2f} €/kg H2")

# Analyse simple
print("\nInterprétation business (démo) :")
sorted_scenarios = sorted(results.items(), key=lambda x: x[1])

best = sorted_scenarios[0]
worst = sorted_scenarios[-1]

print(f"- Le scénario le plus compétitif est '{best[0]}' avec {best[1]:.2f} €/kg.")
print(f"- Le scénario le moins compétitif est '{worst[0]}' avec {worst[1]:.2f} €/kg.")

# Sensibilité CAPEX (central)
print("\nAnalyse de sensibilité CAPEX (scénario Central) :")
central = scenarios["Central"]

for delta in [-0.2, -0.1, 0, 0.1, 0.2]:
    capex_var = central["capex"] * (1 + delta)
    lcoh_var = lcoh(
        capex=capex_var,
        opex_annual=central["opex_annual"],
        lifetime_years=lifetime,
        wacc=wacc,
        annual_h2_production_kg=annual_production
    )
    print(f"CAPEX {'+' if delta>0 else ''}{int(delta*100)}% → LCOH = {lcoh_var:.2f} €/kg")
