import os
import random
import wave
import struct
import math

# Create a directory to store the audio files
os.makedirs('audio_samples', exist_ok=True)

# Define the number of audio files you want to create
num_files = 50000

# Specify the duration, sample rate, and bit depth for the audio files
duration = 1  # 1 second (shorter duration)
sample_rate = 22050  # Lower sample rate (half of 44.1 kHz)
bit_depth = 16  # 16-bit

max_samples_per_file = (1024 ** 3) // (sample_rate * (bit_depth // 8) * num_files)

for i in range(num_files):
    # Generate a random filename
    filename = f'audio_samples/sample_{i}.wav'

    # Create a new WAV file
    with wave.open(filename, 'w') as wf:
        wf.setnchannels(1)  # Mono audio
        wf.setsampwidth(bit_depth // 8)
        wf.setframerate(sample_rate)
        
        # Generate random audio data and write it to the file
        for _ in range(int(sample_rate * duration)):
            sample = random.randint(-(2**(bit_depth - 1)), 2**(bit_depth - 1) - 1)
            packed_sample = struct.pack('<h', sample)
            wf.writeframes(packed_sample)

    print(f'File {i + 1}/{num_files} created: {filename}')

print('Audio file generation complete.')
