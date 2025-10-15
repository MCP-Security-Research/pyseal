"""Setup the storage of the vurze keypair in a .env file."""

import os
from pathlib import Path
from typing import Optional, Tuple
from dotenv import load_dotenv, set_key
from vurze import generate_keypair

def setup_keypair(env_path: Optional[str | Path] = None) -> Tuple[str, str]:
    """
    Generate and store keypair securely.
    
    Args:
        env_path: Optional path to .env file. If None, creates in current directory.
    """
    # Determine .env location
    if env_path is None:
        env_path = Path.cwd() / '.env'
    else:
        env_path = Path(env_path)
    
    # Create .env if it doesn't exist
    env_path.touch(exist_ok=True)

    # Generate keypair using the Rust function
    private_key_hex, public_key_hex = generate_keypair()
    
    # Store keys in .env file
    set_key(str(env_path), "VURZE_PRIVATE_KEY", private_key_hex)
    set_key(str(env_path), "VURZE_PUBLIC_KEY", public_key_hex)
    
    print(f"✅ Vurze keypair generated and saved to {env_path}")
    print("⚠️ Keep your private key secure and never commit it to version control!")
    
    return private_key_hex, public_key_hex


def get_public_key(env_path: Optional[str | Path] = None) -> str:
    """
    Retrieve the public key from the .env file.
    
    Args:
        env_path: Optional path to .env file. If None, looks in current directory.
    
    Returns:
        str: The public key hex string, or None if not found.
    """
    # Determine .env location
    if env_path is None:
        env_path = Path.cwd() / '.env'
    else:
        env_path = Path(env_path)
    
    # Check if .env exists
    if not env_path.exists():
        raise FileNotFoundError(f"No .env file found at {env_path}. Run setup_keypair() first.")
    
    # Load environment variables from .env
    load_dotenv(env_path)
    
    # Get public key
    public_key = os.getenv("VURZE_PUBLIC_KEY")
    
    if public_key is None:
        raise ValueError(f"VURZE_PUBLIC_KEY not found in {env_path}. Run setup_keypair() first.")
    
    return public_key


def get_private_key(env_path: Optional[str | Path] = None) -> str:
    """
    Retrieve the private key from the .env file.
    
    Args:
        env_path: Optional path to .env file. If None, looks in current directory.
    
    Returns:
        str: The private key hex string, or None if not found.
    """
    # Determine .env location
    if env_path is None:
        env_path = Path.cwd() / '.env'
    else:
        env_path = Path(env_path)
    
    # Check if .env exists
    if not env_path.exists():
        raise FileNotFoundError(f"No .env file found at {env_path}. Run setup_keypair() first.")
    
    # Load environment variables from .env
    load_dotenv(env_path)
    
    # Get private key
    private_key = os.getenv("VURZE_PRIVATE_KEY")
    
    if private_key is None:
        raise ValueError(f"VURZE_PRIVATE_KEY not found in {env_path}. Run setup_keypair() first.")
    
    return private_key
