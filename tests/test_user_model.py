"""Tests User model functionalities.

Pytest tests to verify core functionalities of 
the User model including: user creation, data initialization, password
hashing uniqueness, UUID generation, timestamp updates, 
user deletion, and the representation string correctness.

Note: The test functions (excluding pytest fixtures) docstring 
should follow the GIVEN-WHEN-THEN structure:
- GIVEN: what are the initial conditions for the test?
- WHEN: what is occurring that needs to be tested?
- THEN: what is the expected response?
"""
import time

import pytest

from styx import db
from styx.models.user_model import User


@pytest.fixture
def sample_users(init_database):
    """Create sample users for testing."""
    user1 = User(username="user1", email="user1@example.com")
    user1.password = "password1"
        
    user2 = User(username="user2", email="user2@example.com")
    user2.password = "password2"

    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()
    
    return [user1, user2]


def test_user_creation(init_database, sample_users):
    """Verify user data initialization on creation.

    Given: A database with sample users, including 'user1'.
    When:  A user is retrieved from the database by username 'user1'.
    Then:
        - The user exists.
        - `username` is 'user1'.
        - `email` is 'user1@example.com'.
        - `password` verification for 'password1' succeeds.
    """
    user_from_db = User.query.filter_by(username="user1").first()

    assert user_from_db is not None
    assert user_from_db.username == "user1"
    assert user_from_db.email == "user1@example.com"
    assert user_from_db.verify_password("password1")

def test_password_hash_uniqueness(init_database):
    """Verify unique password hashes for different users.

    Ensures that even with the same plaintext password, 
    different users get unique password hashes.

    Given: Two User instances.
    When:  Both users are assigned the same plaintext password and persisted.
    Then:  Their stored password hashes are unique.
    """
    # Create two users with identical passwords
    user1 = User(username="user3", email="user3@example.com")
    user1.password = "samepassword"

    user2 = User(username="user4", email="user4@example.com")
    user2.password = "samepassword"

    db.session.add(user1)
    db.session.add(user2)
    db.session.commit()

    # Verify hashes are different
    # "Password hashes should be unique for different users"
    assert user1.password != user2.password 

def test_uuid_uniqueness(sample_users):
    """Verify unique UUIDs for different users.

    Given: Two sample users.
    When:  Two sample users are created and their IDs are accessed.
    Then:  Their IDs (UUIDs) are different.
    """
    user1, user2 = sample_users
    assert user1.id != user2.id

def test_updated_on_field(init_database, sample_users):
    """Verify `updated_on` field updates when user data changes.

    Given: A User instance from the database.
    When:  A user attribute (e.g., `email`) is updated and committed.
    Then:  The `updated_on` field is updated to a timestamp greater 
    than its original value.
    """
    user1 = sample_users[0]
    
    # Get original timestamp
    original_timestamp = user1.updated_on
    
    # Wait briefly to ensure timestamp will be different
    time.sleep(1)
    
    # Update user
    user1.email = "new_user1@example.com"
    db.session.commit()
    db.session.refresh(user1)
    
    assert user1.updated_on > original_timestamp

def test_user_repr(sample_users):
    """Verify the __repr__ method of the User model.

    Given: A sample User object.
    When:  The repr() function is called on the User object.
    Then:  A string representation matching the expected format is returned,
           containing the username and email of the user.
    """
    user = sample_users[0]
    expected_repr = f"User(username={user.username}, email={user.email})"
    assert repr(user) == expected_repr

def test_user_deletion(init_database, sample_users):
    """Verify user deletion functionality.

    Given: Two sample users in the database.
    When:  Both users are deleted from the database and changes are committed.
    Then:  Neither user can be found in the database by username.
    """
    user1, user2 = sample_users
    
    # Delete users
    db.session.delete(user1)
    db.session.delete(user2)
    db.session.commit()
    
    # Verify deletion
    assert User.query.filter_by(username="user1").first() is None
    assert User.query.filter_by(username="user2").first() is None
