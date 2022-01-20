#! /usr/bin/env python

import time
import serial
from nm3driver import Nm3
from nm3driver import MessagePacket
from datetime import datetime
import csv
import sys

def main():
    """Main Program Entry."""

    ## Create the Modem
    # Serial Port is opened with a 100ms timeout for reading.
    serial_port = serial.Serial('/dev/modem', 9600, 8, serial.PARITY_NONE, serial.STOPBITS_ONE, 0.1)
    nm3_modem = Nm3(input_stream=serial_port, output_stream=serial_port)

    ## Parameters used
    local_address = 228 # If bouy IP is 192.168.0.8 then local_address = 228
    remote_addreses = [123, 124, 125, 126]
    message = b'Hello'

    ## Run Through Functions

    # $A - Set Address
    set_address(nm3_modem=nm3_modem, new_address=local_address)

    # $C - Channel Impulse Response
    channel_impulse_response(nm3_modem=nm3_modem, remote_addreses=remote_addreses, plot_results=False)

    return

def query_status(nm3_modem):
    """Example: $? - Query Status."""
    print('Example: Query Status')
    addr_int, voltage, version_string, build_date_string = nm3_modem.query_status()

    print(' Modem Address={:03d}'.format(addr_int))
    print(' Battery Voltage={:.2f}V'.format(voltage))
    print(' Version=' + version_string)
    print(' Build Date=' + build_date_string)


def set_address(nm3_modem, new_address):
    """Example: $A - Set Address."""
    print('Set Address')

    print('  Query Current Status')
    ret = nm3_modem.query_status()
    if ret == -1:
        print(' Error')
    else:
        addr_int, voltage, version_string, build_date_string = ret
        print(' Initial Modem Address={:03d}'.format(addr_int))

    addr_new_int = nm3_modem.set_address(new_address)
    print(' Set Modem Address={:03d}'.format(addr_new_int))

    print('  Query Current Status')
    ret = nm3_modem.query_status()
    if ret == -1:
        print(' Error')
    else:
        addr_int, voltage, version_string, build_date_string = ret
        print(' Current Modem Address={:03d}'.format(addr_int))


def channel_impulse_response(nm3_modem, remote_addreses, plot_results=False):
    """Example: $C - Channel Impulse Response."""
    print('Channel Impulse Response')

    for adress in remote_addreses:
        print('Magnitudes: Remote Address={:03d}'.format(adress))
        ret = nm3_modem.send_ping_for_channel_impulse_response(adress, 'M')
        now = datetime.now()
        dt_string = now.strftime("%d-%m-%Y-%H-%M-%S")
        if ret == -1:
            print(' Error')
            with open('ensemble_log.txt', 'a') as f:
                print(dt_string +' Magnitude query - No response from modem id={:03d}'.format(adress), file=f)
        else:
            timeofarrival, data_count, data_values = ret
            print(' Time of Arrival={:.6f} seconds'.format(timeofarrival))
            print(' Data Count={:04d}'.format(data_count))
            time_values = [(float(b-100) / 16e3) for b in range(data_count)]
            # print(' Time Values: {}'.format(time_values))
            # print(' Data Values: {}'.format(data_values))
            x = time_values
            y = list(data_values)
            new_list = zip(x, y)
            file_name = 'id-{:03d}-mag-'.format(adress) + dt_string
            print(' Channel Impulse Response (Magnitude) saved to file ={}.csv'.format(file_name))
            with open('ensemble_log.txt', 'a') as f:
                print(dt_string +' Magnitudes: Remote Address={:03d}'.format(adress), file=f)
                print(dt_string +' Time of Arrival={} seconds'.format(timeofarrival), file=f)
                print(dt_string +' Data Count={}'.format(data_count), file=f)
                print(dt_string +' Channel Impulse Response (Magnitude) saved to file ={}.csv'.format(file_name), file=f)
            with open(file_name+'.csv', 'w+') as csvfile:
                filewriter = csv.writer(csvfile)
                filewriter.writerows(new_list)

        # print('Complex: Remote Address={:03d}'.format(adress))
        # ret = nm3_modem.send_ping_for_channel_impulse_response(adress, 'C')
        # now = datetime.now()
        # dt_string = now.strftime("%d-%m-%Y-%H-%M-%S")
        # if ret == -1:
        #     print(' Error')
        #     with open('ensemble_log.txt', 'a') as f:
        #         print(dt_string +' Complex query - No response from modem id={:03d}'.format(adress), file=f)
        # else:
        #     timeofarrival, data_count, data_values = ret
        #     print(' Time of Arrival={:.6f} seconds'.format(timeofarrival))
        #     print(' Data Count={:04d}'.format(data_count))
        #     real_data_values = data_values[0::2]
        #     # print(' Real Data Values {}'.format(real_data_values))
        #     imaginary_data_values = data_values[1::2]

        #     x = time_values
        #     y_real = list(real_data_values)
        #     y_imaginary = list(imaginary_data_values)
        #     new_list = zip(x, y_real, y_imaginary)
        #     file_name = 'id-{:03d}-complex-'.format(adress) + dt_string
        #     print(' Channel Impulse Response (Complex) saved to file ={}.csv'.format(file_name))
        #     with open('ensemble_log.txt', 'a') as f:
        #         print(dt_string +' Complex: Remote Address={:03d}'.format(adress), file=f)
        #         print(dt_string +' Time of Arrival={} seconds'.format(timeofarrival), file=f)
        #         print(dt_string +' Data Count={}'.format(data_count), file=f)
        #         print(dt_string +' Channel Impulse Response (Complex) saved to file ={}.csv'.format(file_name), file=f)
        #     with open(file_name+'.csv', 'w+') as csvfile:
        #         filewriter = csv.writer(csvfile)
        #         filewriter.writerows(new_list)

def unicast_data_with_ack(nm3_modem, remote_address, message):
    """Example: $M - Unicast Data with Ack."""
    print('Example: Unicast Data with Ack')

    ret = nm3_modem.send_unicast_message_with_ack(remote_address, message)
    if ret == -1:
        print(' Error')
    else:
        print(' Time of Arrival={:.6f} seconds'.format(ret))


def ping(nm3_modem, remote_address):
    """Example: $P - Ping"""
    print('Example: Ping')

    ret = nm3_modem.send_ping(remote_address)
    if ret == -1:
        print(' Error')
    else:
        print(' Time of Arrival={:.6f} seconds'.format(ret))


if __name__ == '__main__':
    main()
