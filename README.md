# AES-Image-Cryptography-VHDL
This project implements AES-based image cryptography on the Basys 3 FPGA board using VHDL, enabling secure message embedding within images. The encrypted message can only be extracted with the correct password, ensuring safe and reliable image-based communication.

# 🔐 AES-Based Image Cryptography using VHDL on Basys 3 FPGA

This project implements AES-based image cryptography on the **Basys 3 FPGA board** using **VHDL**, combined with a Python-based simulation for bit-level message embedding and visual analysis. The system allows secure message insertion into images, with decryption accessible only via the correct key.

---

## 📌 Overview

This project blends **hardware encryption (VHDL)** and **software steganography (Python)** to protect confidential messages embedded in digital images. The hardware side performs AES encryption and decryption on an FPGA, while the Python module simulates and visualizes how encrypted bits are hidden inside a 256-bit image using custom bit manipulation.

---

## 🎯 Objectives

- Design and deploy a 128-bit AES encryption core on the Basys 3 FPGA.
- Use Python to simulate steganographic embedding of AES-encrypted data.
- Provide bit-level visibility of message embedding and difference visualization.
- Ensure secure message recovery using XOR-based decryption with a key.

---

## 🧩 Key Features

- **AES Encryption** implemented in VHDL.
- **Steganography** using Python's bit manipulation utilities.
- 256-bit image simulation with selected embedding positions.
- XOR-based encryption/decryption validation.
- Visual difference highlighting of modified image bits.

---

## 🖥️ Tools & Hardware

- **FPGA Board**: Basys 3 (Xilinx Artix-7)
- **HDL**: VHDL (AES core modules)
- **Synthesis Tool**: Xilinx Vivado
- **Simulation**: Python 3.8+

---

## 🧪 Python Steganography Demo

The Python script performs the following steps:
1. **Generates a random 256-bit image (32 bytes)**.
2. **Encrypts an 8-bit message** using a random 8-bit key via XOR.
3. **Embeds the 8 encrypted bits** at predefined positions in the image.
4. **Extracts and decrypts the bits**, verifying message recovery.
5. **Prints binary representations** and **visual differences**.





🧾 Original 256-bit Image (256 bits):
1111110111110010001010100000101010110011111110100100011110111110110111010001110000101011010111110110001100110000001001100110000000011001010100001100100101011110111001010110001000111010111001011011010011011110001101010101001101010100101100001100111111111011

🧾 Encrypted 256-bit Image (256 bits):
1111110111010010001010100000101010110011111111100100011110111110110111010001110000101011010111110110001100110000001001100111000000011001010100001100101101011110111001010110001000111010111001011011010001011110001101010101001101010110101100001100111111111011

📷 Visual Difference (⬛=0 ⬜=1 🟥=Changed Bit):
⬜⬜⬜⬜⬜⬜⬛⬜⬜⬜🟥⬜⬛⬛⬜⬛
⬛⬛⬜⬛⬜⬛⬜⬛⬛⬛⬛⬛⬜⬛⬜⬛
⬜⬛⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜🟥⬜⬛
⬛⬜⬛⬛⬛⬜⬜⬜⬜⬛⬜⬜⬜⬜⬜⬛
⬜⬜⬛⬜⬜⬜⬛⬜⬛⬛⬛⬜⬜⬜⬛⬛
⬛⬛⬜⬛⬜⬛⬜⬜⬛⬜⬛⬜⬜⬜⬜⬜
⬛⬜⬜⬛⬛⬛⬜⬜⬛⬛⬜⬜⬛⬛⬛⬛
⬛⬛⬜⬛⬛⬜⬜⬛⬛⬜⬜🟥⬛⬛⬛⬛
⬛⬛⬛⬜⬜⬛⬛⬜⬛⬜⬛⬜⬛⬛⬛⬛
⬜⬜⬛⬛⬜⬛🟥⬜⬛⬜⬛⬜⬜⬜⬜⬛
⬜⬜⬜⬛⬛⬜⬛⬜⬛⬜⬜⬛⬛⬛⬜⬛
⬛⬛⬜⬜⬜⬛⬜⬛⬜⬜⬜⬛⬛⬜⬛⬜
⬜⬛⬜⬜⬛⬜⬛⬛🟥⬜⬛⬜⬜⬜⬜⬛
⬛⬛⬜⬜⬛⬜⬛⬜⬛⬜⬛⬜⬛⬛⬜⬜
⬛⬜⬛⬜⬛⬜🟥⬛⬜⬛⬜⬜⬛⬛⬛⬛
⬜⬜⬛⬛⬜⬜⬜⬜⬜⬜⬜⬜⬜⬛⬜⬜

📝 Message: 10000101 (Decimal: 133 )
🔑 Key    : 11001000 (Decimal: 200 )
📌 Bit Positions Used: [10, 45, 73, 99, 123, 150, 200, 230]

🔒 Encrypted Bits  : 01001101
🔓 Retrieved Binary: 10000101
🔓 Retrieved Decimal: 133



![image](https://github.com/user-attachments/assets/c300abc0-2c7f-487c-9e04-ab583078c1de)



![image](https://github.com/user-attachments/assets/ca965c48-d6cb-4b13-95a1-5d3931906907)

When passkey is wrong:

![WhatsApp Image 2025-04-07 at 15 29 54_e3cf332a](https://github.com/user-attachments/assets/a778c88f-c53d-48f7-8976-edd7be32f232)

When passkey is right:
Retrieved Binary: 10000101

![WhatsApp Image 2025-04-07 at 15 29 55_36c7b72e](https://github.com/user-attachments/assets/884bbbbe-8e5e-4691-a617-fd9324cc4241)

