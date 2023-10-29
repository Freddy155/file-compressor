# File Compression and Decompression App

The **File Compression and Decompression App** is a simple Python application that allows users to compress and decompress files using the zlib compression algorithm. This app provides an interactive command-line interface for compressing and decompressing files with various compression levels.

## Features

- **Compression:** Compress files with varying levels of compression (0 to 9).
- **Decompression:** Decompress previously compressed files.
- **Interactive Interface:** The app provides a user-friendly command-line interface for file compression and decompression.
- **Error Handling:** It includes error handling to ensure that file paths and compression levels are provided correctly.
- **Open Source:** This app is open-source and can be customized as needed.

## Usage

To use the File Compression and Decompression App, follow these steps:

1. Clone or download the app to your local machine.
2. Open a terminal or command prompt.
3. Navigate to the directory where the `app.py` script is located.
4. Run the app using the command `python3 app.py`.

The app will ask you whether you want to compress (C) or decompress (D) a file. Depending on your choice, it will prompt you for the relevant file paths and compression level.

## Getting Started

To get started with the File Compression and Decompression App, follow these instructions:

1. **Clone the Repository:** If you haven't already, clone the app repository to your local machine using Git:

   ```bash
   git clone https://github.com/Freddy155/file-compression.git
   ```

2. **Navigate to the Directory:** Open your terminal or command prompt and navigate to the directory where the app.py script is located.

   ```bash
   cd file-compressor
   ```

3. **Install Dependencies:** The app uses the built-in zlib library for compression and decompression, so there are no additional dependencies to install.

   ```bash
   pip install zlib
   ```

4. **Run the App:** Run the app using the following command:
   
   ```bash
   python app.py
   ```

5. **Follow the on-screen instructions to compress or decompress files.**

Examples
--------

### Compression

To compress a file, choose the `C` option and provide the following information:

-   Input file path: Enter the path to the file you want to compress.
-   Compressed file path: Enter the path where the compressed file will be saved.
-   Compression level: Choose a compression level from 0 (no compression) to 9 (maximum compression).

### Decompression

To decompress a file, choose the `D` option and provide the following information:

-   Compressed file path: Enter the path to the compressed file you want to decompress.
-   Decompressed file path: Enter the path where the decompressed file will be saved.