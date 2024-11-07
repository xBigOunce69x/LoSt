LoSt (Longmont Standard encryption system) - Studio Edition
version 0.3.0

LoSt Studio Edition is an advanced encryption system that encodes a message into an audio file using the LSB (Least Significant Bit) method. 
This version introduces high-quality, 48000 Hz stereo encoding, making it suitable for embedding hidden data or “Easter eggs” in professional audio tracks. 
This tool is ideal for artists, musicians, or those seeking a discreet way to hide sensitive information within audio files.
It is currently early in development (around 95-97% of the code in this program was done by ChatGPT) and thus needs some work.

## Studio Edition Features
-48000hz stereo encoding: allows for encrypted files to be hidden in music and other high-quality audio tracks in a seperate channel that can be decrypted with LoSt:SE

## Changelog
-Added High-Fidelity 48000hz stereo output
-Optimized for embedding files into HQ audio tracks
-General bug fixes

## Planned Changes
-Add encryption key system
-Add custom frequency settings for further data obfuscation
-GnuPG/GPG integration
-Add a GUI
-Learn how to actually f***ing code

## Installation

1. Clone the repository or download the source code.
2. Install the required Python libraries: numpy, scipy, and wave.

## Usage

loststudio.py [mode] input_file output_file

where `mode` is either `encode` or `decode`.

### Encoding

loststudio.py encode input_file output_file

This will encode the message in the `input_file` into the audio file specified by `output_file`.

### Decoding

loststudio.py decode input_file

This will decode the message hidden in the audio file specified by `input_file`.
You can also change the name of the decoded output by adding an `output_file` in the same format as the original

## License

LoSt Studio Edition is released under the BSD license.

## Contact

If you have any questions or comments about LoSt or LoSt:SE, please contact the author at ouncerecords@outlook.com.



