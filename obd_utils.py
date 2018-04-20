import obd
from obd import ECU

ports = obd.scan_serial()

print(ports)
obd.logger.setLevel(obd.logging.DEBUG)
connection = obd.OBD(portstr=ports[2],fast=False)

cmd = obd.commands.RPM
resp = connection.query(cmd)
print(resp.value)

cmd = obd.commands.PIDS_A.ecu = ECU.ALL
resp = connection.query(cmd)
print(resp.value)

cmd = obd.commands.PIDS_B.ecu = ECU.ALL
resp = connection.query(cmd)
print(resp.value)
