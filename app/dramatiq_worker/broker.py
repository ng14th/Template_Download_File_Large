from dramatiq.brokers.rabbitmq import RabbitmqBroker

broker_rqm = RabbitmqBroker(url="amqp://admin:admin@172.27.230.14:5672/nguyennt63")
broker_rqm.declare_queue("file_handler")