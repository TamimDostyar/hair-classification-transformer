import kagglehub

# Download latest version
path = kagglehub.dataset_download("vyombhatia/the-three-hair-types")

print("Path to dataset files:", path)