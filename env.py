import logging
import boto3
import os

logger = logging.getLogger()
logger.setLevel(logging.INFO)

obj_order_table = os.environ.get('DYNAMODB_ORDER_TABLE') or 's3_obj_order'
