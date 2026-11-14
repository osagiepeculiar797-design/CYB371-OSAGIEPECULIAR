
# Role-Based Access Control (RBAC)
#24/15224
#Osagie peculiar

# 1. Define roles and their permissions
roles_allowance = {
    "Admin": ["view", "add", "edit", "delete"],
    "Teacher": ["view", "add", "edit"],
    "Student": ["view"]
}

# Define fictional users and assign roles
users = {
    "Peculiar": "Admin",
    "John": "Teacher",
    "Mary": "Student",
    "Peter": "Student"
}

# 2. Create a function to check permissions
def check_permission(username, permission):

    # Check if the user exists
    if username not in users:
        return "Access Denied: User does not exist."

    # Get the user's role
    role = users[username]

    # Get the permissions assigned to that role
    permissions = roles_allowance[role]

    # Check whether the permission is allowed
    if permission in permissions:
        return f"Access Granted: {username} can {permission}."

    else:
        return f"Access Denied: {username} cannot {permission}."


# 3. Test the access control system
print(check_permission("Peculiar", "delete"))
print(check_permission("John", "edit"))
print(check_permission("Mary", "delete"))
print(check_permission("Peter", "view"))
print(check_permission("James", "add"))
