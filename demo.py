import os

from pyflink.common.serialization import SimpleStringSchema
from pyflink.datastream import StreamExecutionEnvironment
from pyflink.datastream.connectors import FlinkKafkaConsumer

TOPIC = 'stream_latest_news'
KAFKA_PROPERTIES = {
    'bootstrap.servers': '172.18.168.132:9092,172.18.168.133:9092,172.18.168.134:9092',
    'group.id': 'yulong-test',
}

cur_path = os.path.dirname(os.path.realpath(__file__))


def tutorial():
    env = StreamExecutionEnvironment.get_execution_environment()
    jar_files = (
        'flink-connector-kafka_2.12-1.12.2.jar',
        'kafka-clients-2.4.1.jar',
    )
    jar_paths = tuple('file://' + os.path.abspath(os.path.join(cur_path, jar_file)) for jar_file in jar_files)

    env.add_jars(*jar_paths)
    env.add_classpaths(*jar_paths)
    env.set_parallelism(1)

    ds = env.add_source(FlinkKafkaConsumer(TOPIC, SimpleStringSchema(), KAFKA_PROPERTIES))

    ds.print()
    env.execute("tutorial_job")


if __name__ == '__main__':
    tutorial()
