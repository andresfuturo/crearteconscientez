SELECT * 
FROM user_customuser;

SELECT  *
FROM user_customuser_insert aui;



create table user_customuser_insert(
	id_user int,
	username varchar(50)
)



-----------------------------------------------------------------------------------------------

tabla para cuando se inserte un usuario
CREATE TRIGGER tgr_user_customuser_insert
AFTER INSERT
ON user_customuser
FOR EACH ROW
BEGIN
		insert into user_customuser_insert
		values(NEW.id, NEW.username);
END


tabla de actualizacion de un usuario
CREATE TRIGGER tgr_user_customuser_update
AFTER UPDATE 
ON user_customuser
FOR EACH ROW
BEGIN
    UPDATE user_customuser_insert
    SET username = NEW.username
    WHERE id_user = NEW.id;
END;

tabla de borrado de un usuario
CREATE TRIGGER tgr_user_customuser_delete
AFTER DELETE ON user_customuser
FOR EACH ROW
BEGIN
    DELETE FROM user_customuser_insert
    WHERE id_user = OLD.id;
END;




-----------------------------------------------------------------------------------------------
las siguientes dos van juntas que crea un nuevo usuario

INSERT INTO user_customuser (
    id, password, username, first_name, last_name, email,
    is_superuser, is_staff, is_active, date_joined, nombre, apellido, fecha_nacimiento
)

VALUES (
    66, 'Programa124', 'Sandros', 'Diaz', 'Toco', 'Sandrita1@example.com',
    1, 1, 1, DATE(), 'Sandra123', 'Torres',NULL 
);

------------------------------------------------------------------------------------------

actualización de usuario

UPDATE user_customuser
SET username = 'SandraUpdated'
WHERE id = 66;

------------------------------------------------------------------------------------------

eliminar usuario

DELETE FROM user_customuser
WHERE id = 66;

