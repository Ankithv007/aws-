## OpenVPN Setup to Access Private EC2

### 🚀 Objective

Set up OpenVPN on a bastion host so you can securely connect to private EC2 instances via their private IP — without needing SSH key pairs on the terminal.

---

## 🌟 Architecture

```
Laptop (VPN Client: 10.8.0.x)
      │
 (VPN Tunnel)
      │
Bastion Host (OpenVPN server: public IP e.g., 3.6.91.85)
      │
 (VPC internal network)
      │
Private EC2 (private IP e.g., 10.0.x.x)
```

---

## ⚙ Prerequisites

✅ A bastion EC2 (with public IP, e.g., 3.6.91.85)
✅ A private EC2 (no public IP)
✅ Key pair file (e.g., `deepu.pem`)
✅ Open security groups:

* Bastion SG: Allow `UDP 1194` from your laptop’s public IP
* Private EC2 SG: Allow `SSH (22)` from `10.8.0.0/24`

---

## 📝 Step-by-step setup

### 1️⃣ SSH into bastion

```
ssh -i deepu.pem ubuntu@3.6.91.85
```

### 2️⃣ Download & run OpenVPN installer

```
wget https://git.io/vpn -O openvpn-install.sh
chmod +x openvpn-install.sh
sudo ./openvpn-install.sh
```

* When prompted:

  * Public IP: **accept default or enter 3.6.91.85**
  * Protocol: **UDP**
  * Port: **1194**
  * DNS: **Google (2)**
  * Client name: **ankith**
  * Confirm: Press **ENTER** to start install

### 3️⃣ Download the client config to your laptop

From your **laptop terminal**:

```
scp -i deepu.pem ubuntu@3.6.91.85:/home/ubuntu/ankith.ovpn .
```

➡ The file will download to your local folder.

### 4️⃣ Import and connect

✅ Open your OpenVPN client (e.g., OpenVPN Connect)
✅ Import `ankith.ovpn`
✅ Click **Connect**

### 5️⃣ Access private EC2

Once VPN is connected:

```
ssh -i deepu.pem ubuntu@<private-ec2-private-ip>
```

➡ Or enable password SSH on private EC2 if desired.

---

## 🔑 (Optional) Enable SSH password login on private EC2

SSH into private EC2:

```
ssh -i deepu.pem ubuntu@<private-ec2-private-ip>
```

Edit SSH config:

```
sudo nano /etc/ssh/sshd_config
```

Set:

```
PasswordAuthentication yes
```

Restart SSH:

```
sudo systemctl restart ssh
```

Set a password:

```
sudo passwd ubuntu
```

---

## ⚠ Security Group Config

✅ Bastion SG

* UDP 1194 from your laptop IP
* SSH 22 from your laptop IP

✅ Private EC2 SG

* SSH 22 from `10.8.0.0/24`

---

## 📝 Add new VPN clients

On bastion:

```
sudo ./openvpn-install.sh
```

➡ Choose **Add a new client**
➡ Follow prompts

---

## 💡 Summary

✅ VPN allows direct connection from your laptop to private EC2 over the VPC.
✅ No need for terminal-based bastion jump SSH.
