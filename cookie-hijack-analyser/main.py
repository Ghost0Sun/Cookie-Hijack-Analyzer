import requests

def analyze_cookies(url):
    try:
        session = requests.Session()
        response = session.get(url)
        cookies = session.cookies
        
        print(f"\n[+] Cookies received from {url}:")
        for cookie in cookies:
            print(f"\nName: {cookie.name}")
            print(f"Value: {cookie.value}")
            print(f"HttpOnly: {'Yes' if cookie._rest.get('HttpOnly') else 'No'}")
            print(f"Secure: {'Yes' if cookie.secure else 'No'}")

            if not cookie._rest.get("HttpOnly") or not cookie.secure:
                print("⚠️  Potential vulnerability: Missing HttpOnly or Secure flag.")
            else:
                print("✅ Cookie is secure.")

    except requests.exceptions.RequestException as e:
        print(f"Error connecting to {url}: {e}")

if __name__ == "__main__":
    target = input("Enter the URL (e.g., https://example.com): ").strip()
    analyze_cookies(target)
