Adjust_Scale = {
    'Voltage': 10,
    'Current': 1000,
    'Active_Power': 1000,
    'Inductive_Power': 1000,
    'Capacitive_Power': 1000,
    'Aparent_Power': 1000,
    'Power_Factor': 100,
    'CosFi': 100,
    'THDv': 10,
    'THDi': 10,
    'Frecuency': 100,
    'Neutral_Current': 1000,
    'Voltage_AB': 10,
    'Voltage_BC': 10,
    'Voltage_CA': 10,
    'Total_Active_Power': 1000,
    'Total_Inductive_Power': 1000,
    'Total_Capacitive_Power': 1000,
    'Total_Aparent_Power': 1000,
    'Total_Power_Factor': 100,
    'Total_CosFi': 100,
}

Power_State_Selector = {
    '1': 'Energía Consumida puramente Resistiva',
    '2': 'Energía Generada puramente Resistiva',
    '5': 'Energía Consumida Inductiva',
    '6': 'Energía Generada Inductiva',
    '9': 'Energía Consumida Capacitiva',
    '10': 'Energía Generada Capacitiva',
}

Line_A = {
    'Voltage': b'\x00\x00',
    'Current': b'\x00\x02',
    'Active_Power': b'\x00\x04',
    'Inductive_Power': b'\x00\x06',
    'Capacitive_Power': b'\x00\x08',
    'Aparent_Power': b'\x00\x0A',
    'Power_Factor': b'\x00\x0C',
    'CosFi': b'\x00\x0E',
    'THDv': b'\x00\x46',
    'THDi': b'\x00\x4C',
}

Line_B = {
    'Voltage': b'\x00\x10',
    'Current': b'\x00\x12',
    'Active_Power': b'\x00\x14',
    'Inductive_Power': b'\x00\x16',
    'Capacitive_Power': b'\x00\x18',
    'Aparent_Power': b'\x00\x1A',
    'Power_Factor': b'\x00\x1C',
    'CosFi': b'\x00\x1E',
    'THDv': b'\x00\x48',
    'THDi': b'\x00\x4E',
}

Line_C = {
    'Voltage': b'\x00\x20',
    'Current': b'\x00\x22',
    'Active_Power': b'\x00\x24',
    'Inductive_Power': b'\x00\x26',
    'Capacitive_Power': b'\x00\x28',
    'Aparent_Power': b'\x00\x2A',
    'Power_Factor': b'\x00\x2C',
    'CosFi': b'\x00\x2E',
    'THDv': b'\x00\x4A',
    'THDi': b'\x00\x50',
}

ThreePhase_Variables = {
    'Voltage_AB': b'\x00\x3E',
    'Voltage_BC': b'\x00\x40',
    'Voltage_CA': b'\x00\x42',
    'Total_Active_Power': b'\x00\x30',
    'Total_Inductive_Power': b'\x00\x32',
    'Total_Capacitive_Power': b'\x00\x34',
    'Total_Aparent_Power': b'\x00\x36',
    'Total_Power_Factor': b'\x00\x38',
    'Total_CosFi': b'\x00\x3A',
}

Frecuency = b'\x00\x3C'
Neutral_Current = b'\x00\x44'
Power_State = b'\x07\xD1'
