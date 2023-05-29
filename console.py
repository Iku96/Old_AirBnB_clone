#!/usr/bin/python3

import cmd
import sys
import models

class HBNBCommand(cmd.Cmd):
    prompt = "(hbnb) "

    def do_quit(self, arg):
        """Quit command to exit the program"""
        return True

    def do_EOF(self, arg):
        """Exit the program on EOF (Ctrl+D)"""
        print()
        return True

    def emptyline(self):
        """Do nothing on empty line"""
        pass

    def do_create(self, arg):
        """Creates a new instance of BaseModel, saves it, and prints the id"""
        if not arg:
            print("** class name missing **")
            return

        try:
            new_instance = models.classes[arg]()
            new_instance.save()
            print(new_instance.id)
        except KeyError:
            print("** class doesn't exist **")

    def do_show(self, arg):
        """Prints the string representation of an instance"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        try:
            cls_name = args[0]
            obj_id = args[1]
            instance_key = "{}.{}".format(cls_name, obj_id)
            instances = models.storage.all()
            if instance_key in instances:
                print(instances[instance_key])
            else:
                print("** no instance found **")
        except IndexError:
            if cls_name not in models.classes:
                print("** class doesn't exist **")
            elif len(args) < 2:
                print("** instance id missing **")

    def do_destroy(self, arg):
        """Deletes an instance based on the class name and id"""
        args = arg.split()
        if not args:
            print("** class name missing **")
            return

        try:
