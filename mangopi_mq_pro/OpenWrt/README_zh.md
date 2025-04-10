# OpenWrt MangoPi MQ Pro 测试报告

## 测试环境

### 操作系统信息

- 下载链接（OpenWrt Firmware Selector）：https://firmware-selector.openwrt.org/?version=SNAPSHOT&target=d1%2Fgeneric&id=widora_mangopi-mq-pro
- 参考安装文档：https://openwrt.org/docs/techref/hardware/soc/soc.allwinner.d1

> 在 OpenWrt Firmware Selector 中可以在线定制构建系统镜像，添加用户所需要的预装软件包。本次测试使用的为**未经修改**的原版镜像。

### 硬件信息

- MangoPi MQ Pro
- microSD 卡一张
- USB to UART 调试器一个（如：CH340, CH341, FT2232 等）

## 安装步骤

### 刷写镜像到 microSD 卡

使用 `dd` 刷入镜像到 microSD 卡。

```bash
gzip -kd openwrt-d1-generic-widora_mangopi-mq-pro-ext4-sdcard.img.gz
sudo dd if=openwrt-d1-generic-widora_mangopi-mq-pro-ext4-sdcard.img of=/dev/your/device bs=1M status=progress
```

### 登录系统

通过串口登录系统。

## 预期结果

系统正常启动，能够通过板载串口登录。

## 实际结果

系统正常启动，能够通过板载串口登录。

### 启动信息

```log
[    2.013600] Run /sbin/init as init process
[    2.280428] init: Console is alive
[    2.284620] init: - watchdog -
[    2.580288] kmodloader: loading kernel modules from /etc/modules-boot.d/*
[    2.596862] kmodloader: done loading kernel modules from /etc/modules-boot.d/*
[    2.606884] init: - preinit -
[    8.019779] random: crng init done
Press the [f] key and hit [enter] to enter failsafe mode
Press the [1], [2], [3] or [4] key and hit [enter] to select the debug level
[   12.021022] platform 2009400.temperature-sensor: deferred probe pending
[   12.594623] mount_root: mounting /dev/root with options 
[   12.665047] EXT4-fs (mmcblk0p2): re-mounted ff313567-e9f1-5a5d-9895-3ba130b4a864 r/w. Quota mode: disabled.
[   12.679037] urandom-seed: Seed file not found (/etc/urandom.seed)
[   12.737301] procd: - early -
[   12.740832] procd: - watchdog -
[   14.275367] procd: - watchdog -
[   14.280355] procd: - ubus -
[   14.348389] procd: - init -
Please press Enter to activate this console.
[   15.985076] kmodloader: loading kernel modules from /etc/modules.d/*
[   17.212892] compat: loading out-of-tree module taints kernel.
[   17.219557] Loading modules backported from Linux version v6.12.6-0-ge9d65b48ce1a
[   17.227178] Backport generated by backports.git v6.1.110-1-35-g410656ef04d2
[   17.862418] urngd: v1.0.2 started.
[   21.889288] PPP generic driver version 2.4.2
[   21.899199] NET: Registered PF_PPPOX protocol family
[   22.028461] rtw_8723ds mmc1:0001:1: Firmware version 48.0.0, H2C version 0
[   22.750777] kmodloader: done loading kernel modules from /etc/modules.d/*



BusyBox v1.37.0 (2025-03-02 10:42:48 UTC) built-in shell (ash)

  _______                     ________        __
 |     | .-----.-----.-----. |  |  |  | .----. |  | _ |
 | --- ||  _  |  -__|     ||  |  |  ||   _||   _|
 |_______||   __|_____|__|__||________||__|  |____|
          |__| W I R E L E S S   F R E E D O M
 -----------------------------------------------------
 OpenWrt SNAPSHOT, r28926-9a7192c08e
 -----------------------------------------------------
=== WARNING! =====================================
There is no root password defined on this device!
Use the "passwd" command to set up a new password
in order to prevent unauthorized SSH logins.
--------------------------------------------------

 OpenWrt recently switched to the "apk" package manager!

 OPKG Command           APK Equivalent      Description
 ------------------------------------------------------------------
 opkg install <pkg>     apk add <pkg>       Install a package
 opkg remove <pkg>      apk del <pkg>       Remove a package
 opkg upgrade           apk upgrade         Upgrade all packages
 opkg files <pkg>       apk info -L <pkg>   List package contents
 opkg list-installed    apk info            List installed packages
 opkg update            apk update          Update package lists
 opkg search <pkg>      apk search <pkg>    Search for packages
 ------------------------------------------------------------------

For more https://openwrt.org/docs/guide-user/additional-software/opkg-to-apk-cheatsheet

root@OpenWrt:~# uname -a
Linux OpenWrt 6.6.80 #0 SMP Sun Mar  2 10:42:48 2025 riscv64 GNU/Linux
root@OpenWrt:~# cat /etc/os-release 
NAME="OpenWrt"
VERSION="SNAPSHOT"
ID="openwrt"
ID_LIKE="lede openwrt"
PRETTY_NAME="OpenWrt SNAPSHOT"
VERSION_ID="snapshot"
HOME_URL="https://openwrt.org/"
BUG_URL="https://bugs.openwrt.org/"
SUPPORT_URL="https://forum.openwrt.org/"
FIRMWARE_URL="https://downloads.openwrt.org/"
BUILD_ID="r28926-9a7192c08e"
OPENWRT_BOARD="d1/generic"
OPENWRT_ARCH="riscv64_riscv64"
OPENWRT_TAINTS=""
OPENWRT_DEVICE_MANUFACTURER="OpenWrt"
OPENWRT_DEVICE_MANUFACTURER_URL="https://openwrt.org/"
OPENWRT_DEVICE_PRODUCT="Generic"
OPENWRT_DEVICE_REVISION="v0"
OPENWRT_RELEASE="OpenWrt SNAPSHOT r28926-9a7192c08e"
OPENWRT_BUILD_DATE="1740912168"
root@OpenWrt:~# lscpu
-ash: lscpu: not found
root@OpenWrt:~# 

```

## 测试判定标准

测试成功：实际结果与预期结果相符。

测试失败：实际结果与预期结果不符。

## 测试结论

测试成功。