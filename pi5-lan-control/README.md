# Pi5 LAN Control for Huawei Termux

Local Wi-Fi only Raspberry Pi 5 controller for Universal Dragon / Novakutty work.

No Tailscale. No public tunnel. No port forwarding. No API keys printed. Humanity briefly survives another network decision.

## What this gives you

- Control Pi5 from Huawei Termux using SSH on the same Wi-Fi.
- Check Pi health, disk, RAM, SSH, PM2, and Novakutty bot.
- Restart/start/stop the WhatsApp bot safely.
- Read logs without opening `.env` or printing secrets.
- Optional LAN scan for SSH devices.

## Install on Huawei Termux

```bash
pkg update -y
pkg install -y git openssh netcat-openbsd nmap
mkdir -p ~/tools
curl -fsSL https://raw.githubusercontent.com/UniverseDragon14/terminal/feat/pi5-lan-control/pi5-lan-control/pi5ctl -o ~/tools/pi5ctl
chmod +x ~/tools/pi5ctl
mkdir -p ~/.local/bin
ln -sf ~/tools/pi5ctl ~/.local/bin/pi5ctl
export PATH="$HOME/.local/bin:$PATH"
```

Add PATH permanently:

```bash
grep -q 'HOME/.local/bin' ~/.bashrc 2>/dev/null || echo 'export PATH="$HOME/.local/bin:$PATH"' >> ~/.bashrc
```

## First setup

Use your current Pi IP, usually:

```bash
pi5ctl setup aslam 192.168.1.80
pi5ctl trust
pi5ctl status
```

If Pi IP changes:

```bash
pi5ctl scan 192.168.1.0/24
pi5ctl setup aslam NEW_PI_IP
```

## Daily commands

```bash
pi5ctl ssh
pi5ctl status
pi5ctl watchdog
pi5ctl bot
pi5ctl logs 80
pi5ctl restart-bot
pi5ctl check-env
```

## Safety rules

- Do not expose Pi SSH to the internet.
- Do not paste passwords, OTP, API keys, or HubSpot/Groq/Gemini tokens into logs or screenshots.
- Use this only for your own Pi / authorized devices.
- Keep it LAN-only unless you deliberately set up a secure VPN later.

## Expected healthy result

`pi5ctl watchdog` should show something like:

```text
STATUS=online MEM=120MB PID=2999
✅ Novakutty healthy bro
```

## Troubleshooting

### Port open but SSH hangs

```bash
nc -vz -w 5 192.168.1.80 22
ssh -4 -o PreferredAuthentications=password -o PubkeyAuthentication=no -o IPQoS=none aslam@192.168.1.80
```

### Host key changed

Only do this when you are sure the IP is your Pi:

```bash
ssh-keygen -R 192.168.1.80
pi5ctl trust
```

### Bot alive but SSH broken

Power cycle Pi5, wait 3 minutes, then:

```bash
pi5ctl status
```
