import numpy as np
import netCDF4 as nc
import sys

fullfilename = sys.argv[1];
filename = fullfilename.split('.')
filename = filename[0]
point = int(filename[2:4])
month = int(filename[0:2])
density = float(filename[4:6])


def csv_to_netcdf(csv_file, nc_file, Description, Density, Month):

    parameters_data = ['evap_vol', 'disp_vol', 'rem_vol', 'oil_dens', 'oil_vis', 'sw_content']
    
    long_name_data = dict(zip(parameters_data, ['evaporation volume', 'dispersion volume', 'remaining volume', 'oil density', 'oil viscosity', 'seawater content']))
    
    units_data = dict(zip(parameters_data, ['m^3', 'm^3', 'm^3', 'kg m^{-1}', 'cSt', 'percent']))

    data = np.genfromtxt(csv_file, delimiter=';', dtype=None, skip_header=0, encoding=None, names=['time', 'evap_vol', 'disp_vol', 'rem_vol', 'oil_dens', 'oil_vis', 'sw_content'])

    with nc.Dataset(nc_file, 'w', format="NETCDF4") as ds:

        time = data['time']
        ds.createDimension('time', len(time))
        time_var = ds.createVariable('time', 'f4', ('time',))
        time_var.units = 'hours'
        time_var.calendar = 'standard'
        time_var.long_name = 'Time in hours'
        time_var[:] = time

        for param in parameters_data:
            param_var = ds.createVariable(param, 'f4', ('time',))
            param_var.long_name = long_name_data[param]
            param_var.units = units_data[param]
            param_var.missing_value = np.nan
            param_var[:] = data[param]
    
        ds.description = 'Point: P' + str(point)
        ds.Oil_density = str(Density) + "°API"
        ds.Month = str(Month)

    print(f'Successfully converted CSV to netCDF. Saved to: {nc_file}')
    

csv_to_netcdf(fullfilename, filename + '.nc', point, density, month)

