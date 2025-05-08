import os
import math

# Folder tempat lagu-lagu disimpan
folder_path = "YOUR PATHH"  # Ganti dengan lokasi folder kamu

# Mendapatkan daftar file dalam folder dan menghapus ekstensinya
songs = [os.path.splitext(f)[0] for f in os.listdir(folder_path) if f.endswith((".mp3", ".wav", ".flac"))]

# Jumlah bagian (split menjadi 8 array)
num_parts = 8
songs_per_part = math.ceil(len(songs) / num_parts)

# Membagi lagu menjadi 8 bagian
song_lists = [songs[i:i + songs_per_part] for i in range(0, len(songs), songs_per_part)]

# Menampilkan hasil dalam format array
for i, part in enumerate(song_lists):
    print(f"song_list_{i+1} = {part}\n")
