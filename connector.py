import logging
import paramiko

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__) 
def execute_command_readlines(address, usr, pwd, command, port_number):
        try:
            logger.debug("ssh " + usr + "@" + address + ", running : " +
                         command)
            client = paramiko.SSHClient()
            client.load_system_host_keys()
            client.set_missing_host_key_policy(paramiko.AutoAddPolicy())

            client.connect(address, username=usr, password=pwd, port=port_number)
            _, ss_stdout, ss_stderr = client.exec_command(command)
            r_out, r_err = ss_stdout.read(), ss_stderr.read()
            print(r_out)
	    logger.debug(r_err)
            if len(r_err) > 5:
                logger.error(r_err)
            else:
                logger.debug(r_out)
            client.close()
        except IOError:
            logger.warning(".. host " + address + " is not up")
            return "host not up", "host not up"

        return r_out, r_err 
