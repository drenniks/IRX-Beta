import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import numpy as np
from scipy import integrate
import corner
import random
import emcee
import scipy.optimize as op

file = open("skirt_data.dat", "w")

#file = open("skirt_test_data.py", "w")
#numbers =  [18, 23, 24, 25, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50, 51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75, 76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99, 100, 102, 103, 104, 105, 106, 107, 108, 109, 110, 112, 113, 114, 115, 116, 117, 118, 119, 120, 121, 122, 123, 124, 125, 126, 127, 128, 129, 130, 131, 132, 133, 134, 135, 137, 138, 139, 140, 141, 142, 143, 144, 145, 146, 147, 148, 149, 151, 152, 153, 154, 155, 157, 158, 159, 160, 161, 162, 163, 164, 165, 166, 167, 169, 170, 171, 172, 173, 174, 175, 176, 177, 178, 179, 180, 181, 186, 187, 188, 189, 190, 191, 192, 193, 194, 196, 197, 198, 199, 200, 201, 202, 204, 206, 207, 208, 209, 210, 213, 214, 215, 216, 218, 219, 222, 223, 224, 225, 226, 229, 230, 232, 233, 234, 235, 236, 237, 239, 242, 244, 245, 247, 249, 252, 253, 254, 258, 260, 264, 265, 266, 273, 276, 283, 304, 310, 335]
numbers = [38]
UV1 = .15
UV2 = .26

def lnlike(theta, x, y, yerr):
        m, b= theta
        model = m*x + b
        return -1.*np.sum(np.log10((y-model)**2))

def lnprior(theta):
        m, b = theta
        if -4 < m < 0:
            return 0.0
        return -np.inf

def lnprob(theta, x, y, yerr):
        lp = lnprior(theta)
        if not np.isfinite(lp):
            return -np.inf
        return lp + lnlike(theta, x, y, yerr)

ndim, nwalkers = 2, 1000

xl = np.log10(np.array([UV1, UV2]))

for i in range(len(numbers)):
    data = np.genfromtxt('/oasis/scratch/comet/drenniks/temp_project/IRX/z_0/Zubko_'+ str(numbers[i])+ '_i00_sed.dat', names = ['wave','flux'], skip_header = 2)
    print 'you are on halo ' + str(numbers[i])
    wavelength = data['wave']
    scattered_emission = data['flux']
    window1 = (wavelength > .1268) & (wavelength < .1284)
    window2 = (wavelength > .1309) & (wavelength < .1316)
    window3 = (wavelength > .1342) & (wavelength < .1371)
    window4 = (wavelength > .1407) & (wavelength < .1515)
    window5 = (wavelength > .1562) & (wavelength < .1583)
    window6 = (wavelength > .1677) & (wavelength < .1740)
    window7 = (wavelength > .1760) & (wavelength < .1833)
    window8 = (wavelength > .1866) & (wavelength < .1890)
    window9 = (wavelength > .1930) & (wavelength < .1950)
    window10 = (wavelength > .2400) & (wavelength < .2580)
    fitting_windows = window1 + window2 + window3 + window4 + window5 + window6 + window7 + window8 + window9 + window10

    UVrange = fitting_windows
    IRrange = (wavelength > 15) & (wavelength < 1000)
    window_UV = (wavelength > .1425) & (wavelength < .1775)

    xIR = wavelength[IRrange]
    yIR = scattered_emission[IRrange]
    yintIR = integrate.cumtrapz(yIR, xIR)
    
    xUV = wavelength[UVrange]
    xUV_int = wavelength[window_UV]
    yUV = scattered_emission[UVrange]
    yintUV = integrate.cumtrapz(yUV, xUV)
    
    #Caluclating IRX
    yIRX = scattered_emission[IRrange]/(xIR/1e6)
    yintIRX = integrate.cumtrapz(yIRX, xIR)
    yUVX = scattered_emission[window_UV]/(xUV_int/1e6)
    yintUVX = integrate.cumtrapz(yUVX, xUV_int)
    FIR = yintIRX[-1]
    FUV = yintUVX[-1]
    IRx = FIR/FUV
    
    #Fit a line to the UVrange to find an initial fit
    slope, intercept = np.polyfit(np.log10(xUV), np.log10(yUV), 1)
    z = np.polyfit(np.log10(xUV), np.log10(yUV), 1)
    f = np.poly1d(z)
    x_new = np.linspace(np.log10(xUV[0]), np.log10(xUV[-1]), 22)
    y_new = f(x_new)
    m_true = slope
    b_true = intercept
    
    plt.plot(np.log10(xUV), np.log10(yUV))
    plt.plot(x_new, y_new)
    plt.savefig('/oasis/scratch/comet/drenniks/temp_project/IRX/z_0/images/check_slope_' + str(numbers[i]) + '.png') 
    x = np.log10(xUV)
    y = np.log10(yUV)
    yerr = np.zeros(len(x)) + 1e-10
    
    #Finding a linear least squares solution
    A = np.vstack((np.ones_like(x), x)).T
    C = np.diag(yerr * yerr)
    cov = np.linalg.inv(np.dot(A.T, np.linalg.solve(C, A)))
    b_ls, m_ls = np.dot(cov, np.dot(A.T, np.linalg.solve(C, y)))
    yfit = m_ls*x + b_ls
    
    #Making a maximum likelihood estimation
    nll = lambda *args: -lnlike(*args)
    result = op.minimize(nll, [m_true, b_true], args = (x, y, yerr))
    m_ml, b_ml = result["x"]
    
    #Marginalization & uncertainty estimation - MCMC
    pos = [result["x"] + 1e-4*np.random.randn(ndim) for j in range(nwalkers)]
    sampler = emcee.EnsembleSampler(nwalkers, ndim, lnprob, args=(x,y, yerr))
    sampler.run_mcmc(pos, 1000)
    
    #Plotting walkers as a function of time
    fig, axes = plt.subplots(2, 1, sharex = True, figsize = (8,9))
    axes[0].plot(sampler.chain[:, :, 0].T, color="k", alpha=0.4)
    axes[0].axhline(m_true, color = "#888888", lw = 2)
    axes[0].set_ylabel ("$m$")
    axes[1].plot(sampler.chain[:, :, 1].T, color="k", alpha=0.4)
    axes[1].axhline(b_true,color ="#888888", lw =2)
    axes[1].set_ylabel ("$b$")
    fig.tight_layout(h_pad=0.0)
    fig.savefig("/oasis/scratch/comet/drenniks/temp_project/IRX/z_0/images/line-time_" + str(numbers[i]) + ".png")
    fig.clf()
    
    samples = sampler.chain[:, 50:, :].reshape((-1,ndim))
    
    #Plotting the corner plot
    fig = corner.corner(samples, labels = ["$m$", "$b$"], truths = [m_true, b_true], plot_contours = False)
    fig.savefig("/oasis/scratch/comet/drenniks/temp_project/IRX/z_0/images/corner_" + str(numbers[i]) + ".png")
    fig.clf()

    #Plotting the projection of the results onto the dataset
    fig, axes = plt.subplots(1)
    for m, b in samples[np.random.randint(len(samples), size=100)]:
        axes.plot(xl, m*xl+b, color = "k", alpha = 0.1)
        axes.plot(xl, m_true*xl+b_true, color = "r", alpha = 0.8)
        axes.errorbar(x,y, yerr=yerr, fmt = ".k")
    fig.savefig("/oasis/scratch/comet/drenniks/temp_project/IRX/z_0/images/proj_results_" + str(numbers[i]) + ".png")
    fig.clf()
    
    m_mcmc, b_mcmc = map(lambda v: (v[1], v[2]-v[1], v[1]-v[0]), zip(*np.percentile(samples, [16, 50, 84], axis=0)))
    
    file.write(str(numbers[i]) + ' ' + str(IRx) + ' ' + str(m_mcmc) + ' ' + str(b_mcmc) + '\n')
    plt.close(fig)

file.close()
