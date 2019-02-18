"""A module for protecting subject privacy.

The problem addressed by this code is relatively straightforward: we
want to be able to record data about some population of users, but we
have to make sure that there is no possibility of matching a user's
data to their personally identifiable information. This is relatively
easy to do on the client side, as we can simply require authentication
to see any such data. However, in the case that the server itself is
breached, which of course is already improbably low, we also need to
make sure that the database representation of the data does not tie
a particular user to their data. At the same time, we want to allow
users to access their own data when they're authenticated.

The solution is to simply put the linking of a user's own information
in their hands. What piece of identification do they always have? A
username or email and password. By hashing that data with a salt to
guarantee uniqueness, we can create a one-way key for users to look
up their data without the server having to store anything about the
transaction in its database.
"""
