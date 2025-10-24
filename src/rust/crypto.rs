//! Cryptographic utilities for Ed25519 signing.

use ed25519_dalek::{Signer, Verifier, SigningKey, VerifyingKey, Signature};
use rand::rngs::OsRng;

/// Generate a new Ed25519 key pair
/// Returns (private_key_base58, public_key_base58)
pub fn generate_keypair() -> (String, String) {
    let mut csprng = OsRng;
    let signing_key = SigningKey::generate(&mut csprng);
    let verifying_key = signing_key.verifying_key();
    
    let private_key_base58 = bs58::encode(signing_key.to_bytes()).into_string();
    let public_key_base58 = bs58::encode(verifying_key.to_bytes()).into_string();
    
    (private_key_base58, public_key_base58)
}

/// Sign data using Ed25519 with a private key
/// Returns the signature as a Base58 string
pub fn generate_signature(data: &str, private_key_base58: &str) -> Result<String, String> {
    let private_key_bytes = bs58::decode(private_key_base58)
        .into_vec()
        .map_err(|e| format!("Invalid private key Base58: {}", e))?;
    
    if private_key_bytes.len() != 32 {
        return Err("Private key must be 32 bytes".to_string());
    }
    
    let mut key_array = [0u8; 32];
    key_array.copy_from_slice(&private_key_bytes);
    
    let signing_key = SigningKey::from_bytes(&key_array);
    let signature = signing_key.sign(data.as_bytes());
    
    Ok(bs58::encode(signature.to_bytes()).into_string())
}

/// Verify an Ed25519 signature
/// Returns true if the signature is valid
pub fn verify_signature(data: &str, signature_base58: &str, public_key_base58: &str) -> Result<bool, String> {
    let signature_bytes = bs58::decode(signature_base58)
        .into_vec()
        .map_err(|e| format!("Invalid signature Base58: {}", e))?;
    
    let public_key_bytes = bs58::decode(public_key_base58)
        .into_vec()
        .map_err(|e| format!("Invalid public key Base58: {}", e))?;
    
    if public_key_bytes.len() != 32 {
        return Err("Public key must be 32 bytes".to_string());
    }
    
    let mut key_array = [0u8; 32];
    key_array.copy_from_slice(&public_key_bytes);
    
    let verifying_key = VerifyingKey::from_bytes(&key_array)
        .map_err(|e| format!("Invalid public key: {}", e))?;
    
    let signature = Signature::from_slice(&signature_bytes)
        .map_err(|e| format!("Invalid signature: {}", e))?;
    
    match verifying_key.verify(data.as_bytes(), &signature) {
        Ok(_) => Ok(true),
        Err(_) => Ok(false),
    }
}
