from pox.core import core
import pox.openflow.libopenflow_01 as of

log = core.getLogger()

def _handle_ConnectionUp(event):
    log.info("Switch connected!")

def _handle_PacketIn(event):
    packet = event.parsed
    in_port = event.port

    log.info("Packet received from port %s" % in_port)

    # BLOCK h3 (port 3)
    if in_port == 3:
        log.info("BLOCKED h3 traffic")
        return

    # INSTALL FLOW RULE (for h1, h2)
    match = of.ofp_match.from_packet(packet)
    
    actions = [of.ofp_action_output(port=of.OFPP_FLOOD)]

    flow_mod = of.ofp_flow_mod()
    flow_mod.match = match
    flow_mod.actions = actions

    event.connection.send(flow_mod)


def launch():
    core.openflow.addListenerByName("ConnectionUp", _handle_ConnectionUp)
    core.openflow.addListenerByName("PacketIn", _handle_PacketIn)
    log.info("Firewall Controller Started")