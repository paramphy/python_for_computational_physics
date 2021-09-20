##################################
# PROGRAM FOR NUMERICALLY SOLVING SCHRODINGER'S EQUATION
# MATTHEW SRNEC, SHIV UPADHYAY, and JEFFRY MADURA
##################################
import sys
ver=sys.version_info.major
if ver==2:
    from utils2 import *
elif ver==3:
    from utils3 import *
else:
    print("Python version not recognized. Python 2.5 or greater required.")
import numpy as np
##################################
#FUNCTIONS
##################################
########
# PARTICLE IN AN INFINITE POTENTIAL WELL
########
def infinite_well(steps=2000):
    # atomic units
    hbar=1.0
    m=1.0
    # get well width and number of wave function desired
    W,n=infinite_well_input()
    # divide by two so a well from -W to W is of input width
    W=W/2.0
    # create x-vector from -W to W
    xvec=np.linspace(-W,W,steps)
    # get step size
    h=xvec[1]-xvec[0]
    # create Laplacian via 3 point finite-difference method
    Laplacian=(-2.0*np.diag(np.ones(steps))+np.diag(np.ones(steps-1),1)\
        +np.diag(np.ones(steps-1),-1))/(float)(h**2)
    # create Hamiltonian
    Hamiltonian=((-0.5*(hbar**2)/m))*Laplacian
    # diagonalize the Hamiltonian yielding the wavefunctions and energies
    E,V=diagonalize_hamiltonian(Hamiltonian)
    # create plot
    infinite_well_plot(E,V,xvec,W,steps,n,Case,ask_to_save=True,ask_squared=True)
    # print output
    output(Case,['Well Width (a.u.)','Number of wavefunctions to plot'],[W*2,n],E,n)
########
# PARTICLE IN A FINITE WELL OF WIDTH (W) AND DEPTH (D)
########
def finite_well(steps=2000):
    # atomic units
    hbar=1.0
    m=1.0
    # get well depth and width
    A,D=finite_well_input()
    # divide by two so a well from -W to W is of input width
    W=A/2.0
    # create x-vector from -W to W
    xvec=np.linspace(-A,A,steps)
    # get step size
    h=xvec[1]-xvec[0]
    # create the potential from step function
    U=D*(step_func(xvec+W)-step_func(xvec-W))
    # create Laplacian via 3-point finite-difference method
    Laplacian=(-2.0*np.diag(np.ones(steps))+np.diag(np.ones(steps-1),1)\
        +np.diag(np.ones(steps-1),-1))/(float)(h**2)
    # create the Hamiltonian
    Hamiltonian=np.zeros((steps,steps))
    [i,j]=np.indices(Hamiltonian.shape)
    Hamiltonian[i==j]=U
    Hamiltonian+=(-0.5)*((hbar**2)/m)*Laplacian
    # diagonalize the Hamiltonian yielding the wavefunctions and energies
    E,V=diagonalize_hamiltonian(Hamiltonian)
    # determine number of energy levels to plot (n)
    n=0
    while E[n]<0:
        n+=1
    # create plot
    finite_well_plot(E,V,xvec,steps,n,Case,U,ask_to_save=True,ask_squared=True)
    # print output
    output(Case,['Well Width (a.u.)','Well Depth (a.u.)'],[W*2,-D],E,n)
########
# PARTICLE IN A DOUBLE FINITE WELL OF WIDTH (W), DISTANCE (B) APART, AND WELLS OF EQUAL DEPTH (D)
########
def double_finite_well_equal_depth(steps=2000):
    # atomic units
    hbar=1.0
    m=1.0
    # get well width, separation and depth
    W,B,D=double_finite_well_equal_depth_input()
    # set length variable for xvec
    A=2.0*((2*W)+B)
    # divide by two so a separation from -B to B is of input size
    B=B/2.0
    # create x-vector from -A to A
    xvec=np.linspace(-A,A,steps)
    # get step size
    h=xvec[1]-xvec[0]
    # create the potential from step function
    U=D*(step_func(xvec+W+B)-step_func(xvec+B)+\
        step_func(xvec-B)-step_func(xvec-W-B))
    # create Laplacian via 3-point finite-difference method
    Laplacian=(-2.0*np.diag(np.ones(steps))+np.diag(np.ones(steps-1),1)\
        +np.diag(np.ones(steps-1),-1))/(float)(h**2)
    # create the Hamiltonian
    Hamiltonian=np.zeros((steps,steps))
    [i,j]=np.indices(Hamiltonian.shape)
    Hamiltonian[i==j]=U
    Hamiltonian+=(-0.5)*((hbar**2)/m)*Laplacian
    # diagonalize the Hamiltonian yielding the wavefunctions and energies
    E,V=diagonalize_hamiltonian(Hamiltonian)
    # determine number of energy levels to plot (n)
    n=0
    while E[n]<0:
        n+=1
    # create plot
    finite_well_plot(E,V,xvec,steps,n,Case,U,ask_to_save=True,ask_squared=True)
    # print output
    output(Case,['Well Widths (a.u.)','Well Depths (a.u.)','Well Separation (a.u.)'],[W,-D,B*2],E,n)
########
# PARTICLE IN A DOUBLE FINITE WELL OF WIDTHS(W1 and W2), DIFFERENT DEPTHS
# (D1 and D2) AND DISTANCE (B) APART
########
def double_finite_well_unequal_depth(steps=2000):
    # atomic units
    hbar=1.0
    m=1.0
    # get well width, separation and depth
    W1,W2,B,D1,D2=double_finite_well_unequal_depth_input()
    # set length variable for xvec
    A=2.0*((W1+W2)+B)
    # divide by two so a separation from -B to B is of input size
    B=B/2.0
    # create x-vector from -A to A
    xvec=np.linspace(-A,A,steps)
    # get step size
    h=xvec[1]-xvec[0]
    # create the potential from step function
    U=D1*(step_func(xvec+W1+B)-step_func(xvec+B))+D2*\
        (step_func(xvec-B)-step_func(xvec-W2-B))
    # create Laplacian via 3-point finite-difference method
    Laplacian=(-2.0*np.diag(np.ones(steps))+np.diag(np.ones(steps-1),1)\
        +np.diag(np.ones(steps-1),-1))/(float)(h**2)
    # create the Hamiltonian
    Hamiltonian=np.zeros((steps,steps))
    [i,j]=np.indices(Hamiltonian.shape)
    Hamiltonian[i==j]=U
    Hamiltonian+=(-0.5)*((hbar**2)/m)*Laplacian
    # diagonalize the Hamiltonian yielding the wavefunctions and energies
    E,V=diagonalize_hamiltonian(Hamiltonian)
    # determine number of energy levels to plot (n)
    n=0
    while E[n]<0:
        n+=1
    # create plot
    finite_well_plot(E,V,xvec,steps,n,Case,U,ask_to_save=True,ask_squared=True)
    # print output
    output(Case,['Well 1 Width (a.u.)','Well 2 Width (a.u.)','Well 1 Depth (a.u.)','Well 2 Depth (a.u.)','Well Separation (a.u.)'],[W1,W2,-D1,-D2,B*2],E,n)
########
# PARTICLE IN A HARMONIC WELL OF DEPTH (D) WITH A FORCE CONSTANT (OMEGA)
########
def harmonic_well(steps=2000):
    # atomic units
    hbar=1.0
    m=1.0
    # get well force constant and depth
    omega,D=harmonic_well_input()
    # divide by two so a well from -W to W is of input width
    W=np.sqrt(np.abs(2.0*D)/(omega**2))
    # set length variable for xvec
    A=W*2.0
    # create x-vector from -A to A
    xvec=np.linspace(-A,A,steps)
    # get step size
    h=xvec[1]-xvec[0]
    # create the potential from harmonic potential function
    U=harmonic_potential(xvec,omega,D)
    # create Laplacian via 3-point finite-difference method
    Laplacian=(-2.0*np.diag(np.ones(steps))+np.diag(np.ones(steps-1),1)\
        +np.diag(np.ones(steps-1),-1))/(float)(h**2)
    # create the Hamiltonian
    Hamiltonian=np.zeros((steps,steps))
    [i,j]=np.indices(Hamiltonian.shape)
    Hamiltonian[i==j]=U
    Hamiltonian+=(-0.5)*((hbar**2)/m)*Laplacian
    # diagonalize the Hamiltonian yielding the wavefunctions and energies
    E,V=diagonalize_hamiltonian(Hamiltonian)
    # determine theoretical number of energy levels (n)
    n=0
    while E[n]<0:
        n+=1
    # create plot
    finite_well_plot(E,V,xvec,steps,n,Case,U,ask_to_save=True,ask_squared=True)
    # print output
    output(Case,['Force Constant','Depth (a.u.)'],[omega,-D],E,n)
########
# PARTICLE IN A MORSE WELL OF DEPTH (D) WITH A FORCE CONSTANT (OMEGA)
########
def morse_well(steps=2000):
    # atomic units
    hbar=1.0
    m=1.0
    # get well force constant and depth
    omega,D=morse_well_input()
    # create the potential from morse potential function
    xvec,h,U=morse_potential(omega,D,steps)
    # create Laplacian via 3-point finite-difference method
    Laplacian=(-2.0*np.diag(np.ones(steps))+np.diag(np.ones(steps-1),1)+\
        np.diag(np.ones(steps-1),-1))/(float)(h**2)
    # create the Hamiltonian
    Hamiltonian=np.zeros((steps,steps))
    [i,j]=np.indices(Hamiltonian.shape)
    Hamiltonian[i==j]=U
    Hamiltonian+=(-0.5)*((hbar**2)/m)*Laplacian
    # diagonalize the Hamiltonian yielding the wavefunctions and energies
    E,V=diagonalize_hamiltonian(Hamiltonian)
    # determine number of energy levels to plot (n)
    n=0
    while E[n]<0:
        n+=1
    # create plot
    finite_well_plot(E,V,xvec,steps,n,Case,U,ask_to_save=True,ask_squared=True)
    # print output
    output(Case,['Force Constant','Depth (a.u.)'],[omega,-D],E,n)
########
# Kronig-Penney Model
########
def Kronig_Penney(steps=2000):
    # atomic units
    hbar=1.0
    m=1.0
    # get well depth and width
    A,D,B,num_wells=Kronig_Penney_input()
    # divide by two so a well from -W to W is of input width
    W=A/2.0
    # create x-vector from -W to W
    x_size = (A * (num_wells // 2.0)) + (B * (num_wells //2.0)) + W + B/2.0
    xvec=np.linspace(-x_size,x_size,steps)
    # get step size
    h=xvec[1]-xvec[0]
    # create the potential from step function
    U = (step_func(xvec + W)-step_func(xvec-W))
    for n in range(1,((num_wells//2)+1)):
        U += (step_func(xvec + W + (n*B) + ((n)*A)) - step_func(xvec + W + (n*B) + ((n-1)*A)))
        U += (step_func(xvec - W - (n*B) - ((n-1)*A)) - step_func(xvec - W - (n*B) - ((n)*A)))
    U *= D
    # create Laplacian via 3-point finite-difference method
    Laplacian=(-2.0*np.diag(np.ones(steps))+np.diag(np.ones(steps-1),1)\
        +np.diag(np.ones(steps-1),-1))/(float)(h**2)
    Laplacian[0,len(Laplacian)-1] = -1/(float)(h**2)
    Laplacian[len(Laplacian)-1,0] = -1/(float)(h**2)
    # create the Hamiltonian
    Hamiltonian=np.zeros((steps,steps))
    [i,j]=np.indices(Hamiltonian.shape)
    Hamiltonian[i==j]=U
    Hamiltonian+=(-0.5)*((hbar**2)/m)*Laplacian
    # diagonalize the Hamiltonian yielding the wavefunctions and energies
    E,V=diagonalize_hamiltonian(Hamiltonian)
    # determine number of energy levels to plot (n)
    n=0
    while E[n]<0:
        n+=1
    # create plot
    Kronig_Penney_Plot(E,V,xvec,steps,n,Case,U,ask_to_save=True,ask_squared=True)
    # print output
    output(Case,['Well Width (a.u.)','Well Depth (a.u.)','Well Separation (a.u.)'],[W*2,-D,B],E,n)
##################################
#MAIN CODE
##################################
os.system('clear')
Case=choices()
while(Case in set(titles.keys())):
    if(Case==1):
        infinite_well()
    elif(Case==2):
        finite_well()
    elif(Case==3):
        double_finite_well_equal_depth()
    elif(Case==4):
        double_finite_well_unequal_depth()
    elif(Case==5):
        harmonic_well()
    elif(Case==6):
        morse_well()
    elif(Case==7):
        Kronig_Penney()
    Case=choices(Case)
