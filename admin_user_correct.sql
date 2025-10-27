-- admin_user_correct.sql
INSERT INTO auth_user (password, is_superuser, username, first_name, last_name, email, is_staff, is_active, date_joined) 
VALUES (
    'pbkdf2_sha256$1000000$TqR6ZAvjBFX8H6y7u0UDoS$BbOV2Dt9qXa+VsDAdKwbjYFUbtwwxayF1SmXOOiJ2DE=', 
    true, 
    'admin', 
    '', 
    '', 
    'admin123@mail.ru', 
    true, 
    true, 
    NOW()
);