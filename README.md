# LoSt (Longmont Standard encryption system) v0.1.0

LoSt is an encryption system that encodes a message into an audio file using the LSB (Least Significant Bit) method. This can be used to send secret messages or data over an audio channel.
It is currently very early in development (around 97% of the code in this prototype was done by ChatGPT) and thus needs some work.

## Planned Changes
Add some kind of key system
Add a way to change what frequencies are used
GnuPG/GPG integration
Develop some kind of frontend

## Installation

1. Clone the repository or download the source code.
2. Install the required Python libraries: numpy, scipy, and wave.

## Usage

lost.py [mode] input_file output_file

where `mode` is either `encode` or `decode`.

### Encoding

lost.py encode input_file output_file

This will encode the message in the `input_file` into the audio file specified by `output_file`.

### Decoding

lost.py decode input_file

This will decode the message hidden in the audio file specified by `input_file`.
You can also change the name of the decoded output by adding an `output_file` in the same format as the original

## License

LoSt is released under the BSD license.

## Contact

If you have any questions or comments about LoSt, please contact the author at ouncerecords@outlook.com.
