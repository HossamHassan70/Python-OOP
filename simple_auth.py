import re
import json

# File to store user data
DATA_FILE = "users.txt"

def create_file_if_not_exists():
    """Create the data file if it doesn't exist"""
    try:
        with open(DATA_FILE, 'r') as f:
            pass
    except FileNotFoundError:
        with open(DATA_FILE, 'w') as f:
            f.write("")

def validate_email(email):
    """Validate email format"""
    pattern = r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$'
    return re.match(pattern, email) is not None

def validate_egyptian_phone(phone):
    """Validate Egyptian phone numbers"""
    # Remove spaces and dashes
    phone = re.sub(r'[-\s]', '', phone)
    
    # Egyptian phone patterns:
    # Mobile: 010, 011, 012, 015 followed by 8 digits
    # Can start with +20 or 0020
    patterns = [
        r'^(\+20|0020)?01[0125]\d{8}$',  # With country code or without
        r'^01[0125]\d{8}$'               # Local format
    ]
    
    for pattern in patterns:
        if re.match(pattern, phone):
            return True
    return False

def email_exists(email):
    """Check if email already exists"""
    try:
        with open(DATA_FILE, 'r') as f:
            for line in f:
                if line.strip():
                    user_data = json.loads(line.strip())
                    if user_data['email'].lower() == email.lower():
                        return True
    except FileNotFoundError:
        pass
    except json.JSONDecodeError:
        pass
    return False

def register_user(first_name, last_name, email, password, confirm_password, mobile_phone):
    """Register a new user"""
    # Validation
    errors = []
    
    # Check required fields
    if not all([first_name, last_name, email, password, confirm_password, mobile_phone]):
        errors.append("All fields are required")
    
    # Validate names
    if first_name and not first_name.strip():
        errors.append("First name cannot be empty")
    if last_name and not last_name.strip():
        errors.append("Last name cannot be empty")
    
    # Validate email
    if email and not validate_email(email):
        errors.append("Invalid email format")
    
    # Check if email exists
    if email and email_exists(email):
        errors.append("Email already registered")
    
    # Validate password
    if password and len(password) < 6:
        errors.append("Password must be at least 6 characters long")
    
    # Check password confirmation
    if password != confirm_password:
        errors.append("Passwords do not match")
    
    # Validate Egyptian phone number
    if mobile_phone and not validate_egyptian_phone(mobile_phone):
        errors.append("Invalid Egyptian phone number format")
    
    if errors:
        return False, errors
    
    # Create user record
    user_data = {
        'first_name': first_name.strip(),
        'last_name': last_name.strip(),
        'email': email.lower().strip(),
        'password': password,
        'mobile_phone': mobile_phone.strip()
    }
    
    # Save to file
    try:
        with open(DATA_FILE, 'a') as f:
            f.write(json.dumps(user_data) + '\n')
        return True, ["Registration successful!"]
    except Exception as e:
        return False, [f"Error saving user data: {str(e)}"]

def login_user(email, password):
    """Authenticate user login"""
    if not email or not password:
        return False, ["Email and password are required"]
    
    if not validate_email(email):
        return False, ["Invalid email format"]
    
    try:
        with open(DATA_FILE, 'r') as f:
            for line in f:
                if line.strip():
                    user_data = json.loads(line.strip())
                    if (user_data['email'].lower() == email.lower() and 
                        user_data['password'] == password):
                        return True, ["Login successful!", user_data]
    except FileNotFoundError:
        return False, ["No users registered yet"]
    except json.JSONDecodeError:
        return False, ["Error reading user data"]
    
    return False, ["Invalid email or password"]

def get_user_by_email(email):
    """Get user data by email"""
    try:
        with open(DATA_FILE, 'r') as f:
            for line in f:
                if line.strip():
                    user_data = json.loads(line.strip())
                    if user_data['email'].lower() == email.lower():
                        return user_data
    except (FileNotFoundError, json.JSONDecodeError):
        pass
    return None

def display_all_users():
    """Display all registered users (for testing purposes)"""
    try:
        with open(DATA_FILE, 'r') as f:
            lines = f.readlines()
            if not lines:
                print("No users registered yet.")
                return
            
            print("\n--- Registered Users ---")
            for i, line in enumerate(lines, 1):
                if line.strip():
                    try:
                        user_data = json.loads(line.strip())
                        print(f"{i}. {user_data['first_name']} {user_data['last_name']} - {user_data['email']} - {user_data['mobile_phone']}")
                    except json.JSONDecodeError:
                        print(f"{i}. Invalid user data")
    except FileNotFoundError:
        print("No users registered yet.")

def main():
    """Main application interface"""
    create_file_if_not_exists()
    
    while True:
        print("\n=== Simple Authentication System ===")
        print("1. Register")
        print("2. Login")
        print("3. View All Users")
        print("4. Exit")
        
        choice = input("\nSelect an option (1-4): ").strip()
        
        if choice == '1':
            print("\n--- User Registration ---")
            first_name = input("First Name: ")
            last_name = input("Last Name: ")
            email = input("Email: ")
            password = input("Password: ")
            confirm_password = input("Confirm Password: ")
            mobile_phone = input("Mobile Phone (Egyptian): ")
            
            success, messages = register_user(
                first_name, last_name, email, password, confirm_password, mobile_phone
            )
            
            if success:
                print(f"\n✓ {messages[0]}")
            else:
                print("\n✗ Registration failed:")
                for msg in messages:
                    print(f"  - {msg}")
        
        elif choice == '2':
            print("\n--- User Login ---")
            email = input("Email: ")
            password = input("Password: ")
            
            success, result = login_user(email, password)
            
            if success:
                user_data = result[1]
                print(f"\n✓ {result[0]}")
                print(f"Welcome, {user_data['first_name']} {user_data['last_name']}!")
                print(f"Email: {user_data['email']}")
                print(f"Phone: {user_data['mobile_phone']}")
            else:
                print(f"\n✗ Login failed: {result[0]}")
        
        elif choice == '3':
            display_all_users()
        
        elif choice == '4':
            print("\nGoodbye!")
            break
        
        else:
            print("\n✗ Invalid choice. Please select 1, 2, 3, or 4.")

if __name__ == "__main__":
    main()