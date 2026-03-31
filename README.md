# SDN Firewall using POX and Mininet

## Objective

To implement an SDN-based firewall that blocks traffic from a specific host (h3) while allowing communication between other hosts.

---
## What is SDN?
Software Defined Networking (SDN) separates the control plane from the data plane, allowing centralized control of network behavior using a controller.

--- 

## Tools Used

* Mininet
* POX Controller
* OpenFlow Protocol
* iperf (for performance testing)


## Topology

Single switch topology with 3 hosts:

* h1
* h2
* h3
I used Mininet to create a topology with 3 hosts and 1 switch. The switch is controlled by a POX controller using the OpenFlow protocol.

## Implementation

The controller handles PacketIn events and applies the following logic:

* Traffic from port 3 (h3) is blocked
* Traffic from other ports is allowed
* Flow rules are installed dynamically using OpenFlow



## Execution Steps

### Start Controller

cd ~/pox
./pox.py log.level --DEBUG misc.firewall

### Start Mininet

sudo mn --topo single,3 --controller=remote,ip=127.0.0.1,port=6633 --switch ovsk,protocols=OpenFlow10

---

## Test Cases

### Allowed Traffic

h1 ping h2 → Successful communication

### Blocked Traffic

h3 ping h2 → No replies (blocked by controller)

---

## 📊 Flow Table

sudo ovs-ofctl -O OpenFlow10 dump-flows s1

---

## 📈 Performance Test

iperf h1 h2

---

## 📸 Output

Screenshots provided in the screenshots folder.

---

## Conclusion

The SDN firewall successfully demonstrates centralized traffic control using a controller. The system dynamically blocks unauthorized traffic and allows valid communication using OpenFlow rules.
