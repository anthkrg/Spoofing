# DNS SPOOFING

**Author : Anthony KOUROGHLI (anthkrg)**

## French Part

#### Contexte

Ce dossier contient mon code pour réaliser du **DNS spoofing**.  

Le **DNS spoofing** est une technique utilisée pour intercepter les requêtes DNS d'une machine cible et les rediriger vers un domaine choisi par l'attaquant.  

## **IMPORTANT !!!**  

Ce code permet d'effectuer du DNS spoofing à condition que la machine attaquante soit sur le même réseau que la machine cible.  
Pour que l'attaque réussisse, il est nécessaire de réaliser au préalable soit de l'**ARP spoofing**, soit du **DHCP spoofing** (voir les fichiers `README.md` correspondants).  

Dans le cas du **DNS spoofing** via l'**ARP spoofing**, la position de **Man In The Middle** (**MITM**) obtenue grâce à l'ARP spoofing nous permet d'intercepter toutes les requêtes de notre victime.  

Ainsi, dès qu'elle enverra une requête DNS, notre machine pourra la rediriger vers un domaine contrôlé par l'attaquant.  

---

## **Prérequis**  

Ce code utilise **Scapy** pour forger et envoyer des paquets à notre machine cible.  
Nous utilisons également **argparse** pour ajouter des arguments à notre programme.  

---

## **Mise en place**  

1. **Définition de la fonction de redirection**  
   Cette fonction capture une requête DNS et renvoie une réponse DNS pointant vers l'IP d'une machine contrôlée par l'attaquant.  

2. **Ajout des arguments au programme**  
   Nous définissons une fonction permettant d'utiliser des arguments dans notre programme.  
   Dans notre cas, l'argument retenu est l'IP de la machine vers laquelle seront redirigées toutes les requêtes DNS.  

3. **Définition de la fonction `main`**  
   - Analyse des arguments fournis au programme.  
   - Écoute des requêtes UDP à destination du port `53` (requêtes DNS).  

---

## English Part

## **DNS Spoofing**  

This folder contains my code for performing **DNS spoofing**.  

**DNS spoofing** is a technique used to intercept a target machine’s DNS requests and redirect them to a domain chosen by the attacker.  

## **IMPORTANT !!!**  

This code allows DNS spoofing only if the attacking machine is on the same network as the target machine.  
For the attack to be successful, you must first perform either **ARP spoofing** or **DHCP spoofing** (see the corresponding `README.md` files).  

In the case of **DNS spoofing** via **ARP spoofing**, the **Man In The Middle** (**MITM**) position obtained through ARP spoofing allows us to intercept all the victim's requests.  

Thus, whenever the victim sends a DNS request, our machine can redirect it to a domain controlled by the attacker.  

---

## **Prerequisites**  

This code uses **Scapy** to forge and send packets to the target machine.  
We also use **argparse** to add arguments to our program.  

---

## **Setup**  

1. **Defining the redirection function**  
   This function captures a DNS request and sends a DNS response pointing to an IP address controlled by the attacker.  

2. **Adding arguments to the program**  
   We define a function to handle arguments in our program.  
   In this case, the key argument is the IP address to which all DNS requests will be redirected.  

3. **Defining the `main` function**  
   - Parses the arguments provided to the program.  
   - Listens for UDP requests directed to port `53` (DNS requests).  

