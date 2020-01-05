import logging
import greengrasssdk
import json
import dsmr4_reader
import sunspec_modbus_tcp_reader
from threading import Timer

logger = logging.getLogger(__name__)

topic = os.environ['TOPIC']
pv_address = os.environ['PV_ADDRESS']
p1_port = os.environ['P1_PORT']
poll_interval = os.environ['POLL_INTERVAL']

def main():
     
    client = greengrasssdk.client('iot-data')

    p1_meter = dsmr4_reader.Meter(pv_port, simulate=False)
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
        
        client.publish(topic=topic + "/p1", payload=p1_data, qos=0)

        # for k, v in glob_p1_data.iteritems():
        #     logger.debug("Topic: {0}/p1 Key: {1} Value: {2}"
        #                     .format(topic, k.replace("-", "_"), v))
        #     # client.publish(topic + "/" + k, v)

    sunspec_client = sunspec_modbus_tcp_reader.SunSpecModBusTcpClient(pv_address, 502, 2)
    glob_pv_data = sunspec_client.get_sunspec_data()

    if glob_pv_data is not None:

        pv_data = json.dumps(glob_pv_data)
        logger.debug(pv_data)

        client.publish(topic + "/pv", pv_data, qos=0)

        # client.publish(topic + "/timestamp", str(int(time.time())))
        # for k, v in glob_pv_data.iteritems():

            # logger.debug("Topic: {0}/pv Key: {1} Value: {2}"
                            # .format(topic, k, v))
            # client.publish(topic + "/" + k, v)
    else:
        logger.warning('No PV Data! Sun down? or Logger Down')

    # Asynchronously schedule this function to be run again in 10 seconds
    Timer(poll_interval, main).start()

# This is a dummy handler and will not be invoked
# Instead the code above will be executed in an infinite loop for our example
def handler(event, context):
    return

if __name__ == '__main__':
    main()

main()
