viscosity = 1.461 *10**(-5) # [m^2/s]
rho = 1.255 # [kg/m^3]

def Reynolds(U, D):
    """Reynolds number

    Args:
        U (flaot): Speed in [m/s]
        D (float): Caracteristic length (height in [m])

    Returns:
        float: Reynolds number [-]
    """
    return U*D/viscosity

def Strouhal(U, D, f):
    """Strouhal number

    Args:
        U (flaot): Speed in [m/s]
        D (float): Caracteristic length (height in [m])
        f (float): Frequency of vortices in [Hz]

    Returns:
        float: Strouhal number [-]
    """
    return f*D/U

def C_D(F, U, D):
    """Drag coefficient

    Args:
        F (float): Force in [N] !!
        U (float): Speed in [m/s]
        D (float): Height in [m]

    Returns:
        float: Drag coefficient [-]
    """
    return F/(U**2 *rho*(D*1)*(1/2))

def C_L(F, U, L):
    """Lift coefficient

    Args:
        F (float): Force in [N] !!
        U (float): Speed in [m/s]
        L (float): Maximum length in [m]

    Returns:
        float: Lift coefficient [-]
    """
    return F/(U**2 *rho*(L*1)*(1/2))


print("Preliminary Study:")
print(f"\t Re: {Reynolds(0.01, 0.3):.2f}")
print(f"\t St: {Strouhal(0.01, 0.3, 0.003968253968253968):.2f}")
print(f"\t C_D: {C_D(0.01945*10**(-3), 0.01, 0.3):.2f}")
print(f"\t C_L: {C_L(0.02213*10**(-3), 0.01, 0.9):.2f}")

print("Hexagonal Study:")
U1000 = 1000*viscosity/0.3
print(f"\t Re: {Reynolds(U1000, 0.3):.2f} for {U1000:.3f} m/s")
print(f"\t Re: {Reynolds(23, 0.3):.2f} for {U1000:.3f} m/s")
print(f"\t C_D: {C_D(0.01945*10**(-3), 0.01, 0.3):.2f}")
print(f"\t C_L: {C_L(0.02213*10**(-3), 0.01, 0.9):.2f}")

print(1000*viscosity/0.3)