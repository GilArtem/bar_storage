from app.crud.user import get_user_by_email, create_user
from app.schemas.user import UserCreate
from app.security import pwd_context


def test_create_user(sqlite_session):
    user_data = UserCreate(
        email='test@example.com', 
        password='securepassword',
        is_active=True,
        is_superuser=False,
        )
    user = create_user(sqlite_session, user_data)
    assert user.email == 'test@example.com'
    assert pwd_context.verify('securepassword', user.hashed_password)
    assert user.is_active is True
    assert user.is_superuser is False

def test_get_user_by_email(sqlite_session):
    # Добавляем пользователя
    user_data = UserCreate(email='test@example.com', password='securepassword')
    create_user(sqlite_session, user_data)

    # Проверяем, что пользователь доступен
    user = get_user_by_email(sqlite_session, 'test@example.com')
    assert user is not None
    assert user.email == 'test@example.com'
    assert pwd_context.verify('securepassword', user.hashed_password)