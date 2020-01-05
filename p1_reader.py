import logging
import greengrasssdk
import json
import dsmr4_reader
from threading import Timer

print("hello")

def main():

    print('bla')
   
    client = greengrasssdk.client('iot-data', region_name='eu-west-1')

    p1_meter = dsmr4_reader.Meter('/dev/ttyUSB0', simulate=False)
    glob_p1_data = p1_meter.get_telegram()

    if glob_p1_data is not None:

        # ugly hack for now as aws IoT analytics does requires _
        p1_data = json.dumps(glob_p1_data).replace("-", "_")

        # power_data['p1'] = p1_data
        # print "**********************"
        # print power_data
        #
        # client.publish(topic + "/timestamp", str(int(time.time())))
        # logger.debug(p1_data)
        client.publish(topic='p1-test' + "/p1", payload=p1_data, qos=0)

        # for k, v in glob_p1_data.iteritems():

        #     logger.debug("Topic: {0}/p1 Key: {1} Value: {2}"
        #                     .format(topic, k.replace("-", "_"), v))
        #     # client.publish(topic + "/" + k, v)

    
    # Asynchronously schedule this function to be run again in 10 seconds
    Timer(10, main).start()




# This is a dummy handler and will not be invoked
# Instead the code above will be executed in an infinite loop for our example
def function_handler(event, context):
    return

if __name__ == '__main__':
    main()

main()
