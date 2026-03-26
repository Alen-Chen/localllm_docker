from huggingface_hub import hf_hub_download

# Replace with the model repo and GGUF filename you want
repo_id = "unsloth/Qwen3-Coder-Next-GGUF"
filrname = "Qwen3-Coder-Next-UD-Q6_K_XL-00003-of-00003.gguf"

# Download file
file_path = hf_hub_download(
  repo_id=repo_id,
  filename=filename,
  local_dir="./models",
  local_dir_use_symlinks=False
)

print(f"Downloaded to: {file_path}")
