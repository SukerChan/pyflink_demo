from pyflink.common.serialization import SimpleStringSchema
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.connectors import FlinkKafkaConsumer

TOPIC = 'stream_latest_news'
KAFKA_PROPERTIES = {
    'bootstrap.servers': '172.18.168.132:9092,172.18.168.133:9092,172.18.168.134:9092',
    'group.id': 'yulong-test',
}


def tutorial():
    env = StreamExecutionEnvironment.get_execution_environment()
    env.set_parallelism(1)

    ds = env.add_source(FlinkKafkaConsumer(TOPIC, SimpleStringSchema(), KAFKA_PROPERTIES))

    ds.print()
    env.execute("tutorial_job")


if __name__ == '__main__':
    tutorial()
