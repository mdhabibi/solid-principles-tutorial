"""
Example code with SOLID principle violations for demonstration purposes.

This file contains various violations that the SOLID Inspector will detect.
"""

# ❌ SRP Violation: Class with multiple responsibilities
class UserManager:
    """Violates SRP - handles user management, email, and database operations."""
    
    def __init__(self):
        self.users = []
    
    def add_user(self, user):
        """Add a user to the system."""
        self.users.append(user)
        print(f"User {user} added")
    
    def send_email(self, user, message):
        """Send email to user - not the responsibility of UserManager!"""
        print(f"Sending email to {user}: {message}")
    
    def save_to_database(self, user):
        """Save user to database - not the responsibility of UserManager!"""
        print(f"Saving {user} to database")


# ❌ OCP Violation: Hard-coded logic that requires modification for new types
class AreaCalculator:
    """Violates OCP - requires modification to add new shapes."""
    
    def calculate_area(self, shape_type, *args):
        if shape_type == "rectangle":
            return args[0] * args[1]
        elif shape_type == "circle":
            return 3.14 * args[0] * args[0]
        # Adding new shapes requires modifying this method!
        else:
            raise ValueError(f"Unknown shape type: {shape_type}")


# ❌ LSP Violation: Square that doesn't properly substitute Rectangle
class Rectangle:
    """A rectangle with width and height."""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height
    
    def area(self):
        return self.width * self.height


class Square(Rectangle):
    """Violates LSP - doesn't properly substitute Rectangle."""
    
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side
    
    def set_width(self, width):
        # ❌ Problem: This changes both width and height!
        self.width = width
        self.height = width
        self.side = width
    
    def set_height(self, height):
        # ❌ Problem: This changes both width and height!
        self.width = height
        self.height = height
        self.side = height


# ❌ ISP Violation: Fat interface forcing unnecessary implementations
class Worker:
    """Violates ISP - forces all workers to implement everything."""
    
    def work(self):
        pass
    
    def eat(self):
        pass
    
    def sleep(self):
        pass


class Robot(Worker):
    """Robot forced to implement methods it doesn't need."""
    
    def work(self):
        print("Robot is working")
    
    def eat(self):
        # ❌ Problem: Robots don't eat!
        raise NotImplementedError("Robots don't eat!")
    
    def sleep(self):
        # ❌ Problem: Robots don't sleep!
        raise NotImplementedError("Robots don't sleep!")


# ❌ DIP Violation: High-level module depending on low-level modules
class EmailService:
    """Low-level email service."""
    
    def send_email(self, to, subject, body):
        print(f"Email sent to {to}: {subject}")


class DatabaseService:
    """Low-level database service."""
    
    def save_user(self, user_data):
        print(f"User saved to database: {user_data}")


class UserService:
    """Violates DIP - depends directly on concrete implementations."""
    
    def __init__(self):
        # ❌ Problem: Direct dependency on concrete classes
        self.email_service = EmailService()
        self.database_service = DatabaseService()
    
    def register_user(self, user_data):
        self.database_service.save_user(user_data)
        self.email_service.send_email(
            user_data['email'], 
            "Welcome!", 
            f"Welcome {user_data['name']}!"
        )


# Example usage
if __name__ == "__main__":
    print("🔍 This file contains various SOLID principle violations")
    print("📚 Use the SOLID Inspector to analyze this code!")
    print("💡 Check out the tutorials to learn how to fix these issues")
