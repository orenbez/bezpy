#  Office IP "167.206.221.74" has been whitelisted for ssh in firewall
# https://medium.com/better-programming/how-to-set-up-multiple-ssh-keys-ae6688f76570

# Requires `pip install sshtunnel`, `pip install pymysql`
from sshtunnel import SSHTunnelForwarder # , SSH_TIMEOUT, TUNNEL_TIMEOUT
import pymysql  # don't use pypyodbc


SSH_TIMEOUT = 3.0
TUNNEL_TIMEOUT = 3.0



ssh_tunnel_host = '34.238.228.76' # Production
ssh_tunnel_host = '3.233.251.201'   # Staging
#ssh_tunnel_host = '3.82.243.146'   # Development

ssh_port = 22
ssh_username = 'ubuntu'

# Note: C:\OrenDocs\New_Web\TSC_GENERAL_PPK.ppk is used for PuTTY SSH connection, not for MySql
ssh_pkey = 'C:\\OrenDocs\\New_Web\\id_rsa_oren.KEY'


db_host = '127.0.0.1'
db_port = 3306
db_name = 'tscapp'
db_user = 'tscapp'
db_password = 'bPouhcQKHmGdyCGdJHI4YdnwtSWTFLeV'



# for some reason wrapping this 'with' statement in a try: except: doesn't work

with SSHTunnelForwarder((ssh_tunnel_host, ssh_port), ssh_username=ssh_username,
                         ssh_pkey=ssh_pkey, ssh_password=None,
                         remote_bind_address=(db_host, db_port)) as tunnel:
    conn = pymysql.connect(host=db_host, port=tunnel.local_bind_port, db=db_name, user=db_user, password=db_password)
    cr = conn.cursor()
    cr.execute("""SELECT * FROM tscapp.crm_carregistry LIMIT 0,5""")
    x = cr.fetchall()
    cr.close()
    conn.close()


#===========================================================================
# WARNING.   cr.commit() is NOT recognized,  use conn.commit() instead.
#===========================================================================    


