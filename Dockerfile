# Gunakan base image Python
FROM python:3.11-slim

# Tetapkan direktori kerja di dalam container
WORKDIR /app

# Instal pustaka sistem yang diperlukan (termasuk libGL)
RUN apt-get update && apt-get install -y --no-install-recommends \
    libgl1 \
    libglib2.0-0 \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

# Salin semua file ke dalam container
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Buat direktori untuk hasil prediksi jika belum ada
RUN mkdir -p results uploads

# Expose port 8000
EXPOSE 8000

# Jalankan aplikasi menggunakan Uvicorn
CMD ["uvicorn", "app:app", "--host", "0.0.0.0", "--port", "8000"]
