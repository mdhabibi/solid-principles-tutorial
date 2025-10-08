"""
Example code following SOLID principles - demonstrates best practices.

This file shows how to properly implement the same functionality
while following all SOLID design principles.
"""

from abc import ABC, abstractmethod


# ✅ SRP: Each class has a single responsibility
class UserManager:
    """Handles only user management operations."""
    
    def __init__(self):
        self.users = []
    
    def add_user(self, user):
        """Add a user to the system."""
        self.users.append(user)
        print(f"User {user} added")


class EmailService:
    """Handles only email operations."""
    
    def send_email(self, user, message):
        """Send email to user."""
        print(f"Sending email to {user}: {message}")


class DatabaseService:
    """Handles only database operations."""
    
    def save_user(self, user):
        """Save user to database."""
        print(f"Saving {user} to database")


# ✅ OCP: Open for extension, closed for modification
class Shape(ABC):
    """Abstract base class for all shapes."""
    
    @abstractmethod
    def area(self):
        """Calculate the area of the shape."""
        pass


class Rectangle(Shape):
    """Rectangle implementation."""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height


class Circle(Shape):
    """Circle implementation."""
    
    def __init__(self, radius):
        self.radius = radius
    
    def area(self):
        return 3.14 * self.radius * self.radius


class AreaCalculator:
    """Follows OCP - can handle any Shape without modification."""
    
    def calculate_total_area(self, shapes):
        return sum(shape.area() for shape in shapes)


# ✅ LSP: Proper inheritance that maintains substitutability
class Shape2D(ABC):
    """Base class for 2D shapes."""
    
    @abstractmethod
    def area(self):
        pass


class Rectangle2D(Shape2D):
    """Rectangle with independent width and height."""
    
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def set_width(self, width):
        self.width = width
    
    def set_height(self, height):
        self.height = height


class Square2D(Shape2D):
    """Square with equal sides - doesn't inherit from Rectangle."""
    
    def __init__(self, side):
        self.side = side
    
    def area(self):
        return self.side * self.side
    
    def set_side(self, side):
        self.side = side


# ✅ ISP: Segregated interfaces
class Workable(ABC):
    """Interface for entities that can work."""
    
    @abstractmethod
    def work(self):
        pass


class Eatable(ABC):
    """Interface for entities that can eat."""
    
    @abstractmethod
    def eat(self):
        pass


class Sleepable(ABC):
    """Interface for entities that can sleep."""
    
    @abstractmethod
    def sleep(self):
        pass


class Human(Workable, Eatable, Sleepable):
    """Human implements all interfaces it needs."""
    
    def work(self):
        print("Human is working")
    
    def eat(self):
        print("Human is eating")
    
    def sleep(self):
        print("Human is sleeping")


class Robot(Workable):
    """Robot only implements the interface it needs."""
    
    def work(self):
        print("Robot is working")


# ✅ DIP: Depend on abstractions, not concretions
class EmailServiceInterface(ABC):
    """Abstraction for email service."""
    
    @abstractmethod
    def send_email(self, to, subject, body):
        pass


class DatabaseServiceInterface(ABC):
    """Abstraction for database service."""
    
    @abstractmethod
    def save_user(self, user_data):
        pass


class SMTPEmailService(EmailServiceInterface):
    """Concrete implementation of email service."""
    
    def send_email(self, to, subject, body):
        print(f"SMTP email sent to {to}: {subject}")


class MySQLDatabaseService(DatabaseServiceInterface):
    """Concrete implementation of database service."""
    
    def save_user(self, user_data):
        print(f"User saved to MySQL: {user_data}")


class UserService:
    """Follows DIP - depends on abstractions."""
    
    def __init__(self, email_service: EmailServiceInterface, 
                 database_service: DatabaseServiceInterface):
        # ✅ Depends on abstractions, not concrete classes
        self.email_service = email_service
        self.database_service = database_service
    
    def register_user(self, user_data):
        self.database_service.save_user(user_data)
        self.email_service.send_email(
            user_data['email'], 
            "Welcome!", 
            f"Welcome {user_data['name']}!"
        )


# Example usage
if __name__ == "__main__":
    print("✅ This file demonstrates proper SOLID principle implementation")
    print("📚 Compare with bad_example.py to see the differences")
    print("🎯 All classes follow their respective SOLID principles")
    
    # Demonstrate the good examples
    shapes = [Rectangle(5, 3), Circle(4)]
    calculator = AreaCalculator()
    total_area = calculator.calculate_total_area(shapes)
    print(f"Total area: {total_area}")
    
    # Demonstrate proper dependency injection
    email_service = SMTPEmailService()
    db_service = MySQLDatabaseService()
    user_service = UserService(email_service, db_service)
    
    user_data = {'name': 'John', 'email': 'john@example.com'}
    user_service.register_user(user_data)
