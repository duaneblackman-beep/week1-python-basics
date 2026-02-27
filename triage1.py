import os
import anthropic
from pathlib import Path
from dotenv import load_dotenv

# Walk up from this notebook's location to find the .env file
notebook_dir = Path(__file__).resolve().parent
for directory in [notebook_dir] + list(notebook_dir.parents):
    env_file = directory / ".env"
    if env_file.exists():
        load_dotenv(env_file)
        print(f"✅ Found .env at: {env_file}")
        break

# Verify key loaded
api_key = os.getenv("ANTHROPIC_API_KEY")
if api_key:
    print(f"✅ API key loaded — starts with: {api_key[:10]}...")
else:
    print("❌ API key not found — check your .env file")

client = anthropic.Anthropic(api_key=api_key)