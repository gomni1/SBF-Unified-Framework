import numpy as np
import matplotlib.pyplot as plt

def plot_kill_criterion():
    print("Generating LiteBIRD Prediction Graph...")
    l = np.arange(2, 20)
    power_sm = 100 * (l)**(-1.5) # Standard Inflation (Smooth)
    
    # SBF Prediction: Resonance at l=4 (Cubic) and l=6 (FCC)
    power_sbf = power_sm.copy()
    power_sbf[l == 4] *= 3.0
    power_sbf[l == 6] *= 2.0
    
    plt.figure(figsize=(10, 6), facecolor='#1e1e1e')
    ax = plt.gca()
    ax.set_facecolor('#1e1e1e')
    
    plt.plot(l, power_sm, 'w--', alpha=0.4, label='Standard Inflation (Smooth)')
    plt.plot(l, power_sbf, 'r-o', linewidth=3, label='SBF v1.4 (Geometric Resonance)')
    
    plt.title('THE KILL CRITERION: CMB B-Mode Polarization', color='white', fontsize=14)
    plt.xlabel('Multipole Moment ($\ell$)', color='white')
    plt.ylabel('Power', color='white')
    plt.tick_params(colors='white')
    plt.legend()
    plt.grid(True, alpha=0.1)
    
    plt.savefig('sbf_prediction.png', dpi=300)
    print("Graph saved as 'sbf_prediction.png'")
    plt.show()

if __name__ == "__main__":
    plot_kill_criterion()
