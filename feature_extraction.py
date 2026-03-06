import re
import socket
from urllib.parse import urlparse

# --- Feature Extraction Functions ---

def using_ip(url):
    """Return 1 if URL uses IP address instead of domain, else -1"""
    try:
        host = urlparse(url).netloc
        socket.inet_aton(host)  # check if it's an IP
        return 1
    except:
        return -1

def has_https(url):
    """Return 1 if HTTPS is used, else -1"""
    return 1 if urlparse(url).scheme == "https" else -1

def long_url(url):
    """Check if URL length is suspicious (>75 chars)"""
    return 1 if len(url) >= 75 else -1

def sub_domains(url):
    """Check number of subdomains"""
    host = urlparse(url).netloc
    if host.count('.') > 3:
        return 1
    return -1

def symbol_at(url):
    """Check for '@' symbol"""
    return 1 if "@" in url else -1

# --- Combine into one function ---
def extract_features(url):
    features = []
    features.append(using_ip(url))
    features.append(long_url(url))
    features.append(symbol_at(url))
    features.append(sub_domains(url))
    features.append(has_https(url))
    return features
