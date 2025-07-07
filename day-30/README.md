
# 🚀 Deployment Setup: Clone Private GitHub Repo to EC2 Using SSH

This guide helps you securely set up SSH access on your EC2 instance to clone a private GitHub repository (e.g., `automhr-v3`) without using passwords or tokens.

---
- First 4 steps are most more important 

## 🔐 Step 1: Generate SSH Key (If Not Already Present)

On your **EC2 instance**, run:

```bash
ssh-keygen -t ed25519 -C "your_email@example.com"
```

- Press **Enter** to accept the default file path
- Leave passphrase **empty**

This will create:

- `~/.ssh/id_ed25519` → your **private key** (⚠️ keep it secret!)
- `~/.ssh/id_ed25519.pub` → your **public key**

---

## 📋 Step 2: Copy the Public Key

Show your public key:

```bash
cat ~/.ssh/id_ed25519.pub
```

It will look like:

```
ssh-ed25519 AAAAC3... Ankithv007@youremail.com
```

---

## 🌐 Step 3: Add the Key to GitHub

1. Go to: [https://github.com/settings/ssh/new](https://github.com/settings/ssh/new)
2. Set:
   - **Title**: EC2 VM Key
   - **Key**: Paste the output of `cat ~/.ssh/id_ed25519.pub`
3. Click **Add SSH Key**

---

## 🧪 Step 4: Test SSH Connection to GitHub

```bash
ssh -T git@github.com
```

Expected output:

```
Hi Ankithv007! You've successfully authenticated, but GitHub does not provide shell access.
```

---

## 📦 Step 5: Clone the Private Repo Using SSH

```bash
git clone git@github.com:VelankaniAIandCloudSolutions/automhr-v3.git
```

✅ This will **clone the repo without needing a username, password, or token.**

---

## 📁 Step 6: Move the Code to Apache Directory (Optional)

```bash
sudo mv automhr-v3 /var/www/html/automhr
sudo chown -R www-data:www-data /var/www/html/automhr
sudo chmod -R 755 /var/www/html/automhr
```

---

## ✅ Final Step: Restart Apache

```bash
sudo systemctl restart apache2
```

You're now ready to serve the application on your configured domain or IP.

---

## 🛠 Need Help?

Let us know if you want:
- `.env` configuration
- Apache VirtualHost setup
- MySQL database restore guide

---
