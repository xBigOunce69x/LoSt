import argparse
import wave

def encode(input_file, output_file):
    with wave.open(output_file, 'w') as wav_file:
        with open(input_file, 'rb') as txt_file:
            data = txt_file.read()
            freq = 19980
            wav_file.setnchannels(1)
            wav_file.setsampwidth(1)
            wav_file.setframerate(freq)
            for byte in data:
                wav_file.writeframes(bytes([byte ^ 0b10101010]))

def decode(input_file, output_file):
    with wave.open(input_file, 'r') as wav_file:
        with open(output_file, 'wb') as txt_file:
            data = wav_file.readframes(wav_file.getnframes())
            for byte in data:
                txt_file.write(bytes([byte ^ 0b10101010]))

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