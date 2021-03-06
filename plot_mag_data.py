import numpy as np
import matplotlib.pyplot as plt

sep = '\t'

mag_input_file = str(snakemake.input[0])
sus_input_file = str(snakemake.input[1])

mag_output_file = str(snakemake.output[0])
sus_output_file = str(snakemake.output[1])

mag_data = np.genfromtxt(mag_input_file, skip_header=1)
sus_data = np.genfromtxt(sus_input_file, skip_header=1, usecols=1)

temps = mag_data[:,0]
m_z = mag_data[:,1]
m = mag_data[:,2]
m_bloch = mag_data[:,3]
m_bloch_bulk = mag_data[:,4]

plt.figure()

title = str(snakemake.params[0]) + " " + str(snakemake.params[1]) + " layers; H_z = " + str(snakemake.params[3]) + ", mu_s = " + str(snakemake.params[4])

plt.title(title)
plt.xlabel("Temperature (K)")
plt.ylabel("Magnetisation (T)")

plt.scatter(temps, m_z, label='JAMS M_z', color='red', marker='x')
plt.scatter(temps, m, label='JAMS |M|', color='blue', marker='x')
plt.plot(temps, m_bloch, label='Bloch\'s law (thin film)')
plt.plot(temps, m_bloch_bulk, label='Bloch\'s law (bulk)')
plt.legend()

plt.savefig(mag_output_file)

plt.figure()

plt.title("Susceptibility vs. temperature")
plt.xlabel("Temperature (K)")
plt.ylabel("Temperature-normalised susceptibility (T^2)")

plt.scatter(temps, sus_data, color='red', marker='x')

plt.savefig(sus_output_file)
