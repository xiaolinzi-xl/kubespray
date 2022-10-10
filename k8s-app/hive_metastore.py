from hive_metastore_client.builders import DatabaseBuilder
from hive_metastore_client import HiveMetastoreClient

# database = DatabaseBuilder(name='new_db').build()
with HiveMetastoreClient('127.0.0.1', 9083) as hive_metastore_client:
    # hive_metastore_client.create_database(database) 
    # hive_metastore_client.sh
    hive_metastore_client.add_master_key('xiaolinzi')
    print('连接测试成功')

# pip install hive-metastore-client