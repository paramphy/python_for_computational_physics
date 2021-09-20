import sys
version=sys.version_info.major
import os
import numpy as np
import scipy as sp
import scipy.linalg as spla
import matplotlib.pyplot as plt
import matplotlib.ticker as mtick
import matplotlib as mpl
try:
    from colorama import Fore,Back,Style
    from colorama import init
    init(autoreset=True)
    print_color=True
except:
    print_color=False
np.set_printoptions(threshold='nan')
titles={
    1:'Particle in an infinite potential well',
    2:'Particle in a finite well',
    3:'Particle in a double finite well (equal depth)',
    4:'Particle in a double finite well (unequal depth)',
    5:'Particle in a harmonic well',
    6:'Particle in a Morse well',
    7:'Kronig-Penney finite well'}
##################################
#FUNCTIONS
##################################
########
# IO FUNCTIONS
########
def print_center_text(s):
    print '{:^79}'.format(s)
def valid_input_error_message():
    if print_color:
        print Fore.RED+'\nPlease enter a valid input!\n'
    else:
        print '\nPlease enter a valid input!\n'
def print_startup():
    print ""
    print '*'*79
    print_center_text('Welcome to the Schrodinger Solver!')
    print_center_text('Created by: Matthew Srnec, Shiv Upadhyay, and Jeffry Madura')
    print '*'*79
def print_choices():
    print '\tPlease enter the case number you would like to study.'
    print '\tCases:'
    for i,j in titles.items():
        print('\t\t {}. {}'.format(i,j))
    print '\t\t99. Quit\n'
def choices(Case=111):
    if Case==111:
        # First Print
        print_startup()
        print_choices()
    elif Case==666:
        # Invalid input
        valid_input_error_message()
        print_choices()
    else:
        print_choices()
    try:
        Case=input('Enter case number (1-7 or 99): ')
    except:
       Case=0
    if(Case in set(titles.keys()+[99])):
        return Case
    else:
        return choices(Case=666)
    print_choices()
def infinite_well_input(W=None,n=None):
    if W==None:
        try:
            W=float(raw_input('\nEnter the width of your infinite well in atomic units (a.u.).\n\tSelect a value between 0.5 and 15: '))
            W,n=infinite_well_input(W=W)
        except ValueError:
            valid_input_error_message()
            W,n=infinite_well_input()
    else:
        try:
            n=int(raw_input('Enter the number of wavefunctions you would like to plot.\n\tThis value must be an integer: '))
        except ValueError:
            valid_input_error_message()
            W,n=infinite_well_input(W=W)
    return W,n
def finite_well_input(W=None,D=None):
    if W==None:
        try:
            W=float(raw_input('\nEnter the width of your finite well in atomic units (a.u.).\n\tSelect a value between 1.0 and 15. '))
            W,D=finite_well_input(W=W)
        except ValueError:
            valid_input_error_message()
            W,D=finite_well_input()
    else:
        try:
            D=-float(raw_input('Enter the depth of your finite well in atomic units (a.u.).\n\tSelect a value between 20 and 500. '))
        except ValueError:
            valid_input_error_message()
            W,D=finite_well_input(W=W)
    return W,D
def double_finite_well_equal_depth_input(W=None,B=None,D=None):
    if W==None:
        try:
            print "\nThis case's plot is sensitive to the following user inputs.  Be aware that too wide/deep a well may prevent the user from observing the wave-like nature of the wavefunctions. Users should experiment with inputs until the desired plot is generated."
            W=float(raw_input('\nEnter the width of your finite wells in atomic units (a.u.). Select a value between 0.5 and 10. '))
            W,B,D=double_finite_well_equal_depth_input(W=W)
        except ValueError:
            valid_input_error_message()
            W,B,D=double_finite_well_equal_depth_input()
    elif D==None:
        try:
            D=-float(raw_input('\nEnter the depth of your finite wells in atomic units (a.u.). Select an integer value between 30 and 500. '))
            W,B,D=double_finite_well_equal_depth_input(W=W,D=D)
        except ValueError:
            valid_input_error_message()
            W,B,D=double_finite_well_equal_depth_input(W=W)
    else:
        try:
            B=float(raw_input('\nEnter the distance between potential wells in atomic units (a.u.). Select an integer value between 0.1 and 10. '))
        except ValueError:
            valid_input_error_message()
            W,B,D=double_finite_well_equal_depth_input(W=W,D=D)
    return W,B,D
def double_finite_well_unequal_depth_input(W1=None,W2=None,B=None,D1=None,D2=None):
    if W1==None:
        try:
            print "\nThis case's plot is sensitive to the following user inputs.  Be aware that too wide/deep a well may prevent the user from observing the wave-like nature of the wavefunctions. Users should experiment with inputs until the desired plot is generated."
            W1=float(raw_input('\nEnter the width of finite well 1 in atomic units (a.u.). Select a value between 0.5 and 10. '))
            W1,W2,B,D1,D2=double_finite_well_unequal_depth_input(W1=W1)
        except ValueError:
            valid_input_error_message()
            W1,W2,B,D1,D2=double_finite_well_unequal_depth_input()
    elif W2==None:
        try:
            W2=float(raw_input('\nEnter the width of finite well 2 in atomic units (a.u.). Select a value between 0.5 and 10. '))
            W1,W2,B,D1,D2=double_finite_well_unequal_depth_input(W1=W1,W2=W2)
        except ValueError:
            valid_input_error_message()
            W1,W2,B,D1,D2=double_finite_well_unequal_depth_input(W1=W1)
    elif B==None:
        try:
            B=float(raw_input('\nEnter the distance between potential wells in atomic units (a.u.). Select an integer value between 0.1 and 10. '))
            W1,W2,B,D1,D2=double_finite_well_unequal_depth_input(W1=W1,W2=W2, B=B)
        except ValueError:
            valid_input_error_message()
            W1,W2,B,D1,D2=double_finite_well_unequal_depth_input(W1=W1,W2=W2)
    elif D1==None:
        try:
            D1=-float(raw_input('\nEnter the depth of finite well 1 in atomic units (a.u.). Select an integer value between 30 and 500. '))
            W1,W2,B,D1,D2=double_finite_well_unequal_depth_input(W1=W1,W2=W2,B=B,D1=D1)
        except ValueError:
            valid_input_error_message()
            W1,W2,B,D1,D2=double_finite_well_unequal_depth_input(W1=W1,W2=W2,B=B)
    else:
        try:
            D2=-float(raw_input('\nEnter the depth of finite well 2 in atomic units (a.u.). Select an integer value between 30 and 500. '))
        except ValueError:
            valid_input_error_message()
            W1,W2,B,D1,D2=double_finite_well_unequal_depth_input(W1=W1,W2=W2,B=B,D1=D1)
    return W1,W2,B,D1,D2
def harmonic_well_input(omega=None,D=None):
    if omega==None:
        try:
            omega=float(raw_input('\nEnter the force constant of your harmonic well.\n\tSelect a value between 0.3 and 1.4. '))
            omega,D=harmonic_well_input(omega=omega)
        except ValueError:
            valid_input_error_message()
            omega,D=harmonic_well_input()
    else:
        try:
            D=-float(raw_input('Enter the depth of your harmonic well in atomic units (a.u.).\n\tSelect a value between 2 and 15. '))
        except ValueError:
            valid_input_error_message()
            omega,D=harmonic_well_input(omega=omega)
    return omega,D
def morse_well_input(omega=None,D=None):
    if omega==None:
        try:
            omega=float(raw_input('\nEnter the force constant of your morse well.\n\tSelect a value between 0.05 and 1.4. '))
            omega,D=morse_well_input(omega=omega)
        except ValueError:
            valid_input_error_message()
            omega,D=morse_well_input()
    else:
        try:
            D=-float(raw_input('Enter the depth of your morse well in atomic units (a.u.).\n\tSelect a value between 2 and 15. '))
        except ValueError:
            valid_input_error_message()
            omega,D=morse_well_input(omega=omega)
    return omega,np.abs(D)
def Kronig_Penney_input(A=None,D=None,B=None,num_wells=None):
    if A==None:
        try:
            A=float(raw_input('\nEnter the width of the repeating finite wells in atomic units (a.u.).\n\tSelect a value between 1.0 and 15. '))
            A,D,B,num_wells=Kronig_Penney_input(A=A)
        except ValueError:
            valid_input_error_message()
            A,D,B,num_wells = Kronig_Penney_input()
    elif D==None:
        try:
            D=-float(raw_input('Enter the depth of the repeating finite wells in atomic units (a.u.).\n\tSelect a value between 20 and 500. '))
            A,D,B,num_wells=Kronig_Penney_input(A=A,D=D)
        except ValueError:
            valid_input_error_message()
            A,D,B,num_wells=Kronig_Penney_input(A=A)
    elif B==None:
        try:
            B=float(raw_input('Enter the separation distance of the repeating finite wells in atomic units (a.u.).\n\tSelect a value between 1.0 and 15. '))
            A,D,B,num_wells=Kronig_Penney_input(A=A,D=D,B=B)
        except ValueError:
            valid_input_error_message()
            A,D,B,num_wells=Kronig_Penney_input(A=A,D=D)
    elif num_wells==None:
        try:
            num_wells=int(raw_input('Enter the number of repeating wells to use.\n\tSelect an odd integer between 3 and 7. '))
        except ValueError:
            valid_input_error_message()
            A,D,B,num_wells=Kronig_Penney_input(A=A,D=D,B=B)
    return A,D,B,num_wells
def ask_to_save_plot(error=False):
    if error==True:
        valid_input_error_message()
    try:
        image=raw_input('Would you like to save a .png image of your plot? Type yes or no. ')
    except:
        image=ask_to_save_plot(error=True)
    image=image.strip().lower()
    if image=='yes':
        print 'Your image will be saved in your current working directory.'
    if image not in {'yes','no'}:
        image=ask_to_save_plot(error=True)
    return image
def ask_to_plot_squared(error=False):
    if error==True:
        valid_input_error_message()
    try:
        sq=raw_input('Would you like to plot the probability density (psi squared) instead of the probability amplitude (psi)? Type yes or no. ')
    except:
        sq=ask_to_plot_squared(error=True)
    sq=sq.strip().lower()
    if sq not in {'yes','no'}:
        sq=ask_to_plot_squared(error=True)
    return sq
def print_number_of_wavefunctions(n):
    if print_color:
        print Fore.RED+'\nMaximum number of wavefunctions for plotting is', Fore.RED + str(n), "\n"
    else:
        print '\nMaximum number of wavefunctions for plotting is', n
def output(Case,input_fields,input_values,E,n):
    print ""
    print '*'*79
    print_center_text('Schrodinger Solver Output')
    print_center_text('Matthew Srnec and Shiv Upadhyay')
    print '*'*79
    print_center_text(titles[Case])
    print ""
    print "\t\tInput:"
    for i,j in zip(input_fields,input_values):
        print_center_text(str(i)+' : '+str(j))
    print ""
    print "\t\t{} lowest Bound States:".format(n)
    count=0
    for i in range(n):
        print_center_text('E({})='.format(i) + str(E[i]))
    print '*'*79
    print ""
########
# SHARED FUNCTIONS
########
def step_func(x):
    return 0.5*(1+np.sign(x))
def harmonic_potential(x,omega,D):
    pot=(0.5*(omega**2)*(x**2))+D
    for i in range(len(pot)):
        if pot[i]>0:
            pot[i]=0
    return pot
def morse_function(a,D,x):
    return D*(np.exp(-2*a*x)-2*np.exp(-a*x))
def morse_potential(omega,D,steps):
    D=np.abs(D)
    a=np.sqrt(omega/2.0*D)
    start=0.0
    stop=0.0
    while morse_function(a,D,start)<0.5*np.abs(D):
        start-=0.01
    while morse_function(a,D,stop)<-0.1:
        stop+=0.01
    # create x-vector
    xvec=np.linspace(2.0*start,2.0*stop,steps,dtype=np.float_)
    # get step size
    h=xvec[1]-xvec[0]
    pot=morse_function(a,D,xvec)
    for i in range(len(pot)):
        if pot[i]>0:
            pot[i]=0
    return xvec,h,pot
def diagonalize_hamiltonian(Hamiltonian):
    return spla.eigh(Hamiltonian)
########
# PLOTTING
########
def infinite_well_plot(E,V,xvec,W,steps,n,Case,ask_to_save=False,ask_squared=False):
    if ask_squared:
        sq=ask_to_plot_squared()
        if(sq=='yes'):
            V = np.multiply(np.conj(V),V)
    V_new,ScaleFactor=infinite_well_plot_scaling(E,V,xvec,W)
    # create the figure
    f=plt.figure()
    # add plot to the figure
    ax=f.add_subplot(111)
    # set x limit
    plt.xlim(-W,W)
    # determine how much to buffer the axes
    buff=(np.max(V_new[0:steps,n-1])-np.min(V_new[0:steps,n-1]))
    #set y limit
    plt.ylim(0,np.max(V_new[0:steps,n-1])+buff)
    #plot wave functions
    for i in np.arange(n-1,-1,-1):
        color=mpl.cm.jet_r((i)/(float)(n-1),1)
        wavefunc=ax.plot(xvec,V_new[0:steps,i],c=color,label='E(a.u.)={}'.format(np.round(E[i]*1000)/1000.0))
        ax.axhline(y=V_new[0,i],xmin=-20*W,xmax=20*W,c=color,ls='--')
    # set plot title
    ax.set_title('{}'.format(titles[Case]))
    # set x label
    plt.xlabel('Width of Well / (a.u.)')
    # set y label
    plt.ylabel('Energy / (a.u.)')
    # modify tick marks
    ax.set_yticklabels(np.round(ax.yaxis.get_ticklocs()*ScaleFactor))
    # add plot legend
    L=plt.legend(bbox_to_anchor=(1.05,1),loc=2,borderaxespad=0.)
    box=ax.get_position()
    ax.set_position([box.x0,box.y0,0.7*box.width,box.height])
    if ask_to_save:
        image=ask_to_save_plot()
        if(image=='yes'):
            f.savefig('Case{}.png'.format(Case),bbox_extra_artists=(L,),dpi=200,bbox_inches='tight')
    plt.show()
def finite_well_plot(E,V,xvec,steps,n,Case,U,ask_to_save=False,ask_squared=False):
    if ask_squared:
        sq=ask_to_plot_squared()
        if(sq=='yes'):
            V = np.multiply(np.conj(V),V)
    V_new,ScaleFactor,U_new,n=finite_well_plot_scaling(E,V,xvec,U,n,steps)
    # create the figure
    f=plt.figure()
    # add plot to the figure
    ax=f.add_subplot(111)
    # plot potential
    ax.plot(xvec,U_new,c='lightslategray')
    # find appropriate x limits and set x limit
    MinX=0
    MaxX=len(xvec)-1
    while U_new[MinX]==0:
        MinX=MinX+1
    while U_new[MaxX]==0:
        MaxX=MaxX-1
    for m in range(n):
        V_old=V_new[MinX+1,m]
        while(np.abs(V_old - V_new[MinX,m])>1e-6 and MinX>0):
            V_old=V_new[MinX,m]
            MinX=MinX-1
        V_old=V_new[MaxX-1,m]
        while(np.abs(V_old - V_new[MaxX,m])>1e-6 and MaxX<len(xvec)-1):
            V_old=V_new[MaxX,m]
            MaxX=MaxX+1
    plt.xlim(xvec[MinX],xvec[MaxX])
    # find appropriate y limits and set y limit
    if(np.max(V_new)>0):
        if(np.min(V_new)>np.min(U_new)):
            plt.ylim(1.05*np.min(U_new),np.max(V_new)+abs(0.05*np.min(U_new)))
        else:
            plt.ylim(1.05*np.min(V_new),np.max(V_new)+abs(0.05*np.min(U_new)))
    else:
        if(np.min(V_new)>np.min(U_new)):
            plt.ylim(1.05*np.min(U_new),np.max(U_new)+abs(0.05*np.min(U_new)))
        else:
            plt.ylim(1.05*np.min(V_new),np.max(U_new)+abs(0.05*np.min(U_new)))
    #plot wave functions
    for i in np.arange(n-1,-1,-1):
        color=mpl.cm.jet_r((i)/(float)(n),1)
        wavefunc=ax.plot(xvec,V_new[0:steps,i],c=color,label='E(a.u.)={}'.format(np.round(E[i]*1000)/1000.0))
        ax.axhline(y=V_new[0,i],xmin=-10,xmax=10,c=color,ls='--')
    # set plot title
    ax.set_title('{}'.format(titles[Case]))
    # set x label
    plt.xlabel('Width of Well / (a.u.)')
    # set y label
    plt.ylabel('Energy / (a.u.)')
    # modify tick marks
    ax.set_yticklabels(np.round(ax.yaxis.get_ticklocs()*ScaleFactor))
    # add plot legend
    L=plt.legend(bbox_to_anchor=(1.05,1),loc=2,borderaxespad=0.)
    box=ax.get_position()
    ax.set_position([box.x0,box.y0,0.7*box.width,box.height])
    if ask_to_save:
        image=ask_to_save_plot()
        if(image=='yes'):
            f.savefig('Case{}.png'.format(Case),bbox_extra_artists=(L,),dpi=200,bbox_inches='tight')
    plt.show()
def Kronig_Penney_Plot(E,V,xvec,steps,n,Case,U,ask_to_save=False,ask_squared=False):
    if ask_squared:
        sq=ask_to_plot_squared()
        if(sq=='yes'):
            V = np.multiply(np.conj(V),V)
    V_new,ScaleFactor,U_new,n=finite_well_plot_scaling(E,V,xvec,U,n,steps)
    # create the figure
    f=plt.figure()
    # add plot to the figure
    ax=f.add_subplot(111)
    # plot potential
    ax.plot(xvec,U_new,c='lightslategray')
    # find appropriate x limits and set x limit
    MinX=0
    MaxX=len(xvec)-1
    while U_new[MinX]==0:
        MinX=MinX+1
    while U_new[MaxX]==0:
        MaxX=MaxX-1
    for m in range(n):
        V_old=V_new[MinX+1,m]
        while(np.abs(V_old - V_new[MinX,m])>1e-6 and MinX>0):
            V_old=V_new[MinX,m]
            MinX=MinX-1
        V_old=V_new[MaxX-1,m]
        while(np.abs(V_old - V_new[MaxX,m])>1e-6 and MaxX<len(xvec)-1):
            V_old=V_new[MaxX,m]
            MaxX=MaxX+1
    plt.xlim(xvec[MinX],xvec[MaxX])
    # find appropriate y limits and set y limit
    if(np.max(V_new)>0):
        if(np.min(V_new)>np.min(U_new)):
            plt.ylim(1.05*np.min(U_new),np.max(V_new)+abs(0.05*np.min(U_new)))
        else:
            plt.ylim(1.05*np.min(V_new),np.max(V_new)+abs(0.05*np.min(U_new)))
    else:
        if(np.min(V_new)>np.min(U_new)):
            plt.ylim(1.05*np.min(U_new),np.max(U_new)+abs(0.05*np.min(U_new)))
        else:
            plt.ylim(1.05*np.min(V_new),np.max(U_new)+abs(0.05*np.min(U_new)))
    #plot wave functions
    for i in np.arange(n-1,-1,-1):
        color=mpl.cm.jet_r((i)/(float)(n),1)
        wavefunc=ax.plot(xvec,V_new[0:steps,i],c=color,label='E(a.u.)={}'.format(np.round(E[i]*1000)/1000.0))
        ax.axhline(y=V_new[0,i],xmin=-10,xmax=10,c=color,ls='--')
    # set plot title
    ax.set_title('{}'.format(titles[Case]))
    # set x label
    plt.xlabel('Width of Well / (a.u.)')
    # set y label
    plt.ylabel('Energy / (a.u.)')
    # modify tick marks
    ax.set_yticklabels(np.round(ax.yaxis.get_ticklocs()*ScaleFactor))
    # add plot legend
    L=plt.legend(bbox_to_anchor=(1.05,1),loc=2,borderaxespad=0.)
    box=ax.get_position()
    ax.set_position([box.x0,box.y0,0.7*box.width,box.height])
    if ask_to_save:
        image=ask_to_save_plot()
        if(image=='yes'):
            f.savefig('Case{}.png'.format(Case),bbox_extra_artists=(L,),dpi=200,bbox_inches='tight')
    plt.show()
def infinite_well_plot_scaling(E,V,xvec,W):
    # scale the wave functions
    ScaleFactorStep=0.05
    ScaleFactor=1.00
    MaxV2=np.amax(V[1])
    MinV2=np.amin(V[1])
    MaxV1=np.amax(V[0])
    while((MaxV2-MinV2)<np.abs(MinV2-MaxV1)*10.0):
        MaxV2=np.amax(V[1])+E[1]/ScaleFactor
        MinV2=np.amin(V[1])+E[1]/ScaleFactor
        MaxV1=np.amax(V[0])+E[0]/ScaleFactor
        ScaleFactor+=ScaleFactorStep
    V_new=(E/ScaleFactor)+V
    return V_new,ScaleFactor
def finite_well_plot_scaling(E,V,xvec,U,n,steps):
    # scale the wave functions
    order=np.argsort(E)
    Converged=False
    while(Converged is False):
        E_copy=E[0:n]
        V_copy=V[0:steps,order]
        V_copy=V[0:steps,0:n]
        max_E_diff = E_copy[n-1] - E_copy[0]
        found_step = False
        step = 1
        while found_step is False:
            if(E_copy[step]-E_copy[0]<0.2):
                step+=1
            else:
                found_step = True
        ScaleFactorStep=0.05
        ScaleFactor=1.00
        Overlap=1
        while(Overlap==1):
            for i in range(0,n,step):
                MaxV2=np.max(V_copy[0:steps,i])+E_copy[i]/ScaleFactor
                MinV2=np.min(V_copy[0:steps,i])+E_copy[i]/ScaleFactor
                MaxV1=np.max(V_copy[0:steps,i-step])+E_copy[i-step]/ScaleFactor
                if((MaxV2-MinV2)<(np.abs(MinV2-MaxV1)*10)):
                    Overlap=1
                else:
                    Overlap=0
                    break
            ScaleFactor=ScaleFactor+ScaleFactorStep
        V_copy_new=(E_copy/ScaleFactor)+V_copy
        if np.max(V_copy_new[n])>0:
            Converged=True
            n=n-1
        else:
            n=n+1
        V_copy_old=V_copy_new
    V_new=V_copy_old
    U_new=U/ScaleFactor
    return V_new,ScaleFactor,U_new,n

if __name__ == "__main__":
    print "\nSchrodinger utils file. This file was not meant to be run independently."
