import argparse
import wave

def encode(input_file, output_file):
    with wave.open(output_file, 'w') as wav_file:
        with open(input_file, 'rb') as txt_file:
            data = txt_file.read()
            wav_file.setnchannels(2)           # Set to stereo
            wav_file.setsampwidth(1)
            wav_file.setframerate(48000)       # Set sample rate to 48000 Hz
            encoded_data = bytes([byte ^ 0b10101010 for byte in data])
            
            # Duplicate each byte to both channels for stereo
            stereo_data = bytearray()
            for byte in encoded_data:
                stereo_data.extend([byte, byte])
            
            wav_file.writeframes(stereo_data)

def decode(input_file, output_file):
    with wave.open(input_file, 'r') as wav_file:
        with open(output_file, 'wb') as txt_file:
            data = wav_file.readframes(wav_file.getnframes())
            
            # Extract only one channel (assuming both channels contain the same data)
            decoded_data = bytes([data[i] ^ 0b10101010 for i in range(0, len(data), 2)])
            
            txt_file.write(decoded_data)

if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('mode', choices=['encode', 'decode'])
    parser.add_argument('input_file')
    parser.add_argument('output_file')
    args = parser.parse_args()
    if args.mode == 'encode':
        encode(args.input_file, args.output_file)
    else:
        decode(args.input_file, args.output_file)
