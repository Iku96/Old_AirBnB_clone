#!/usr/bin/python3
# AirBnB Clone

This project is a command-line interface (CLI) implementation of a simplified AirBnB clone. It allows users to create, view, update, and delete objects such as users, places, and reviews. The project uses a JSON file as a simple database to store and retrieve data.

## Command Interpreter

### Starting the Command Interpreter

To start the command interpreter, run the `console.py` file:

```
$ python3 console.py
```

### Using the Command Interpreter

Once the command interpreter is started, you can enter commands to interact with the system. Commands are entered in the following format:

```
command class_id command_action
```

- `command` is the name of the command, such as `create`, `show`, `update`, or `destroy`.
- `class_id` is the name of the class you want to interact with, such as `User`, `Place`, or `Review`.
- `command_action` is any additional information needed to complete the command, such as the ID of the object you want to show or update.

### Examples

Here are some examples of commands you can enter:

```
(hbnb) create User
00e601e9-44a4-49de-a68e-520f2c2dfe5e
(hbnb) show User 00e601e9-44a4-49de-a68e-520f2c2dfe5e
[User] (00e601e9-44a4-49de-a68e-520f2c2dfe5e) {'id': '00e601e9-44a4-49de-a68e-520f2c2dfe5e', 'created_at': datetime.datetime(2022, 5, 9, 0, 0), 'updated_at': datetime.datetime(2022, 5, 9, 0, 0)}
(hbnb) update User 00e601e9-44a4-49de-a68e-520f2c2dfe5e name "John Doe"
(hbnb) show User 00e601e9-44a4-49de-a68e-520f2c2dfe5e
[User] (00e601e9-44a4-49de-a68e-520f2c2dfe5e) {'id': '00e601e9-44a4-49de-a68e-520f2c2dfe5e', 'created_at': datetime.datetime(2022, 5, 9, 0, 0), 'updated_at': datetime.datetime(2022, 5, 9, 0, 1), 'name': 'John Doe'}
(hbnb) destroy User 00e601e9-44a4-49de-a68e-520f2c2dfe5e
(hbnb) show User 00e601e9-44a4-49de-a68e-520f2c2dfe5e
** no instance found **
```

## Author

- Ikundwila Mwambona <ikumwana@gmail.com>
