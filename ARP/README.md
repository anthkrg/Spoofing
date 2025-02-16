# ARP SPOOFING

**Author : Anthony KOUROGHLI (anthkrg)**

## French Part

### Contexte

Ce dossier contient mon code pour faire de l'ARP spoofing.

L'ARP spoofing est une technique utilisé pour altérer la table ARP (correspondance MAC <--> IP) d'une machine cible

### **IMPORTANT !!!**

Ce code permet de faire de l'ARP spoofing **si et seulement si** l'attaquant se trouve sur le même réseau que la victime

L'idée est de faire croire à la victime sur notre réseau que nous sommes le routeur, et de faire croire au routeur que nous somme la victime.

Le but étant de situer entre la victime et le routeur pour faire ce que l'on appelle une attaque **Man In The Midlle** ou **MITM**

### Prérequis

Ce code utilise **scapy** pour forger des paquets et les envoyer a nos victimes. Nous utilisons aussi **argparse** pour ajouter des arguments à notre programme.

### Mise en place

Dans un premier temps nous récupérons l'adresse IP du routeur de manière **dynamique** et ce, peu importe la plateforme depuis laquelle le code est lancé (Windows, Linux, MacOS).

Dans un second temps à l'aide d'une requête APR nous récupérons l'adresse mac d'une IP précise sur le réseau.

Puis nous faisons du spoofing pour faire croire à une machine que nous sommes une autre machine.

Pour finir nous appelerons une fonction pour rétablir les tables ARP de chaque machine (pour éviter de tout casser).

## English Part

### Background

This folder contains my ARP spoofing code.

ARP spoofing is a technique used to alter the ARP table (MAC <--> IP correspondence) of a target machine.

### **IMPORTANT**

This code enables ARP spoofing **if and only if** the attacker is on the same network as the victim.

The idea is to make the victim on our network believe that we are the router, and to make the router believe that we are the victim.

The aim is to get between the victim and the router, in what is known as a **Man In The Middle** or **MITM** attack.

### Prerequisites

This code uses **scapy** to forge packets and send them to our victims. We also use **argparse** to add arguments to our program.

### Implementation

In the first stage, we use **dynamic** to retrieve the router's IP address, regardless of the platform from which the code is launched (Windows, Linux, MacOS).

Then, using an APR request, we retrieve the mac address of a specific IP on the network.

Then we spoof it to make a machine think we're another machine.

Finally, we'll call a function to restore the ARP tables of each machine (to avoid breaking everything).
