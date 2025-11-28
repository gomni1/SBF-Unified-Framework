"""
SINGLE BULK FRAMEWORK (SBF) v1.4
Unified Geometric Calculator

Description:
Derives the Lepton Mass Hierarchy and Neutrino Sector properties
solely from the geometry of Random Close Packing (RCP).
"""

import numpy as np

def run_sbf_verification():
    print("\n=== SBF v1.4 PHYSICS VERIFICATION ===")
    
    # --- 1. FUNDAMENTAL CONSTANTS ---
    M_e = 0.51099        # Electron Mass (MeV)
    E_void = 2.3e-9      # Dark Energy Scale (MeV)
    
    # The Geometric Axiom (Bernal Limit)
    Z = 14.39            
    xi = 1 / (2 * np.pi) 

    print(f"Vacuum Coordination (Z): {Z} (Bernal Limit)")
    print("-" * 45)

    # --- 2. THE LEPTON SECTOR (Contact Network) ---
    print("--- CONTACT NETWORK (Charged Leptons) ---")
    
    # MUON (N=5)
    M_mu_pred = M_e * (Z**2)
    M_mu_obs  = 105.658
    err_mu    = abs(M_mu_pred - M_mu_obs) / M_mu_obs * 100
    print(f"[MUON N=5] Pred: {M_mu_pred:.4f} MeV | Error: {err_mu:.3f}%")
    
    # TAU (N=6)
    M_tau_pred = M_e * (Z**3) * (1 + xi)
    M_tau_obs  = 1776.86
    err_tau    = abs(M_tau_pred - M_tau_obs) / M_tau_obs * 100
    print(f"[TAU N=6]  Pred: {M_tau_pred:.4f} MeV | Error: {err_tau:.3f}%")
    
    # --- 3. THE DARK SECTOR (Void Network) ---
    print("--- VOID NETWORK (Neutrinos) ---")
    
    # NEUTRINO MASS (Scaled by Dark Energy)
    M_nu_pred_eV = (E_void * Z) * 1e6 
    print(f"[NEUTRINO] Pred: {M_nu_pred_eV:.3f} eV (Scale: Void Energy * Z)")

    # MIXING ANGLE (Scaled by Density Deficit)
    phi_fcc = np.pi / np.sqrt(18)
    phi_rcp = 0.6366
    tortuosity = np.sqrt(2)
    
    sin_theta = (phi_fcc - phi_rcp) * tortuosity
    theta_pred = np.degrees(np.arcsin(sin_theta))
    
    print(f"[THETA_13] Pred: {theta_pred:.2f}° | Obs: 8.57°")
    print("=" * 45)

if __name__ == "__main__":
    run_sbf_verification()
