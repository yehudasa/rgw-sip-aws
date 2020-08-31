import logging
import boto3
import os
import sys

logger = logging.getLogger()
# logger.setLevel(logging.INFO)
logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)


dynamodb_url='http://localhost:8100'

obj_order_table = os.environ.get('DYNAMODB_ORDER_TABLE') or 's3_obj_order'

datalog_num_shards = os.environ.get('DATALOG_NUM_SHARDS') or 16
