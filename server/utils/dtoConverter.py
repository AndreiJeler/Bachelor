from Data.user import User


class DTOConverter:
    @staticmethod
    def convert_to_userDto(user: User):
        return {"email": user.email, "name": user.name, "id": str(user.id)}
