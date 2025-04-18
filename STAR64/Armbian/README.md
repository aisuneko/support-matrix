---
sys: armbian
sys_ver: 25.2.0-trunk.124
sys_var: null

status: cft
last_update: 2025-04-07

# Due to the complexcity in armbian mirror naming, we needs to provide the download link for sync tools in the metadata.
link: https://github.com/armbian/community/releases/download/25.2.0-trunk.124/Armbian_community_25.2.0-trunk.124_Star64_noble_edge_5.15.0_xfce_desktop.img.xz
---

# Armbian Star64 Test Report

## Test Environment

### Operating System Information

- Download Link: https://github.com/armbian/community/releases/download/25.2.0-trunk.124/Armbian_community_25.2.0-trunk.124_Star64_noble_edge_5.15.0_xfce_desktop.img.xz
- Reference Installation Document: https://www.hackster.io/lupyuen/rtos-on-a-risc-v-sbc-star64-jh7110-apache-nuttx-2a7429

### Hardware Information

- Development Board: Star64
- USB A to C / USB C to C Cable
- SD Card

## Installation Steps

### Flashing Image

After downloading, unzip and flash the image (using the xfce version as an example):
```bash
unxz -k Armbian_community_25.2.0-trunk.124_Star64_noble_edge_5.15.0_xfce_desktop.img.xz
sudo dd if=Armbian_community_25.2.0-trunk.124_Star64_noble_edge_5.15.0_xfce_desktop.img of=/dev/your/sdcard bs=1M status=progress
```

### Logging into the System

Connect to the development board via the serial port.

Upon startup, the system will prompt the user to manually configure the username, password, timezone, language, etc.

The Xfce version requires configuration completion before entering the desktop environment.

Configuration can be done via the serial port. If a keyboard and monitor are connected, it can also be done via the keyboard.

## Expected Results

The system boots up normally, and information can be viewed through the onboard serial port.

## Actual Results

CFT

### Boot Log

Screen recording (from flashing the system to booting up):
```log
```

## Test Criteria

Successful: The actual result matches the expected result.

Failed: The actual result does not match the expected result.

## Test Conclusion

CFT