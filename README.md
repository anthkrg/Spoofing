# **ARP Spoofing, DNS Spoofing, and DHCP Spoofing**

**Author : Anthony KOUROGHLI (anthkrg)**

## French Part

Ce repo contient mes codes pour faire de **l'ARP spoofing**, du **DNS spoofing** et du **DHCP spoofing**.

---

### **IMPORTANT !!!**

Pour réaliser ces techniques, l'attaquant doit nécessairement se trouver sur le même réseau que la machine cible.

Dans le cas du **DNS spoofing** l'attaquant doit réaliser en amont de **l'ARP spoofing** ou du **DHCP spoofing**.

---

### DNS spoofing via ARP Spoofing

Dans le cadre du **DNS spoofing** via **ARP spoofing**, l'attaquant aura une position de **Man In The Middle (MITM)** et pourras rediriger toutes mes requêtes de la machine ciblé par **l'ARP spoofing** vers un domaine controlé par lui.

---

### DNS Spoofing via DHCP Spoofing

Dans le cadre du **DNS spoofing** via **DHCP spoofing**, l'attaquant déclarera une des machines qu'il controle comme serveur DNS sur le réseau. Il n'aura alors plus qu'à paramétrer un serveur DNS et renvoyé toute les requêtes des machines sur le réseau vers un domaine qu'il contrôle.

## English Part

This repository contains my code for performing **ARP spoofing**, **DNS spoofing**, and **DHCP spoofing**.  

---

### **IMPORTANT !!!**  

To execute these techniques, the attacker must be on the same network as the target machine.  

For **DNS spoofing**, the attacker must first perform **ARP spoofing** or **DHCP spoofing**.  

---

### **DNS Spoofing via ARP Spoofing**  

In the case of **DNS spoofing** via **ARP spoofing**, the attacker will take a **Man In The Middle (MITM)** position and will be able to redirect all DNS requests from the machine targeted by **ARP spoofing** to a domain controlled by them.  

---

### **DNS Spoofing via DHCP Spoofing**  

In the case of **DNS spoofing** via **DHCP spoofing**, the attacker will declare one of their controlled machines as the DNS server on the network.  
They will then simply need to configure a DNS server and redirect all DNS requests from machines on the network to a domain they control.  
