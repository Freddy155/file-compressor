import zlib

def compress_file(input_file, output_file, compression_level):
    with open(input_file, 'rb') as f_in:
        with open(output_file, 'wb') as f_out:
            compressor = zlib.compressobj(compression_level)
            for chunk in iter(lambda: f_in.read(4096), b''):
                compressed_chunk = compressor.compress(chunk)
                f_out.write(compressed_chunk)
            f_out.write(compressor.flush())

def decompress_file(input_file, output_file):
    with open(input_file, 'rb') as f_in:
        with open(output_file, 'wb') as f_out:
            decompressor = zlib.decompressobj()
            for chunk in iter(lambda: f_in.read(4096), b''):
                decompressed_chunk = decompressor.decompress(chunk)
                f_out.write(decompressed_chunk)
            f_out.write(decompressor.flush())

if __name__ == '__main__':
    action = input("Do you want to compress (C) or decompress (D) a file? ").strip().lower()
    
    if action == 'c':
        input_file = input("Enter the input file path: ").strip('\'"') 
        compressed_file = input("Enter the compressed file path: ").strip('\'"')  
        compression_level = int(input("Enter the compression level (0 to 9): "))
        
        compress_file(input_file, compressed_file, compression_level)
        print(f'File "{input_file}" compressed to "{compressed_file}".')
        
    elif action == 'd':
        compressed_file = input("Enter the compressed file path: ").strip('\'"')  
        decompressed_file = input("Enter the decompressed file path: ").strip('\'"') 
        
        decompress_file(compressed_file, decompressed_file)
        print(f'File "{compressed_file}" decompressed to "{decompressed_file}".')
        
    else:
        print("Invalid choice. Please enter 'C' for compression or 'D' for decompression.")
