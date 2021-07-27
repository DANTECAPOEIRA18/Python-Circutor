import os

if os.environ.get('ENV') == 'Development':
    DATA_ENERGY_ROUTE = '/mnt/c/Users/dante/Desktop/DataBases/circutor/energy_data/'
    DATA_ELECTRIC_ROUTE = '/mnt/c/Users/dante/Desktop/DataBases/circutor/electric_data/'
    DATA_HARMONIC_ROUTE = '/mnt/c/Users/dante/Desktop/DataBases/circutor/harmonic_data/'
    DATABASE_ROUTE = '/mnt/c/Users/dante/Desktop/DataBases/circutor/CVM.sqlite'
    SERIAL_PORT = '/dev/ttyS7'
else:
    DATA_ENERGY_ROUTE = '/root/energy_data/'
    DATA_ELECTRIC_ROUTE = '/root/electric_data/'
    DATA_HARMONIC_ROUTE = '/root/harmonic_data/'
    DATABASE_ROUTE = '/root/CVM.sqlite'
    SERIAL_PORT = '/dev/ttyUSB0'

os.environ.__setitem__('DATA_ENERGY_ROUTE', DATA_ENERGY_ROUTE)
os.environ.__setitem__('DATA_ELECTRIC_ROUTE', DATA_ELECTRIC_ROUTE)
os.environ.__setitem__('DATA_HARMONIC_ROUTE', DATA_HARMONIC_ROUTE)
os.environ.__setitem__('DATABASE_ROUTE', DATABASE_ROUTE)
os.environ.__setitem__('SERIAL_PORT', SERIAL_PORT)
