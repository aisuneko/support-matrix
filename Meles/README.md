---
product: Milk-V Meles
vendor: milkv_meles
cpu: TH1520
cpu_core: XuanTie C910 + XuanTie C906 + XuanTie E902
---

# Milk-V Meles

## Test Environment

### Operating System Information

- RevyOS
    - Download link: https://mirror.iscas.ac.cn/revyos/extra/images/meles/20241229/
    - Reference Installation Document: https://milkv.io/zh/docs/meles/getting-started/boot
- Deepin TH1520 20250122
    - Download Link: https://ci.deepin.com/repo/deepin/deepin-ports/cdimage/20250122/riscv64/deepin-25-beige-preview-riscv64-th1520-20250122-113934.tar.xz
        - iw-single-line binary: https://mirror.iscas.ac.cn/revyos/extra/images/meles/20240720/iw-single-line.bin
        - U-Boot with SPL firmware: https://cdimage.deepin.com/RISC-V/preview-20240815-riscv64/uboot-th1520-revyos.zip
    - Reference Installation Document: https://milkv.io/zh/docs/meles/getting-started/boot
### Hardware Information

- Milk-V Meles 4GB/8GB/16GB
    - The board tested here in the documents is the 16GB variant

## Test Results

| Software Category | Package Name | Test Results (Test Report) |
| ----------------- | ------------ | -------------------------- |
| RevyOS Image Boot | N/A          | [Good][RevyOS]             |
| Deepin Image Boot | N/A          | [Good][Deepin]             |

[RevyOS]: ./RevyOS/README.md
[Deepin]: ./Deepin/README.md
