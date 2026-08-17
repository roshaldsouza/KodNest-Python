class CandidateProfile:
    def __init__(self, name, email, score):
        self.name = name
        self._email = email
        self.__score = score

    def get_email(self):
        return self._email

    def get_score(self):
        return self.__score


name = input().strip()
email = input().strip()
score = int(input())

# Create one CandidateProfile object
candidate = CandidateProfile(name, email, score)

# Print the name directly
print("CANDIDATE PROFILE")
print("Name:", candidate.name)

# Print the email using get_email()
print("Email:", candidate.get_email())

# Print the score using get_score()
print("Score:", candidate.get_score())