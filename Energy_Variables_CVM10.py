Adjust_Scale = {
    'Active_Energy_kWh': 1,
    'Active_Energy_Wh': 1000,
    'Reactive_Inductive_Energy_kVArh': 1,
    'Reactive_Inductive_Energy_VArh': 1000,
    'Reactive_Capacitive_Energy_kVArh': 1,
    'Reactive_Capacitive_Energy_VArh': 1000,
    'Aparent_Energy_kVAh': 1,
    'Aparent_Energy_VAh': 1000,
    'CO2_Consumption': 10,
}

# ---------------- Energy Consumption --------------------

Energy_Consumption_Line_A = {
    'Active_Energy_kWh': b'\x00\x5E',
    'Active_Energy_Wh': b'\x00\x60',
    'Reactive_Inductive_Energy_kVArh': b'\x00\x62',
    'Reactive_Inductive_Energy_VArh': b'\x00\x64',
    'Reactive_Capacitive_Energy_kVArh': b'\x00\x66',
    'Reactive_Capacitive_Energy_VArh': b'\x00\x68',
    'Aparent_Energy_kVAh': b'\x00\x6A',
    'Aparent_Energy_VAh': b'\x00\x6C',
    'CO2_Consumption': b'\x00\x6E',
}

Energy_Consumption_Line_B = {
    'Active_Energy_kWh': b'\x00\x88',
    'Active_Energy_Wh': b'\x00\x8A',
    'Reactive_Inductive_Energy_kVArh': b'\x00\x8C',
    'Reactive_Inductive_Energy_VArh': b'\x00\x8E',
    'Reactive_Capacitive_Energy_kVArh': b'\x00\x90',
    'Reactive_Capacitive_Energy_VArh': b'\x00\x92',
    'Aparent_Energy_kVAh': b'\x00\x94',
    'Aparent_Energy_VAh': b'\x00\x96',
    'CO2_Consumption': b'\x00\x98',
}

Energy_Consumption_Line_C = {
    'Active_Energy_kWh': b'\x00\xB2',
    'Active_Energy_Wh': b'\x00\xB4',
    'Reactive_Inductive_Energy_kVArh': b'\x00\xB6',
    'Reactive_Inductive_Energy_VArh': b'\x00\xB8',
    'Reactive_Capacitive_Energy_kVArh': b'\x00\xBA',
    'Reactive_Capacitive_Energy_VArh': b'\x00\xBC',
    'Aparent_Energy_kVAh': b'\x00\xBE',
    'Aparent_Energy_VAh': b'\x00\xC0',
    'CO2_Consumption': b'\x00\xC2',
}

Energy_Consumption_Total = {
    'Active_Energy_kWh': b'\x00\xDC',
    'Active_Energy_Wh': b'\x00\xDE',
    'Reactive_Inductive_Energy_kVArh': b'\x00\xE0',
    'Reactive_Inductive_Energy_VArh': b'\x00\xE2',
    'Reactive_Capacitive_Energy_kVArh': b'\x00\xE4',
    'Reactive_Capacitive_Energy_VArh': b'\x00\xE6',
    'Aparent_Energy_kVAh': b'\x00\xE8',
    'Aparent_Energy_VAh': b'\x00\xEA',
    'CO2_Consumption': b'\x00\xEC',
}

# ---------------- Energy Generated --------------------

Energy_Generated_Line_A = {
    'Active_Energy_kWh': b'\x00\x72',
    'Active_Energy_Wh': b'\x00\x74',
    'Reactive_Inductive_Energy_kVArh': b'\x00\x76',
    'Reactive_Inductive_Energy_VArh': b'\x00\x78',
    'Reactive_Capacitive_Energy_kVArh': b'\x00\x7A',
    'Reactive_Capacitive_Energy_VArh': b'\x00\x7C',
    'Aparent_Energy_kVAh': b'\x00\x7E',
    'Aparent_Energy_VAh': b'\x00\x80',
    'CO2_Consumption': b'\x00\x82',
}

Energy_Generated_Line_B = {
    'Active_Energy_kWh': b'\x00\x9C',
    'Active_Energy_Wh': b'\x00\x9E',
    'Reactive_Inductive_Energy_kVArh': b'\x00\xA0',
    'Reactive_Inductive_Energy_VArh': b'\x00\xA2',
    'Reactive_Capacitive_Energy_kVArh': b'\x00\xA4',
    'Reactive_Capacitive_Energy_VArh': b'\x00\xA6',
    'Aparent_Energy_kVAh': b'\x00\xA8',
    'Aparent_Energy_VAh': b'\x00\xAA',
    'CO2_Consumption': b'\x00\xAC',
}

Energy_Generated_Line_C = {
    'Active_Energy_kWh': b'\x00\xC6',
    'Active_Energy_Wh': b'\x00\xC8',
    'Reactive_Inductive_Energy_kVArh': b'\x00\xCA',
    'Reactive_Inductive_Energy_VArh': b'\x00\xCC',
    'Reactive_Capacitive_Energy_kVArh': b'\x00\xCE',
    'Reactive_Capacitive_Energy_VArh': b'\x00\xD0',
    'Aparent_Energy_kVAh': b'\x00\xD2',
    'Aparent_Energy_VAh': b'\x00\xD4',
    'CO2_Consumption': b'\x00\xD6',
}

Energy_Generated_Total = {
    'Active_Energy_kWh': b'\x00\xF0',
    'Active_Energy_Wh': b'\x00\xF2',
    'Reactive_Inductive_Energy_kVArh': b'\x00\xF4',
    'Reactive_Inductive_Energy_VArh': b'\x00\xF6',
    'Reactive_Capacitive_Energy_kVArh': b'\x00\xF8',
    'Reactive_Capacitive_Energy_VArh': b'\x00\xFA',
    'Aparent_Energy_kVAh': b'\x00\xFC',
    'Aparent_Energy_VAh': b'\x00\xFE',
    'CO2_Consumption': b'\x01\x00',
}
