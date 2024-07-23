# replaces pyhive library
# requires `pip install trino`
# see https://docs.google.com/document/d/1hnsZXYvHyqgSZUOgV3tfSYm_UywO9veAdip1_vYNm10/edit

import trino
from trino.exceptions import TrinoError

#====================================================
# example of configuration of property files setting
#====================================================
# user-credential-name=user
# password-credential-name=pass
#====================================================

conn = trino.dbapi.connect(
    host='localhost',
    port=8080,
    user='the-user',                                               
    # http_scheme='https',                                      # <---- go together instead of user=...
    # auth=trino.auth.BasicAuthentication('zkpnqzq', 'psswd')   # <---- go together instead of user=...
    extra_credentials = [('user', 'xxx'), ('pass', 'yyy')],     # <---- 'user', 'pass' must match property fle settings
    catalog='the-catalog',
    schema='the-schema',
    verify=False # skip SSL verification
)
cur = conn.cursor()
cur.execute('SELECT * FROM system.runtime.nodes')
cur.fetchone()
cur.stats
# {
# 'queryId': '20220130_143549_08022_t43i7', 'state': 'QUEUED', 'queued': True, 'scheduled': False, 
# 'nodes': 0, 'totalSplits': 0, 'queuedSplits': 0, 'runningSplits': 0, 'completedSplits': 0, 
# 'cpuTimeMillis': 0, 'wallTimeMillis': 0, 'queuedTimeMillis': 0, 'elapsedTimeMillis': 0, 
# 'processedRows': 0, 'processedBytes': 0, 'physicalInputBytes': 0, 'peakMemoryBytes': 0, 'spilledBytes': 0}

cur.execute('SHOW TABLES')
rows = cur.fetchall()