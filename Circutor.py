import CVM10
import Measure_Variables_CVM10 as General
import Energy_Variables_CVM10 as Energy
import Harmonic_Variables as Harmonic
from datetime import datetime


class Circutor_Data:
    def __init__(self):
        self.Electric_Variables = CVM10.CVM_C10()
        self.Quantity = b'\x00\x02'
        self.Quantity2B = b'\x00\x01'

    def JSON_Data(self, address, scale, Quantity, topic, data_4B):
        length = (Quantity[1] * 2) + 5
        response = self.Electric_Variables.CVM_C10_data(address, Quantity, length)
        if data_4B:
            Variable = self.Electric_Variables.value_data_4B(response, scale)
        else:
            Variable = self.Electric_Variables.value_data_2B(response, scale)
        return {'topic': topic, 'payload': Variable}

    def Version_CVM10(self):
        length = (self.Quantity[1] * 2) + 5
        response = self.Electric_Variables.CVM_C10_data(b'\x05\x78', self.Quantity, length)
        return 'Versión(' + str(response[3:7], 'utf-8') + ').'

    def Power_State(self):
        power_state = self.JSON_Data(General.Power_State, 1, self.Quantity2B, 'power_state', False)
        State = str(int(power_state['payload']))
        return {'topic': power_state['topic'], 'payload': General.Power_State_Selector[State]}

    def Energy_Data(self, topic_measure, scale, Quantity):
        length = (Quantity[1] * 2) + 5
        Variable = {}
        for data in topic_measure:
            response = self.Electric_Variables.CVM_C10_data(topic_measure[data], Quantity, length)
            Variable[data] = self.Electric_Variables.value_data_4B(response, scale[data])

        Data_Energy = {
            'Active_Energy': {'topic': 'Active_Energy',
                              'payload': Variable['Active_Energy_kWh'] + Variable['Active_Energy_Wh']},
            'Reactive_Inductive_Energy': {'topic': 'Reactive_Inductive_Energy',
                                          'payload': Variable['Reactive_Inductive_Energy_kVArh'] + Variable[
                                              'Reactive_Inductive_Energy_VArh']},
            'Reactive_Capacitive_Energy': {'topic': 'Reactive_Capacitive_Energy',
                                           'payload': Variable['Reactive_Capacitive_Energy_kVArh'] + Variable[
                                               'Reactive_Capacitive_Energy_VArh']},
            'Aparent_Energy': {'topic': 'Aparent_Energy',
                               'payload': Variable['Aparent_Energy_kVAh'] + Variable['Aparent_Energy_VAh']},
            'CO2': {'topic': 'CO2', 'payload': Variable['CO2_Consumption']},
        }

        return Data_Energy

    def General_data(self, topic_measure, scale):
        Variable = {}
        for data in topic_measure:
            Variable[data] = self.JSON_Data(topic_measure[data], scale[data], self.Quantity, data, True)
        return Variable

    def Harmonic_packet(self, topic_measure, scale, limit_harmonic):
        Variable = {}
        harmonic = str(limit_harmonic + 1) + 'th'
        for data in Harmonic.Voltage_Harmonic_Line_A:
            if data == 'Fundamental':
                Variable[data] = self.JSON_Data(topic_measure[data], scale[data], self.Quantity, data, True)
            else:
                Variable[data] = self.JSON_Data(topic_measure[data], scale[data], self.Quantity2B, data, False)
            if data == harmonic:
                break

        return Variable

    def General_Measurements(self, type_meter):
        General_Variables = {}
        General_Variables['Frecuency'] = self.JSON_Data(General.Frecuency, General.Adjust_Scale['Frecuency'],
                                                        self.Quantity, 'Frecuency', True)
        General_Variables['Neutral_Current'] = self.JSON_Data(General.Neutral_Current,
                                                              General.Adjust_Scale['Neutral_Current'], self.Quantity,
                                                              'Neutral_Current', True)

        General_Variables['power_state'] = self.Power_State()

        if type_meter == 1 or type_meter == 2 or type_meter == 3:
            General_Variables['line_A'] = self.General_data(General.Line_A, General.Adjust_Scale)

        if type_meter == 2 or type_meter == 3:
            General_Variables['line_B'] = self.General_data(General.Line_B, General.Adjust_Scale)

        if type_meter == 3:
            General_Variables['line_C'] = self.General_data(General.Line_C, General.Adjust_Scale)
            General_Variables['Treephase_Data'] = self.General_data(General.ThreePhase_Variables, General.Adjust_Scale)

        General_Variables['localTimestamp'] = round(datetime.now().timestamp())

        return General_Variables

    def Harmonic_Measurements(self, type_meter, limit_harmonic):

        Harmonic_data = {}

        if type_meter == 1 or type_meter == 2 or type_meter == 3:
            Harmonic_data['Harmonic_Voltage_A'] = self.Harmonic_packet(Harmonic.Voltage_Harmonic_Line_A,
                                                                       Harmonic.Adjust_Scale, limit_harmonic)
            Harmonic_data['Harmonic_Current_A'] = self.Harmonic_packet(Harmonic.Current_Harmonic_Line_A,
                                                                       Harmonic.Adjust_Scale, limit_harmonic)

        if type_meter == 2 or type_meter == 3:
            Harmonic_data['Harmonic_Voltage_B'] = self.Harmonic_packet(Harmonic.Voltage_Harmonic_Line_B,
                                                                       Harmonic.Adjust_Scale, limit_harmonic)
            Harmonic_data['Harmonic_Current_B'] = self.Harmonic_packet(Harmonic.Current_Harmonic_Line_B,
                                                                       Harmonic.Adjust_Scale, limit_harmonic)

        if type_meter == 3:
            Harmonic_data['Harmonic_Voltage_C'] = self.Harmonic_packet(Harmonic.Voltage_Harmonic_Line_C,
                                                                       Harmonic.Adjust_Scale, limit_harmonic)
            Harmonic_data['Harmonic_Current_C'] = self.Harmonic_packet(Harmonic.Current_Harmonic_Line_C,
                                                                       Harmonic.Adjust_Scale, limit_harmonic)

        Harmonic_data['localTimestamp'] = round(datetime.now().timestamp())

        return Harmonic_data

    def Energy_Measurements(self, type_meter, bidirectional):

        Energy_Variables = {}

        if type_meter == 1 or type_meter == 2 or type_meter == 3:
            Energy_Variables['Energy_Consumption_Line_A'] = self.Energy_Data(Energy.Energy_Consumption_Line_A,
                                                                             Energy.Adjust_Scale,
                                                                             self.Quantity)
        if type_meter == 2 or type_meter == 3:
            Energy_Variables['Energy_Consumption_Line_B'] = self.Energy_Data(Energy.Energy_Consumption_Line_B,
                                                                             Energy.Adjust_Scale,
                                                                             self.Quantity)
            Energy_Variables['Energy_Consumption_Total'] = self.Energy_Data(Energy.Energy_Consumption_Total,
                                                                            Energy.Adjust_Scale,
                                                                            self.Quantity)
        if type_meter == 3:
            Energy_Variables['Energy_Consumption_Line_C'] = self.Energy_Data(Energy.Energy_Consumption_Line_C,
                                                                             Energy.Adjust_Scale,
                                                                             self.Quantity)

        if bidirectional:
            if type_meter == 1 or type_meter == 2 or type_meter == 3:
                Energy_Variables['Energy_Generated_Line_A'] = self.Energy_Data(Energy.Energy_Generated_Line_A,
                                                                               Energy.Adjust_Scale,
                                                                               self.Quantity)
            if type_meter == 2 or type_meter == 3:
                Energy_Variables['Energy_Generated_Line_B'] = self.Energy_Data(Energy.Energy_Generated_Line_B,
                                                                               Energy.Adjust_Scale,
                                                                               self.Quantity)
                Energy_Variables['Energy_Generated_Total'] = self.Energy_Data(Energy.Energy_Generated_Total,
                                                                              Energy.Adjust_Scale,
                                                                              self.Quantity)
            if type_meter == 3:
                Energy_Variables['Energy_Generated_Line_C'] = self.Energy_Data(Energy.Energy_Generated_Line_C,
                                                                               Energy.Adjust_Scale,
                                                                               self.Quantity)

        Energy_Variables['localTimestamp'] = round(datetime.now().timestamp())

        return Energy_Variables
